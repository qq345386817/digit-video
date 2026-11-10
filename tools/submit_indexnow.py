#!/usr/bin/env python3
"""Notify participating search engines after publishing canonical HTML updates."""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

from check_seo import Page, file_for_url


ROOT = Path(__file__).resolve().parents[1]
HOST = "digit-video.luopeike.com"
BASE = "https://" + HOST
KEY_FILE = ROOT / "06aacb315549422782b8611275debae7.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"
MAX_URLS = 10000


def canonical_urls():
    urls = []
    tree = ET.parse(ROOT / "sitemap.xml")
    for node in tree.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        url = node.findtext("{http://www.sitemaps.org/schemas/sitemap/0.9}loc", "")
        parsed = urlparse(url)
        if (parsed.scheme != "https" or parsed.netloc != HOST
                or parsed.query or parsed.fragment):
            raise ValueError("Sitemap contains a noncanonical or foreign URL: " + url)
        path = file_for_url(url)
        if not path.is_file() or path.suffix != ".html":
            raise ValueError("No HTML page for sitemap URL: " + url)
        page = Page()
        page.path = path
        page.feed(path.read_text(encoding="utf-8"))
        if page.canonicals != [url] or "noindex" in page.robots.lower():
            raise ValueError("URL is not an indexable, self-canonical HTML page: " + url)
        urls.append(url)
    if not urls or len(urls) != len(set(urls)) or len(urls) > MAX_URLS:
        raise ValueError("Expected 1-10000 unique canonical sitemap URLs")
    return urls


def select_urls(urls, requested=None, since=None):
    if requested is not None:
        unknown = set(requested) - set(urls)
        if unknown:
            raise ValueError("Only current canonical sitemap URLs are allowed: " + ", ".join(sorted(unknown)))
        return list(dict.fromkeys(requested))
    if since is None:
        return urls
    # Resolve to a commit before diffing so revision input cannot become an option.
    revision = subprocess.check_output(
        ["git", "rev-parse", "--verify", "--end-of-options", since + "^{commit}"],
        cwd=ROOT, text=True).strip()
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", "-z", revision, "HEAD", "--", "*.html"],
        cwd=ROOT).decode("utf-8").split("\0")
    paths = {ROOT / name for name in changed if name}
    return [url for url in urls if file_for_url(url) in paths]


def payload_for(urls):
    key = KEY_FILE.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[a-zA-Z0-9-]{8,128}", key) or KEY_FILE.name != key + ".txt":
        raise ValueError("IndexNow key must match its root verification filename")
    return {"host": HOST, "key": key, "keyLocation": BASE + "/" + KEY_FILE.name,
            "urlList": urls}


def submit(payload):
    # Never notify before deployment, or mistake an HTML 404 fallback for a key.
    with urlopen(payload["keyLocation"], timeout=30) as response:
        if (response.status != 200 or response.geturl() != payload["keyLocation"]
                or response.read(1024).decode("utf-8").strip() != payload["key"]):
            raise ValueError("Live verification file is missing, redirected or incorrect; deploy first")
    request = Request(ENDPOINT, data=json.dumps(payload).encode("utf-8"),
                      headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    with urlopen(request, timeout=60) as response:
        status = response.status
        if response.geturl() != ENDPOINT or status not in (200, 202):
            raise ValueError("Unexpected IndexNow response: " + str(status))
    return {"httpStatus": status,
            "status": "submitted" if status == 200 else "accepted_key_validation_pending",
            "indexed": "unknown"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--url", action="append", help="Notify only these canonical URLs (repeatable)")
    scope.add_argument("--since", help="Notify current HTML pages changed since this Git revision")
    parser.add_argument("--submit", action="store_true", help="Verify the live key, then POST (default: offline dry run)")
    parser.add_argument("--receipt", type=Path, help="Optional local JSON receipt; keep outside the website repository")
    args = parser.parse_args(argv)
    if args.receipt and args.receipt.resolve().is_relative_to(ROOT):
        parser.error("Keep receipts outside the published website repository")
    report = {"host": HOST, "endpoint": ENDPOINT, "submittedAt": None,
              "mode": "submit" if args.submit else "dry_run"}
    try:
        urls = select_urls(canonical_urls(), args.url, args.since)
        payload = payload_for(urls)
        report.update(urlCount=len(urls), urls=urls, keyLocation=payload["keyLocation"])
        if not urls:
            report["status"] = "no_changed_canonical_pages"
        elif args.submit:
            report.update(submit(payload))
            report["submittedAt"] = datetime.now(timezone.utc).isoformat()
        else:
            report["status"] = "not_submitted"
        code = 0
    except (ValueError, OSError, URLError, ET.ParseError, subprocess.CalledProcessError) as error:
        report.update(status="failed_or_unconfirmed", error=str(error))
        if isinstance(error, HTTPError):
            report["httpStatus"] = error.code
        # A timed-out POST may already have arrived. Do not retry automatically.
        code = 1
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
