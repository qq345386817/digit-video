# Website Content

`workflow-content.json` contains the translated feature descriptions, help, FAQs and workflow guides for all 12 languages. `landing-copy.json` adds the homepage narrative. Reusable brand foundations live in `design-system/`. Regenerate shared tokens, HTML, Markdown, `llms.txt` and the sitemap from the website root:

```sh
python3 tools/build_site_design.py
python3 tools/build_workflow_pages.py --date YYYY-MM-DD
python3 tools/build_site_design.py --check
python3 tools/build_workflow_pages.py --date YYYY-MM-DD --check
python3 tools/check_seo.py
python3 -m unittest discover -s tools -p 'test_site_design.py' -v
python3 -m unittest discover -s tools -p 'test_product_content.py' -v
```

Use the actual content-update date. Existing guide publication dates are preserved. The generator renders the homepage and retains existing guide text; regenerated sections should be edited in the JSON source. It fingerprints both stylesheets, keeps localized navigation and adds a keyboard skip link. `design-system/README.md` documents the brand; `style/tokens.css` is generated, not edited by hand.

Product descriptions follow the App's actual platform boundaries, not a copy of the hidden App Store keywords. Selected stills export as PNG; single cover crops support PNG/JPEG; Mac batch automatic export supports PNG/JPEG and optional JSON. The 40-frame PNG overview and 120-frame paginated PDF limits describe individual exports. Use approachable Chinese product names such as “PDF 缩略图索引页” / “PDF 縮圖總覽”, but keep literal App menu labels “PDF 联系表” / “PDF 聯絡表” in instructions. Keep the English `contact sheet` and Japanese `コンタクトシート` terminology.

The existing cover and tutorial-step URLs are maintained alongside batch/contact-sheet guides. Their introductions, export details, metadata and Markdown companions share `workflow-content.json`; local advice is retained. `llms.txt` groups the same public facts under explicit headings. Keep CLI distribution limitations visible, do not present sampling as an iOS feature, and do not imply that source-resolution export upscales video. Version requirements are minimum versions, not a claim that a pending App Store update has been published.

For a browser preview with production-style extensionless links, run `python3 tools/serve_preview.py` and open `http://127.0.0.1:8765`. The editable design draft is `design/canvas.json`; its embedded token snapshot should be refreshed whenever the design system changes. Design tools inject the draft's `support.js` runtime; it is not a public website entry point. Keep browser screenshots and run reports outside this repository.

The CLI is a separate tool with no public distribution at present. Update its availability consistently here before adding a public download link. Do not imply that it is included in the App Store app.

Workflow images show the real Mac app with sample data. Video frames are from Big Buck Bunny, © 2008 Blender Foundation, licensed under CC BY 3.0; retain the adjacent attribution when reusing them.

The Markdown companions are directly readable by agents and marked `noindex` in `_headers` so the corresponding HTML remains the search entry point. `llms.txt` provides a documentation index, not a promise of search ranking or AI recommendations.

## Search Engine Notifications

`submit_indexnow.py` notifies participating search engines (including Bing) about published HTML updates. The root `<key>.txt` file is a publicly served IndexNow ownership proof, not an account/API secret. Keep it in the deployment. No Google/Bing account credentials or GitHub token are needed, and no new deployment Action is installed.

```sh
python3 tools/submit_indexnow.py                        # Offline dry run
python3 tools/submit_indexnow.py --since HEAD~1         # Changed canonical HTML only
python3 tools/submit_indexnow.py --url https://digit-video.luopeike.com/ --submit
# Initial setup only: notify all current sitemap URLs after deploying the key.
python3 tools/submit_indexnow.py --submit --receipt ../build/seo/indexnow-receipt.json
python3 -m unittest discover -s tools -p 'test_indexnow.py' -v
```

For subsequent releases, deploy first, then use `--since <previous-published-commit> --submit` or repeat `--url` for the pages actually changed. This tool covers current canonical pages, not deleted URLs. It verifies the live key before notifying, rejects foreign URLs/aliases/Markdown, does not retry ambiguous submissions, and distinguishes HTTP 200 receipt from HTTP 202 key-validation-pending. Neither response proves indexing; check Bing's dashboard later. IndexNow does not replace Google Search Console or its sitemap.
