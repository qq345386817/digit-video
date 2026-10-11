#!/usr/bin/env python3
"""Validate crawlable URLs, metadata, schema, localized docs and static assets."""

import json
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse


ROOT = Path(__file__).resolve().parents[1]
HOST = 'digit-video.luopeike.com'
ERRORS = []


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []
        self.alternates = []
        self.resources = []
        self.h1 = 0
        self.title = ''
        self.description = None
        self.schema = []
        self.in_title = False
        self.in_schema = False
        self.buffer = []
        self.lang = ''
        self.direction = ''
        self.robots = ''
        self.ids = []
        self.meta = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html': self.lang, self.direction = a.get('lang', ''), a.get('dir', '')
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if a.get('id'): self.ids.append(a['id'])
        if tag == 'meta':
            self.meta[a.get('name', a.get('property'))] = a.get('content')
            if a.get('name') == 'description': self.description = a.get('content')
            if a.get('name') == 'robots': self.robots = a.get('content', '')
        if tag == 'link':
            if a.get('rel') == 'canonical': self.canonicals.append(a['href'])
            elif a.get('rel') == 'alternate' and 'hreflang' in a: self.alternates.append((a['hreflang'], a['href']))
            elif a.get('href'): self.resources.append(a['href'])
        if tag in ('a', 'option') and a.get('href', a.get('value')):
            self.resources.append(a.get('href', a.get('value')))
        if tag == 'img':
            self.resources.append(a.get('src', ''))
            if 'alt' not in a: self.fail('Image has no alt attribute')
            if a.get('src', '').endswith('.webp') and not (a.get('width') and a.get('height')):
                self.fail('Workflow image has no intrinsic dimensions')
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_schema, self.buffer = True, []

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
        if tag == 'script' and self.in_schema:
            try:
                nodes = json.loads(''.join(self.buffer))
                self.schema.extend(nodes if isinstance(nodes, list) else [nodes])
            except ValueError as error: self.fail('Invalid JSON-LD: ' + str(error))
            self.in_schema = False

    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.in_schema: self.buffer.append(data)

    def fail(self, message):
        ERRORS.append((str(self.path.relative_to(ROOT)), message))


def file_for_url(url):
    path = ROOT / unquote(urlparse(url).path).lstrip('/')
    if path.is_dir(): return path / 'index.html'
    if path.exists(): return path
    return Path(str(path) + '.html')


def main():
    pages = {}
    for path in sorted(ROOT.rglob('*.html')):
        page = Page()
        page.path = path
        page.feed(path.read_text(encoding='utf-8'))
        if not page.canonicals:
            if path.name not in ('404.html', 'google8bdd3bd447b6e703.html'):
                page.fail('Missing canonical URL')
            continue
        if len(page.canonicals) != 1: page.fail('Expected one canonical URL')
        canonical = page.canonicals[0]
        if canonical in pages: page.fail('Duplicate canonical URL: ' + canonical)
        pages[canonical] = page
        if page.h1 != 1: page.fail('Expected exactly one H1')
        if not page.title.strip() or not page.description: page.fail('Missing title or description')
        for key in ('og:title', 'twitter:title'):
            if page.meta.get(key) != page.title: page.fail(key + ' disagrees with title')
        for key in ('og:description', 'twitter:description'):
            if page.meta.get(key) != page.description: page.fail(key + ' disagrees with description')
        if page.meta.get('og:url') != canonical: page.fail('og:url disagrees with canonical')
        if 'noindex' in page.robots: page.fail('Canonical HTML page is noindex')
        if page.lang == 'ar' and page.direction != 'rtl': page.fail('Arabic page needs RTL')
        if len(page.ids) != len(set(page.ids)): page.fail('Duplicate element IDs')
        if not page.schema: page.fail('Missing JSON-LD')
        for node in page.schema:
            if node.get('@type') == 'SoftwareApplication':
                if node.get('@id') != 'https://' + HOST + '/#app': page.fail('Inconsistent application identity')
                if node.get('downloadUrl') != 'https://apps.apple.com/app/id6508171056': page.fail('Wrong App Store download URL')
            if node.get('@type') == 'WebPage':
                if node.get('url') != canonical: page.fail('WebPage schema URL disagrees with canonical')
                if node.get('description') != page.description: page.fail('WebPage schema description disagrees with meta description')
        for reference in page.resources:
            target = urljoin(canonical, reference)
            parsed = urlparse(target)
            if parsed.netloc != HOST: continue
            path = file_for_url(target)
            if not path.is_file(): page.fail('Missing internal target: ' + target)
            if parsed.fragment and path.suffix == '.html':
                text = path.read_text(encoding='utf-8')
                if f'id="{parsed.fragment}"' not in text: page.fail('Missing anchor: ' + target)

    for canonical, page in pages.items():
        if len(page.alternates) != 13 and urlparse(canonical).path != '/digit-video': page.fail('Expected 12 languages plus x-default')
        if canonical not in [u for _, u in page.alternates]: page.fail('Missing self hreflang')
        for language, target in page.alternates:
            other = pages.get(target)
            if other is None: page.fail('Hreflang does not point to canonical page: ' + target)
            elif canonical not in [u for _, u in other.alternates]: page.fail('Non-reciprocal hreflang: ' + target)

    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    sitemap = ET.parse(ROOT / 'sitemap.xml')
    locations = [n.text for n in sitemap.findall('.//s:loc', ns)]
    if len(locations) != len(set(locations)): ERRORS.append(('sitemap.xml', 'Duplicate URLs'))
    for location in locations:
        if location not in pages: ERRORS.append(('sitemap.xml', 'URL has no canonical page: ' + location))
    for canonical in pages:
        if canonical not in locations: ERRORS.append(('sitemap.xml', 'Missing canonical URL: ' + canonical))

    docs = [path for path in ROOT.rglob('*.md') if path.parent.name != 'tools']
    for path in docs:
        text = path.read_text(encoding='utf-8')
        canonical_match = re.match(r'Canonical page: (\S+)', text)
        if not canonical_match or canonical_match[1] not in pages: ERRORS.append((str(path), 'Missing canonical HTML counterpart'))
        if text.count('```') % 2: ERRORS.append((str(path), 'Unbalanced code fences'))
        if re.search(r'\[[^\]]*\n\s*\n[^\]]*\]\(', text): ERRORS.append((str(path), 'Blank line inside a Markdown link'))
        for target in re.findall(r'\]\((https?://[^)]+)\)', text):
            if urlparse(target).netloc == HOST and not file_for_url(target).is_file(): ERRORS.append((str(path), 'Missing Markdown link: ' + target))
        if 'https://github.com/qq345386817/DigIt' in text: ERRORS.append((str(path), 'Inaccessible CLI source link'))
    llms = (ROOT / 'llms.txt').read_text(encoding='utf-8')
    for target in re.findall(r'\]\((https?://[^)]+)\)', llms):
        if urlparse(target).netloc == HOST and not file_for_url(target).is_file(): ERRORS.append(('llms.txt', 'Missing documentation: ' + target))

    if ERRORS:
        print(json.dumps(ERRORS, ensure_ascii=False, indent=2))
        return 1
    print(f'SEO checks passed: {len(pages)} canonical HTML pages, {len(locations)} sitemap URLs, {len(docs)} Markdown documents and llms.txt.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
