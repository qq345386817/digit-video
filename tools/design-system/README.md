# Dig It

Useful stills. A simpler video workflow.

## Content Fundamentals

Lead with video-to-images, not a video editor or an AI promise. Explain the output before the controls. Mac supports batch folders, sampling and source-frame review; iPhone and iPad process one video at a time. Keep those differences explicit. Do not imply that the separate, unpublished CLI ships with the App Store app. Download links must target App Store ID `6508171056`.

## Visual Foundations

`tokens.json` is the source of truth. `python3 tools/build_site_design.py` generates the website's `style/tokens.css`; never maintain a second hand-edited token sheet. `primary` and `accent` follow the native app's `Color.main` and `Color.mainAccent`, rounded to 8-bit sRGB. Existing warm `bg`, `text`, `muted` and `warm` colors retain the icon's purple-and-gold identity. Light and dark are equally supported.

Use `text` for headings, `muted` for prose and `primary` for actions. Pair primary fills with `on-primary`. `border` is decorative, not a focus indicator: use `accent` for visible keyboard focus. `warm` decorates frame markers, never small text on white. No page-sized gradients or translucent card stacks. The showcase alone uses `stage` with light labels.

Use Avenir Next where available, then Avenir and Trebuchet MS; language-appropriate browser fallbacks render other scripts. No remote font request is required. Display type is responsive, not a fixed desktop size. Body copy is 16px with 1.7 line height; long documentation stays near 76 characters per line. Space follows the 8px scale. Cards use `radius-md`; primary actions remain pill-shaped. All controls have at least 44px touch targets. Respect reduced motion.

## Imagery And Iconography

Use the real `images/app-icon.png` unchanged, never a redrawn logo. Existing Mac screenshots and the contact sheet are real product examples, not interactive web controls. Keep their localized captions stating that the English interface is shown. Retain the adjacent Big Buck Bunny / Blender Foundation / CC BY 3.0 attribution. `images/CREDITS.txt` records the source.

The real App Store glyph remains `images/app-store-icon.svg`. Decorative small icons use inline stroke SVG with `aria-hidden="true"`; meaningful icon-only controls need accessible names. Do not use emoji as interface icons.

## Patterns And Source Inventory

- Download action: filled `primary` pill with App Store glyph and readable text; secondary links use a bordered pill.
- Product stage: one real screenshot, its caption and attribution; no fake status bar or fabricated metrics.
- Workflow: numbered import, review and export steps with distinct headings.
- Guides: linked title, concise description and visible arrow; an entire guide card can be a link.
- Documentation: readable panels, explicit headings, scrollable command examples and native `details` FAQs.
- Navigation: language paths remain crawlable; switching locale keeps the equivalent page. Arabic uses logical CSS and RTL.

Inventory: 12 color tokens across two themes, 6 type styles, 6 spacing tokens, 4 radii and 1 shadow. Four existing image assets plus the App Store glyph are referenced unchanged from the production site. No runtime component bundle is exported: the website is static HTML and CSS, with no framework dependency.

Not synced: no font files exist in the source. No binary assets have been imported into the design-system asset library because its import tool is unavailable in this session. The real production assets remain at their original paths; the editable design draft uses a labeled image placeholder rather than inventing an imported asset ID.
