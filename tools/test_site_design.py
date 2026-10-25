import json
import re
import unittest

import build_site_design as design
import build_workflow_pages as pages


class WebsiteDesignTests(unittest.TestCase):
    def test_landing_translations(self):
        copy = json.loads((pages.ROOT / 'tools/landing-copy.json').read_text())
        self.assertEqual(set(copy), set(pages.LOCALES))
        for locale, content in copy.items():
            with self.subTest(locale=locale):
                self.assertEqual(set(content), set(copy['en']))
                self.assertEqual(len(content['title']), 2)
                self.assertEqual(len(content['steps']), 3)
                self.assertTrue(all(len(step) == 2 for step in content['steps']))
                self.assertTrue(all(content.values()))
                if locale != 'en':
                    for key in ('title', 'intro', 'download', 'skip'):
                        self.assertNotEqual(content[key], copy['en'][key])

    def test_design_tokens_current(self):
        self.assertEqual((pages.ROOT / 'style/tokens.css').read_text(), design.stylesheet())

    def test_design_artifact_and_embedded_system(self):
        root = pages.ROOT / 'tools/design'
        canvas = json.loads((root / 'canvas.json').read_text())
        self.assertEqual(canvas['title'], 'Dig It Website')
        self.assertEqual(set(canvas['order']), set(canvas['boards']))
        for file, board in canvas['boards'].items():
            text = (root / file).read_text()
            self.assertIn('<script src="./support.js"></script>', text)
            self.assertIn('class Component extends DCLogic', text)
            self.assertEqual(board['expand'], 'fill')
            self.assertNotIn('data:', text)
        system = pages.ROOT / 'tools/design-system'
        self.assertEqual(json.loads((root / 'ds/digit/tokens.json').read_text()),
                         json.loads((system / 'tokens.json').read_text()))
        self.assertTrue((system / 'README.md').is_file())
        self.assertTrue((system / 'components/Cover/preview.html').is_file())

    def test_semantic_color_contrast(self):
        tokens = json.loads((pages.ROOT / 'tools/design-system/tokens.json').read_text())
        colors = {item['name']: item['value'] for item in tokens['color']['tokens']}

        def luminance(value):
            channels = [int(value[index:index + 2], 16) / 255 for index in (1, 3, 5)]
            channels = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in channels]
            return sum(v * weight for v, weight in zip(channels, (.2126, .7152, .0722)))

        for theme in ('light', 'dark'):
            pairs = [(text, surface) for text in ('text', 'muted', 'primary', 'primary-dark', 'accent')
                     for surface in ('bg', 'surface', 'surface-strong')]
            pairs += [('on-primary', 'primary'), ('on-primary', 'primary-dark')]
            for foreground, background in pairs:
                with self.subTest(theme=theme, pair=(foreground, background)):
                    high, low = sorted([luminance(colors[name][theme]) for name in (foreground, background)], reverse=True)
                    self.assertGreaterEqual((high + .05) / (low + .05), 4.5)

    def test_generation_is_repeatable_and_all_pages_share_shell(self):
        pages.OUTPUTS.clear()
        date = re.search(r'<lastmod>([^<]+)', (pages.ROOT / 'sitemap.xml').read_text())[1]
        pages.build(date)
        for path, value in pages.OUTPUTS.items():
            with self.subTest(path=str(path.relative_to(pages.ROOT))):
                self.assertEqual(path.read_text(), value)
                if path.suffix == '.html':
                    self.assertEqual(value.count('class="skip-link"'), 1)
                    self.assertEqual(value.count('id="main-content"'), 1)
                    self.assertEqual(len(re.findall(r'<link[^>]*rel="stylesheet"', value)), 2)
                    self.assertIn('/style/tokens.css?v=', value)
                    self.assertIn('/style/base.css?v=', value)
        for locale in pages.LOCALES:
            home = pages.local_path(locale).read_text()
            self.assertIn('class="hero-screenshot"', home)
            self.assertIn('fetchpriority="high"', home)
            self.assertNotIn('class="still-grid"', home)
            self.assertIn('https://creativecommons.org/licenses/by/3.0/', home)
            self.assertIn('href="https://apps.apple.com/app/id6508171056"', home)


if __name__ == '__main__':
    unittest.main()
