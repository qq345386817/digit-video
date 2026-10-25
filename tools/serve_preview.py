#!/usr/bin/env python3
"""Serve the static site locally, including production-style extensionless URLs."""

import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def translate_path(self, path):
        target = Path(super().translate_path(path))
        if target == ROOT / 'favicon.ico':
            target = ROOT / 'favicon/favicon.ico'
        if not target.exists() and target.suffix == '' and target.with_suffix('.html').is_file():
            target = target.with_suffix('.html')
        return str(target)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    print(f'Dig It preview: http://127.0.0.1:{args.port}', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), Handler).serve_forever()
