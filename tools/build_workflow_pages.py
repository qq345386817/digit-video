#!/usr/bin/env python3
"""Render localized workflow docs and their Markdown from one content source."""

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from html import escape, unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin


ROOT = Path(__file__).resolve().parents[1]
BASE = "https://digit-video.luopeike.com"
STORE = "https://apps.apple.com/app/id6508171056"
LOCALES = {
    "en": ("", "en", "English"),
    "zh-Hans": ("zh-Hans", "zh-Hans", "简体中文"),
    "zh-Hant": ("zh-Hant", "zh-Hant", "繁體中文"),
    "es-ES": ("es-ES", "es", "Español"),
    "id": ("id", "id", "Bahasa Indonesia"),
    "it": ("it", "it", "Italiano"),
    "ar-SA": ("ar-SA", "ar", "العربية"),
    "ja": ("ja", "ja", "日本語"),
    "ko": ("ko", "ko", "한국어"),
    "de-DE": ("de-DE", "de", "Deutsch"),
    "fr-FR": ("fr-FR", "fr", "Français"),
    "pt-BR": ("pt-BR", "pt-BR", "Português (Brasil)"),
}
BATCH = "batch-extract-video-frames-on-mac"
CONTACT = "video-contact-sheet"
START = "<!-- digit-workflows:start -->"
END = "<!-- digit-workflows:end -->"
MAIN_RE = re.compile(r"<main(?:\s[^>]*)?>(.*?)</main>", re.S)
SCHEMA_RE = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
BLOCK_RE = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
OUTPUTS = {}


class Tag(HTMLParser):
    def handle_starttag(self, name, attrs):
        self.attrs = dict(attrs)


def edit_tags(html, name, update):
    def replace(match):
        tag = Tag()
        tag.feed(match[0])
        if not update(tag.attrs):
            return match[0]
        return '<' + name + ' ' + ' '.join(
            key if value is None else f'{key}="{escape(value, quote=True)}"'
            for key, value in tag.attrs.items()
        ) + '>'
    return re.sub(r'<' + name + r'\b[^>]*>', replace, html)


def url(locale, page=""):
    prefix = LOCALES[locale][0]
    return BASE + "/" + (prefix + "/" if prefix else "") + page


def local_path(locale, page="index", suffix=".html"):
    return ROOT / LOCALES[locale][0] / (page + suffix)


def paragraph(text):
    return "<p>" + escape(text) + "</p>"


def section(title, content, identifier=None):
    attr = f' id="{identifier}"' if identifier else ""
    return f'<section class="section"{attr}><h2>{escape(title)}</h2>{content}</section>'


def figure(content, filename, caption, width=1208, height=948):
    return (
        '<figure class="workflow-figure">'
        f'<a href="/images/{filename}"><img src="/images/{filename}" '
        f'alt="{escape(caption, quote=True)}" width="{width}" height="{height}" '
        'loading="lazy" decoding="async"></a>'
        f'<figcaption>{escape(caption)}<span class="image-credit">{escape(content["credits"])} '
        '<a href="https://peach.blender.org/about/">Big Buck Bunny</a> · '
        '<a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a>'
        '</span></figcaption></figure>'
    )


def guide_cards(locale, content, exclude=None):
    cards = []
    for path, title, intro in (
        (BATCH, "batchTitle", "batchIntro"),
        (CONTACT, "contactTitle", "contactIntro"),
    ):
        if path == exclude:
            continue
        cards.append(
            f'<a class="feature feature-link" href="{url(locale, path)}">'
            f'<strong>{escape(content[title])}</strong>{paragraph(content[intro])}'
            f'<span class="guide-action">{escape(content["readGuide"])} →</span></a>'
        )
    if exclude:
        cards.append(
            f'<a class="feature feature-link" href="{url(locale, "help")}">'
            f'<strong>{escape(content["helpLabel"])}</strong>{paragraph(content["helpDescription"])}</a>'
        )
    return '<div class="feature-grid two">' + "".join(cards) + "</div>"


def platform(content):
    return section(
        content["platformTitle"],
        '<div class="feature-grid two">'
        '<article class="feature"><h3>Mac</h3>' + paragraph(content["macBody"]) + '</article>'
        '<article class="feature"><h3>iPhone / iPad</h3>' + paragraph(content["iosBody"]) + '</article>'
        '</div>',
        "platforms",
    )


def delivery_workflows(content, sampling=True):
    note = '<p class="availability-note">' + escape(content['availability']) + '</p>'
    blocks = ''
    if sampling:
        blocks += section(content['samplingTitle'], note + paragraph(content['samplingBody']), 'frame-sampling')
    blocks += section(content['deliveryTitle'], ('' if sampling else note) + paragraph(content['deliveryBody']), 'frame-delivery')
    return blocks


def download_action(copy):
    return (
        f'<a class="button primary" href="{STORE}">'
        '<img class="store-icon" src="/images/app-store-icon.svg" width="22" height="22" alt="">'
        + escape(copy['download']) + '</a>'
    )


def image_credit(content):
    return (
        '<span class="image-credit">' + escape(content['credits'])
        + ' <a href="https://peach.blender.org/about/">Big Buck Bunny</a> · '
        '<a href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</a></span>'
    )


def home_main(locale, content, copy):
    title = ''.join('<span>' + escape(line) + '</span>' for line in copy['title'])
    steps = ''.join(
        f'<li><span class="step-number" aria-hidden="true">0{index}</span>'
        f'<h3>{escape(title)}</h3>{paragraph(body)}</li>'
        for index, (title, body) in enumerate(copy['steps'], 1)
    )
    features = ''.join(
        f'<article class="feature"><span class="feature-index" aria-hidden="true">0{index}</span>'
        f'<h3>{escape(content[title])}</h3>{paragraph(content[body])}</article>'
        for index, (title, body) in enumerate((
            ('batchTitle', 'batchIntro'), ('reviewTitle', 'reviewBody'), ('contactTitle', 'contactIntro')
        ), 1)
    )
    return (
        '<section class="hero"><div class="hero-copy">'
        f'<p class="kicker">{escape(copy["eyebrow"])}</p><h1>{title}</h1>'
        f'<p class="lead">{escape(copy["intro"])}</p><div class="actions">'
        + download_action(copy)
        + f'<a class="text-action" href="#workflow">{escape(copy["secondary"])} <span aria-hidden="true">↗</span></a></div>'
        + f'<p class="device-note">{escape(copy["note"])}</p></div>'
        '<figure class="product-stage"><div class="stage-heading">'
        f'<span>{escape(content["batchTitle"])}</span><span class="stage-device" dir="ltr">macOS</span></div>'
        '<img class="hero-screenshot" src="/images/mac-batch-workspace.webp" width="1208" height="948" '
        f'alt="{escape(content["workspaceCaption"], quote=True)}" fetchpriority="high" decoding="async">'
        f'<figcaption>{escape(content["workspaceCaption"])}{image_credit(content)}</figcaption></figure></section>'
        '<section class="landing-section" id="workflow"><div class="section-heading">'
        f'<h2>{escape(copy["stepsTitle"])}</h2>{paragraph(copy["stepsIntro"])}</div>'
        f'<ol class="step-grid">{steps}</ol></section>'
        '<section class="landing-section" id="mac-workflow"><div class="section-heading">'
        f'<p class="kicker">{escape(copy["platformKicker"])}</p>'
        f'<h2>{escape(content["workflowTitle"])}</h2>{paragraph(content["workflowIntro"])}</div>'
        f'<div class="feature-grid">{features}</div></section>'
        '<section class="landing-section contact-showcase"><div class="section-heading">'
        f'<h2>{escape(copy["showcaseTitle"])}</h2>{paragraph(copy["showcaseBody"])}</div>'
        '<figure class="contact-example"><a href="/images/video-contact-sheet.webp">'
        '<img src="/images/video-contact-sheet.webp" width="1550" height="554" '
        f'alt="{escape(content["contactCaption"], quote=True)}" loading="lazy" decoding="async"></a>'
        f'<figcaption>{escape(content["contactCaption"])}{image_credit(content)}</figcaption></figure></section>'
        + platform(content)
        + '<section class="landing-section technical"><details><summary>'
        + escape(copy['detailsLabel']) + '</summary>' + delivery_workflows(content) + '</details></section>'
        + '<section class="landing-section" id="workflow-guides"><div class="section-heading">'
        f'<p class="kicker">{escape(copy["guideKicker"])}</p><h2>{escape(content["guidesTitle"])}</h2></div>'
        + guide_cards(locale, content) + '</section>'
        + faq(content, copy['faqTitle'])
        + '<section class="download-section"><img src="/images/app-icon.png" width="64" height="64" alt="">'
        f'<h2>{escape(copy["ctaTitle"])}</h2>{paragraph(copy["ctaBody"])}'
        + download_action(copy) + '</section>'
    )


def site_shell(html, locale, landing):
    """Keep generated pages, old guides and localized navigation on one visual shell."""
    def remove_styles(match):
        tag = Tag()
        tag.feed(match[0])
        if tag.attrs.get('rel') == 'stylesheet' and re.search(
            r'(?:^|/)style/(?:base|tokens)\.css(?:\?|$)', tag.attrs.get('href', '')
        ):
            return ''
        return match[0]
    html = re.sub(r'<link\b[^>]*>', remove_styles, html)
    html = re.sub(r'\n[ \t]*\n+', '\n', html)
    styles = ''
    for filename in ('tokens.css', 'base.css'):
        digest = hashlib.sha256((ROOT / 'style' / filename).read_bytes()).hexdigest()[:12]
        styles += f'  <link rel="stylesheet" href="/style/{filename}?v={digest}">\n'
    html = html.replace('</head>', styles + '</head>')
    html = re.sub(r'<a class="skip-link"[^>]*>.*?</a>', '', html)
    html = re.sub(r'(<body[^>]*>)', lambda m: m[1] + '<a class="skip-link" href="#main-content">'
                  + escape(landing[locale]['skip']) + '</a>', html, count=1)
    html = html.replace('<main>', '<main id="main-content">')
    # Give the current navigation item a visible and semantic active state.
    canonical = None
    for tag_text in re.findall(r'<link\b[^>]*>', html):
        tag = Tag()
        tag.feed(tag_text)
        if tag.attrs.get('rel') == 'canonical':
            canonical = tag.attrs['href']
            break
    if canonical is None:
        raise ValueError('Cannot style a page without its canonical URL')
    page_path = canonical.removeprefix(BASE)
    def navigation(match):
        def active(link):
            href = link.group(1)
            target = urljoin(canonical, href).removeprefix(BASE)
            return '<a href="' + href + '"' + (' aria-current="page"' if target == page_path else '') + '>'
        nav = re.sub(r'<a href="([^"]+)"(?: aria-current="page")?>', active, match[0])
        return nav
    html = re.sub(r'<nav class="nav"[^>]*>.*?</nav>', navigation, html, flags=re.S)
    return re.sub(r'[ \t]+\n', '\n', html)


def faq(content, title):
    return section(
        title,
        '<div class="faq-list">' + "".join(
            f'<details><summary>{escape(question)}</summary>{paragraph(answer)}</details>'
            for question, answer in content["faq"]
        ) + '</div>',
        "faq",
    )


def help_main(locale, content, original):
    introduction = re.search(r'<section\b.*?</section>', MAIN_RE.search(original).group(1), re.S).group(0)
    introduction = re.sub(r'<p class="lead">.*?</p>', f'<p class="lead">{escape(content["helpDescription"])}</p>', introduction, count=1, flags=re.S)
    faq_title = {
        "en": "Frequently asked questions", "zh-Hans": "常见问题", "zh-Hant": "常見問題",
        "es-ES": "Preguntas frecuentes", "id": "Pertanyaan umum", "it": "Domande frequenti",
        "ar-SA": "الأسئلة الشائعة", "ja": "よくある質問", "ko": "자주 묻는 질문",
        "de-DE": "Häufige Fragen", "fr-FR": "Questions fréquentes", "pt-BR": "Perguntas frequentes",
    }[locale]
    commands = [
        "digit extract video.mp4 --output ./frames --mode balanced --json frames.json",
        "digit contact-sheet video.mp4 --output sheet.png --columns 4 --limit 40",
        "digit sample video.mp4 --output ./samples --every 10 --max 30 --json samples.json",
        "digit extract video.mp4 --output ./originals --resolution source --json originals.json",
        "digit preset-template --output workflow.json",
        "digit extract video.mp4 --output ./frames --preset workflow.json",
    ]
    cli = section(
        content["cliTitle"],
        '<p class="availability-note">' + escape(content["cliStatus"]) + '</p>'
        f'<a class="button compact" href="{url(locale, "support")}">{escape(content["cliHelp"])}</a>'
        '<div class="cli-code">' + "".join(f'<code dir="ltr">{escape(command)}</code>' for command in commands) + '</div>',
        "cli",
    )
    return (
        introduction + platform(content)
        + section(content['startTitle'], '<ol class="workflow-steps">' + ''.join('<li>' + escape(step) + '</li>' for step in content['startSteps']) + '</ol>', 'getting-started')
        + section(content['modeTitle'], '<ul>' + ''.join('<li>' + escape(item) + '</li>' for item in content['modeItems']) + '</ul>', 'extraction-modes')
        + section(content["guidesTitle"], guide_cards(locale, content), "workflow-guides")
        + delivery_workflows(content)
        + section(content["reviewTitle"], paragraph(content["reviewBody"]) + figure(content, "mac-frame-review.webp", content["reviewCaption"]), "source-frame-review")
        + section(content["saveTitle"], paragraph(content["saveBody"]), "saved-projects")
        + section(content["contactLimitTitle"], paragraph(content["contactLimit"]), "contact-sheet-limit")
        + faq(content, faq_title) + cli
    )


def metadata(html, title=None, description=None):
    if title:
        html = re.sub(r'<title>.*?</title>', '<title>' + escape(title) + '</title>', html, flags=re.S)
    def update(attr):
        key = attr.get('name', attr.get('property'))
        if title and key in ('og:title', 'twitter:title'):
            attr['content'] = title
            return True
        if description and key in ('description', 'og:description', 'twitter:description'):
            attr['content'] = description
            return True
        return False
    return edit_tags(html, 'meta', update)


def app_schema(content):
    return {
        "@context": "https://schema.org", "@type": "SoftwareApplication", "@id": BASE + "/#app",
        "name": "Dig It: Video Keyframes", "alternateName": ["Dig It", "DigIt", "DigIt Video", "DigIt keyframes"],
        "description": content["homeDescription"], "applicationCategory": "MultimediaApplication",
        "operatingSystem": "iOS, iPadOS, macOS", "url": BASE + "/", "downloadUrl": STORE,
        "image": BASE + "/images/app-icon.png", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
    }


def update_schema(html, content, title=None, description=None, date=None):
    def replace(match):
        nodes = json.loads(match[1])
        if isinstance(nodes, dict): nodes = [nodes]
        for index, node in enumerate(nodes):
            if node.get("@type") == "SoftwareApplication":
                nodes[index] = app_schema(content)
            elif node.get("@type") in ("WebPage", "Article"):
                node["@id"] = node["url"] + "#page"
                node["about"] = {"@id": BASE + "/#app"}
                if title: node["name"] = title
                if description: node["description"] = description
                if date: node["dateModified"] = date
        return '<script type="application/ld+json">' + json.dumps(nodes, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + '</script>'
    return SCHEMA_RE.sub(replace, html)


def machine_links(html, locale, page=None):
    html = re.sub(r'\s*<link rel="describedby"[^>]*>', '', html)
    html = re.sub(r'\s*<link rel="alternate" type="text/markdown"[^>]*>', '', html)
    links = '\n  <link rel="describedby" href="/llms.txt">'
    if page:
        links += f'\n  <link rel="alternate" type="text/markdown" href="{url(locale, page + ".md")}">'
    return html.replace('</head>', links + '\n</head>')


def locale_navigation(html, locale, page):
    links = ''.join(
        f'<a href="{url(key, page)}" hreflang="{language}"' + (' aria-current="page"' if key == locale else '') + f'>{name}</a>'
        for key, (_, language, name) in LOCALES.items()
    )
    label_match = re.search(r'<label class="language-switch"><span>(.*?)</span>', html)
    label = label_match[1] if label_match else 'Language'
    nav = f'<nav class="locale-links" aria-label="{label}">{links}</nav>'
    old = re.search(r'<nav class="locale-links"[^>]*>.*?</nav>', html, re.S)
    if old:
        # Preserve the already localized accessible label.
        label = re.search(r'aria-label="([^"]*)"', old[0])[1]
        nav = nav.replace('aria-label="Language"', f'aria-label="{label}"')
        return html[:old.start()] + nav + html[old.end():]
    return html.replace('<footer class="footer">', nav + '<footer class="footer">')


def guide_page(locale, content, kind, template, date):
    is_batch = kind == BATCH
    prefix = "batch" if is_batch else "contact"
    title, intro = content[prefix + "Title"], content[prefix + "Intro"]
    steps = '<ol class="workflow-steps">' + ''.join('<li>' + escape(step) + '</li>' for step in content[prefix + "Steps"]) + '</ol>'
    action = f'<div class="actions"><a class="button primary" href="{STORE}"><img class="store-icon" src="/images/app-store-icon.svg" alt="">App Store</a><a class="button" href="{url(locale, "help")}">{escape(content["helpLabel"])}</a></div>'
    intro_section = (
        '<section class="section"><p class="article-meta">' + escape(content["guideLabel"]) + '</p>'
        f'<h1>{escape(title)}</h1><p class="lead">{escape(intro)}</p>{action}'
        f'<p class="updated">{escape(content["updatedLabel"])}: <time datetime="{date}">{date}</time></p></section>'
    )
    if is_batch:
        body = (
            section(content['startTitle'], steps, "steps")
            + section(content["batchOutputTitle"], paragraph(content["batchOutput"])
                      + figure(content, "mac-batch-workspace.webp", content["workspaceCaption"]), "batch-exports")
            + section(content["batchReviewTitle"], paragraph(content["batchReview"])
                      + figure(content, "mac-frame-review.webp", content["reviewCaption"]), "review")
        )
    else:
        body = (
            section(content['startTitle'], steps, "steps")
            + section(content["contactLimitTitle"], paragraph(content["contactLimit"])
                      + figure(content, "video-contact-sheet.webp", content["contactCaption"], 1550, 554), "limits")
            + section(content["contactUseTitle"], paragraph(content["contactUse"]), "use-the-results")
        )
    body += delivery_workflows(content, sampling=is_batch) + platform(content) + section(content["saveTitle"], paragraph(content["saveBody"]), "saved-projects")
    body += section(content["related"], guide_cards(locale, content, exclude=kind) + f'<p><a href="{url(locale, kind + ".md")}">{escape(content["markdownLabel"])}</a></p>', "related-guides")
    html = MAIN_RE.sub(lambda _: '<main>' + intro_section + body + '</main>', template)
    html = metadata(html, title + ' | Dig It', intro)
    def update_link(attr):
        if attr.get('rel') == 'canonical':
            attr['href'] = url(locale, kind)
            return True
        if attr.get('rel') == 'alternate' and attr.get('hreflang'):
            target_locale = next((key for key, (_, lang, _) in LOCALES.items() if lang == attr['hreflang']), 'en')
            attr['href'] = url(target_locale, kind)
            return True
        return False
    def update_meta(attr):
        if attr.get('property') == 'og:url':
            attr['content'] = url(locale, kind)
            return True
        return False
    html = edit_tags(html, 'link', update_link)
    html = edit_tags(html, 'meta', update_meta)
    html = re.sub(r'<option value="[^"]+"([^>]*)>(.*?)</option>', lambda m: '<option value="' + url(next(key for key, (_, _, name) in LOCALES.items() if name == unescape(m[2])), kind) + '"' + m[1] + '>' + m[2] + '</option>', html)
    def rewrite_schema(match):
        published = date
        existing_path = local_path(locale, kind)
        if existing_path.exists():
            existing = SCHEMA_RE.search(existing_path.read_text(encoding='utf-8'))
            if existing:
                nodes = json.loads(existing[1])
                for node in nodes:
                    if node.get('@type') == 'WebPage' and node.get('url') == url(locale, kind):
                        published = node.get('datePublished', date)
        page = {
            '@context': 'https://schema.org', '@type': 'WebPage', '@id': url(locale, kind) + '#page',
            'name': title + ' | Dig It', 'description': intro, 'url': url(locale, kind),
            'inLanguage': LOCALES[locale][1], 'datePublished': published, 'dateModified': date,
            'about': {'@id': BASE + '/#app'},
            'isPartOf': {'@type': 'WebSite', '@id': BASE + '/#website', 'name': 'Dig It', 'url': BASE + '/'},
        }
        return '<script type="application/ld+json">' + json.dumps([app_schema(content), page], ensure_ascii=False, separators=(',', ':')) + '</script>'
    html = SCHEMA_RE.sub(rewrite_schema, html)
    html = machine_links(html, locale, kind)
    return locale_navigation(html, locale, kind)


class Markdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.numbered = []
        self.in_code = False

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag in ('h1', 'h2', 'h3'):
            self.parts.append('\n\n' + '#' * int(tag[1]) + ' ')
        elif tag == 'summary': self.parts.append('\n\n### ')
        elif tag in ('p', 'div', 'section', 'figure', 'figcaption'): self.parts.append('\n\n')
        elif tag == 'ol': self.numbered.append(0)
        elif tag == 'li':
            if self.numbered:
                self.numbered[-1] += 1
                self.parts.append(f'\n{self.numbered[-1]}. ')
            else: self.parts.append('\n- ')
        elif tag == 'a':
            pass
        elif tag == 'img' and attr.get('alt') and not attr.get('src', '').endswith('app-store-icon.svg'):
            self.parts.append('![' + attr.get('alt', '') + '](' + urljoin(self.canonical, attr['src']) + ')')
        elif tag == 'span' and attr.get('class') == 'image-credit':
            self.parts.append('\n\n')
        elif tag == 'code':
            self.parts.append('\n\n```sh\n')
            self.in_code = True
        if tag == 'a': self.links.append((urljoin(self.canonical, attr.get('href', '')), len(self.parts), attr.get('class', '')))

    def handle_endtag(self, tag):
        if tag == 'a':
            href, start, classes = self.links.pop()
            label = re.sub(r'\s+', ' ', ''.join(self.parts[start:])).strip()
            self.parts[start:] = ['[' + label + '](' + href + ')']
            if 'feature' in classes or 'button' in classes: self.parts.append('\n\n')
        elif tag == 'code':
            self.parts.append('\n```\n')
            self.in_code = False
        elif tag == 'ol': self.numbered.pop()
        elif tag in ('h1', 'h2', 'h3', 'p', 'section', 'li', 'figcaption', 'summary'): self.parts.append('\n')

    def handle_data(self, data):
        self.parts.append(data)

    def render(self, html, canonical):
        self.canonical = canonical
        self.links = []
        self.feed(MAIN_RE.search(html)[1])
        text = re.sub(r'\n{3,}', '\n\n', ''.join(self.parts)).strip()
        return f'Canonical page: {canonical}\n\n{text}\n'


def build(date):
    content = json.loads((ROOT / 'tools/workflow-content.json').read_text(encoding='utf-8'))
    landing = json.loads((ROOT / 'tools/landing-copy.json').read_text(encoding='utf-8'))
    assert set(content) == set(LOCALES), 'Every locale needs translated content'
    assert set(landing) == set(LOCALES), 'Every locale needs landing-page translations'
    expected = set(content['en'])
    for locale, copy in content.items():
        assert set(copy) == expected, f'Incomplete translations: {locale}'
        home_path = local_path(locale)
        home = home_path.read_text(encoding='utf-8')
        body = home_main(locale, copy, landing[locale])
        home = MAIN_RE.sub(lambda _: '<main>' + body + '</main>', home)
        home = home.replace('<body>', '<body class="home">')
        home = metadata(home, copy['homeTitle'], copy['homeDescription'])
        home = update_schema(home, copy, copy['homeTitle'], copy['homeDescription'], date)
        OUTPUTS[home_path] = machine_links(home, locale)

        help_path = local_path(locale, 'help')
        help_html = help_path.read_text(encoding='utf-8')
        help_html = MAIN_RE.sub(lambda _: '<main>' + help_main(locale, copy, help_html) + '</main>', help_html)
        help_html = metadata(help_html, description=copy['helpDescription'])
        help_html = update_schema(help_html, copy, description=copy['helpDescription'], date=date)
        help_html = machine_links(help_html, locale, 'help')
        OUTPUTS[help_path] = locale_navigation(help_html, locale, 'help')

        template = local_path(locale, 'extract-keyframes-from-video').read_text(encoding='utf-8')
        for kind in (BATCH, CONTACT):
            html = guide_page(locale, copy, kind, template, date)
            OUTPUTS[local_path(locale, kind)] = html
            OUTPUTS[local_path(locale, kind, '.md')] = Markdown().render(html, url(locale, kind))
        OUTPUTS[local_path(locale, 'help', '.md')] = Markdown().render(help_html, url(locale, 'help'))

        for name in ('extract-keyframes-from-video', 'video-cover-image-from-video', 'turn-video-into-step-images'):
            path = local_path(locale, name)
            html = path.read_text(encoding='utf-8')
            related = START + section(copy['related'], guide_cards(locale, copy), 'related-workflows') + END
            html = BLOCK_RE.sub('', html).replace('</main>', related + '</main>')
            OUTPUTS[path] = machine_links(update_schema(html, copy, date=date), locale)

    for path in ROOT.rglob('*.html'):
        if 'tools' in path.relative_to(ROOT).parts:
            continue
        if path in OUTPUTS:
            continue
        locale = next((key for key, (prefix, _, _) in LOCALES.items() if prefix and path.parent.name == prefix), 'en')
        original = path.read_text(encoding='utf-8')
        if SCHEMA_RE.search(original):
            OUTPUTS[path] = machine_links(update_schema(original, content[locale]), locale)

    OUTPUTS[ROOT / 'structured-data.json'] = json.dumps(app_schema(content['en']), ensure_ascii=False, indent=2) + '\n'
    llms = [
        '# Dig It: Video Keyframes',
        '> Official documentation for Dig It (DigIt), a local video-to-stills app for macOS, iPhone and iPad.',
        '', content['en']['faq'][2][1], content['en']['faq'][0][1],
        content['en']['macBody'], content['en']['iosBody'],
        content['en']['contactLimit'], content['en']['saveBody'],
        content['en']['faq'][4][1], content['en']['cliStatus'],
        content['en']['availability'], content['en']['samplingBody'], content['en']['deliveryBody'],
        'MCP integration is not provided.',
        '', '## Official documentation',
        f'- [Help and product facts]({BASE}/help.md): Platform differences, local processing, saved projects, limits and CLI availability.',
        f'- [Batch extract video frames on Mac]({BASE}/{BATCH}.md): Queue files or folders, choose presets, review and export.',
        f'- [Create a video contact sheet]({BASE}/{CONTACT}.md): PNG overviews (up to 40 frames) and printable paginated PDF sheets (up to 120 frames).',
        f'- [App Store download]({STORE}): Official pricing and device compatibility.',
        f'- [Support]({BASE}/support): Contact the developer, including questions about the separate CLI.',
        f'- [Privacy policy]({BASE}/privacy-policy): The published privacy policy.',
        '', '## Localized documentation',
    ]
    llms.extend(f'- [{name}]({url(locale, "help.md")}): Localized help and links to workflow guides.' for locale, (_, _, name) in LOCALES.items())
    OUTPUTS[ROOT / 'llms.txt'] = '\n'.join(llms) + '\n'

    namespace = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', namespace)
    sitemap = ET.parse(ROOT / 'sitemap.xml').getroot()
    records = {node.find(f'{{{namespace}}}loc').text: node for node in sitemap}
    for locale in LOCALES:
        for page in ('', 'help', 'extract-keyframes-from-video', 'video-cover-image-from-video', 'turn-video-into-step-images', BATCH, CONTACT):
            location = url(locale, page)
            if location not in records:
                node = ET.SubElement(sitemap, f'{{{namespace}}}url')
                ET.SubElement(node, f'{{{namespace}}}loc').text = location
                records[location] = node
            node = records[location]
            lastmod = node.find(f'{{{namespace}}}lastmod')
            if lastmod is None: lastmod = ET.SubElement(node, f'{{{namespace}}}lastmod')
            lastmod.text = date
    ET.indent(sitemap, space='  ')
    OUTPUTS[ROOT / 'sitemap.xml'] = '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(sitemap, encoding='unicode') + '\n'
    for path, value in list(OUTPUTS.items()):
        if path.suffix == '.html':
            value = site_shell(value, locale_for_path(path), landing)
            head, body = value.split('</head>', 1)
            # Same-origin links work on production and on local/staging previews.
            body = body.replace('href="' + BASE + '/', 'href="/')
            body = body.replace('value="' + BASE + '/', 'value="/')
            OUTPUTS[path] = head + '</head>' + body


def locale_for_path(path):
    return next((key for key, (prefix, _, _) in LOCALES.items()
                 if prefix and path.parent.name == prefix), 'en')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', default='2026-10-11', help='Date of this content update')
    parser.add_argument('--check', action='store_true', help='Check generated files without writing')
    args = parser.parse_args()
    build(args.date)
    differences = [str(path.relative_to(ROOT)) for path, value in OUTPUTS.items() if not path.exists() or path.read_text(encoding='utf-8') != value]
    if args.check:
        if differences:
            raise SystemExit('Outdated generated files: ' + ', '.join(differences))
        print(f'Generated content is current ({len(OUTPUTS)} files).')
        return
    for path, value in OUTPUTS.items():
        path.write_text(value, encoding='utf-8')
    print(f'Updated {len(OUTPUTS)} files in {len(LOCALES)} languages.')


if __name__ == '__main__':
    main()
