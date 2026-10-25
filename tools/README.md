# Website Content

`workflow-content.json` contains the translated feature descriptions, help, FAQs and workflow guides for all 12 languages. `landing-copy.json` adds the homepage narrative. Reusable brand foundations live in `design-system/`. Regenerate shared tokens, HTML, Markdown, `llms.txt` and the sitemap from the website root:

```sh
python3 tools/build_site_design.py
python3 tools/build_workflow_pages.py --date YYYY-MM-DD
python3 tools/build_site_design.py --check
python3 tools/build_workflow_pages.py --date YYYY-MM-DD --check
python3 tools/check_seo.py
python3 -m unittest discover -s tools -p 'test_site_design.py' -v
```

Use the actual content-update date. Existing guide publication dates are preserved. The generator renders the homepage and retains existing guide text; regenerated sections should be edited in the JSON source. It fingerprints both stylesheets, keeps localized navigation and adds a keyboard skip link. `design-system/README.md` documents the brand; `style/tokens.css` is generated, not edited by hand.

For a browser preview with production-style extensionless links, run `python3 tools/serve_preview.py` and open `http://127.0.0.1:8765`. The editable design draft is `design/canvas.json`; its embedded token snapshot should be refreshed whenever the design system changes. Design tools inject the draft's `support.js` runtime; it is not a public website entry point. Keep browser screenshots and run reports outside this repository.

The CLI is a separate tool with no public distribution at present. Update its availability consistently here before adding a public download link. Do not imply that it is included in the App Store app.

Workflow images show the real Mac app with sample data. Video frames are from Big Buck Bunny, © 2008 Blender Foundation, licensed under CC BY 3.0; retain the adjacent attribution when reusing them.

The Markdown companions are directly readable by agents and marked `noindex` in `_headers` so the corresponding HTML remains the search entry point. `llms.txt` provides a documentation index, not a promise of search ranking or AI recommendations.
