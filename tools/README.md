# Website Content

`workflow-content.json` contains the translated feature descriptions, help, FAQs and workflow guides for all 12 languages. Update it, then regenerate HTML, Markdown, `llms.txt` and the sitemap from the website root:

```sh
python3 tools/build_workflow_pages.py --date YYYY-MM-DD
python3 tools/build_workflow_pages.py --date YYYY-MM-DD --check
python3 tools/check_seo.py
```

Use the actual content-update date. Existing guide publication dates are preserved. The generator retains the established layout and existing guide text; regenerated workflow sections should be edited in the JSON source.

The CLI is a separate tool with no public distribution at present. Update its availability consistently here before adding a public download link. Do not imply that it is included in the App Store app.

Workflow images show the real Mac app with sample data. Video frames are from Big Buck Bunny, © 2008 Blender Foundation, licensed under CC BY 3.0; retain the adjacent attribution when reusing them.

The Markdown companions are directly readable by agents and marked `noindex` in `_headers` so the corresponding HTML remains the search entry point. `llms.txt` provides a documentation index, not a promise of search ranking or AI recommendations.
