#!/usr/bin/env python3
"""Add crawlable locale links next to the existing language switchers."""

from html import unescape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAGES = [ROOT / "index.html", *sorted(ROOT.glob("*/index.html"))]
SELECT_RE = re.compile(r'<label class="language-switch"><span>(.*?)</span><select[^>]*>(.*?)</select></label>')
OPTION_RE = re.compile(r'<option value="([^"]+)"([^>]*)>(.*?)</option>')


def main() -> None:
    for path in PAGES:
        html = path.read_text(encoding="utf-8")
        if '<nav class="locale-links"' in html:
            continue
        match = SELECT_RE.search(html)
        if match is None:
            raise ValueError(f"Missing language switcher: {path}")
        label, options = match.groups()
        links = []
        for url, attributes, name in OPTION_RE.findall(options):
            current = ' aria-current="page"' if "selected" in attributes else ""
            links.append(f'<a href="{url}"{current}>{name}</a>')
        if len(links) != 12:
            raise ValueError(f"Expected 12 locale options in {path}, found {len(links)}")
        nav = f'<nav class="locale-links" aria-label="{unescape(label)}">' + "".join(links) + "</nav>"
        if html.count('<footer class="footer">') != 1:
            raise ValueError(f"Missing footer: {path}")
        path.write_text(html.replace('<footer class="footer">', nav + '<footer class="footer">'), encoding="utf-8")


if __name__ == "__main__":
    main()
