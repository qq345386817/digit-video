function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function stripMarks(node) {
  node.querySelectorAll('mark[data-help-search]').forEach(mark => {
    const text = document.createTextNode(mark.textContent);
    mark.replaceWith(text);
  });
}

function highlightInNode(root, query) {
  stripMarks(root);
  if (!query) return;
  const pattern = new RegExp(`(${escapeRegExp(query)})`, 'ig');
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      if (!node.nodeValue || !node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
      if (node.parentElement && ['SCRIPT', 'STYLE', 'MARK'].includes(node.parentElement.tagName)) return NodeFilter.FILTER_REJECT;
      return pattern.test(node.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
    }
  });
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  nodes.forEach(node => {
    const frag = document.createDocumentFragment();
    const parts = node.nodeValue.split(pattern);
    parts.forEach(part => {
      if (!part) return;
      if (part.toLowerCase() === query.toLowerCase()) {
        const mark = document.createElement('mark');
        mark.setAttribute('data-help-search', '1');
        mark.textContent = part;
        frag.appendChild(mark);
      } else {
        frag.appendChild(document.createTextNode(part));
      }
    });
    node.parentNode.replaceChild(frag, node);
  });
}

function applyHelpSearch() {
  const input = document.getElementById('help-search-input');
  const status = document.getElementById('help-search-status');
  const empty = document.getElementById('help-search-empty');
  const blocks = Array.from(document.querySelectorAll('.searchable-block'));
  const items = Array.from(document.querySelectorAll('.searchable-item'));
  if (!input || !status) return;

  const locale = (window.localStorage && localStorage.getItem('digit-lang')) || 'en';
  const dict = (window.DIGIT_I18N && window.DIGIT_I18N[locale]) || (window.DIGIT_I18N && window.DIGIT_I18N.en) || {};
  const query = input.value.trim();

  [...blocks, ...items].forEach(node => {
    node.hidden = false;
    stripMarks(node);
  });

  if (!query) {
    if (empty) empty.hidden = true;
    status.textContent = dict.searchCleared || 'Search all help topics on this page.';
    const url = new URL(window.location.href);
    url.searchParams.delete('query');
    window.history.replaceState({}, '', `${url.pathname}${url.search}`);
    return;
  }

  let visibleCount = 0;
  items.forEach(item => {
    const text = item.textContent.toLowerCase();
    const match = text.includes(query.toLowerCase());
    item.hidden = !match;
    if (match) {
      visibleCount += 1;
      highlightInNode(item, query);
    }
  });

  blocks.forEach(block => {
    if (block.querySelector('.searchable-item')) {
      const hasVisibleItem = Array.from(block.querySelectorAll('.searchable-item')).some(item => !item.hidden);
      block.hidden = !hasVisibleItem;
      if (hasVisibleItem) highlightInNode(block.querySelector('h2') || block, query);
    } else {
      const match = block.textContent.toLowerCase().includes(query.toLowerCase());
      block.hidden = !match;
      if (match) {
        visibleCount += 1;
        highlightInNode(block, query);
      }
    }
  });

  if (empty) empty.hidden = visibleCount !== 0;
  const template = visibleCount === 1 ? (dict.searchResultsOne || 'Showing 1 matching topic for “{query}”.') : (dict.searchResults || 'Showing {count} matching topics for “{query}”.');
  status.textContent = template.replace('{count}', String(visibleCount)).replace('{query}', query);

  const url = new URL(window.location.href);
  url.searchParams.set('query', query);
  window.history.replaceState({}, '', `${url.pathname}${url.search}`);
}

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('help-search-form');
  const input = document.getElementById('help-search-input');
  if (!form || !input) return;
  const params = new URLSearchParams(window.location.search);
  const initialQuery = params.get('query') || '';
  if (initialQuery) input.value = initialQuery;

  form.addEventListener('submit', e => {
    e.preventDefault();
    applyHelpSearch();
  });

  input.addEventListener('search', applyHelpSearch);
  input.addEventListener('input', () => {
    if (!input.value.trim()) applyHelpSearch();
  });

  document.addEventListener('digit:locale-applied', () => applyHelpSearch());
  applyHelpSearch();
});
