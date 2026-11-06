"""Regression checks for public product facts and localized guide coverage."""

import json
import re
import unittest
import xml.etree.ElementTree as ET
from html import escape
from urllib.parse import urlparse

import build_workflow_pages as pages
from check_seo import Page


class ProductContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = json.loads((pages.ROOT / 'tools/workflow-content.json').read_text())

    def test_all_locales_have_translated_product_facts(self):
        self.assertEqual(set(self.content), set(pages.LOCALES))
        keys = set(self.content['en'])
        for locale, content in self.content.items():
            with self.subTest(locale=locale):
                self.assertEqual(set(content), keys)
                for key in ('useTitle', 'useBody', 'coverTitle', 'coverIntro', 'stepsGuideTitle',
                            'stepsGuideIntro', 'exportQuestion', 'exportAnswer', 'availability'):
                    self.assertTrue(content[key].strip())
                    if locale != 'en':
                        self.assertNotEqual(content[key], self.content['en'][key])
                for value in ('PNG', 'JPEG', 'PDF', '40', '120', 'Mac', 'JSON'):
                    self.assertIn(value, content['exportAnswer'])
                self.assertIn('1.4.3', content['availability'])

    def test_home_and_help_link_to_all_workflows(self):
        for locale, content in self.content.items():
            for page in ('index', 'help'):
                html = pages.local_path(locale, page).read_text()
                with self.subTest(locale=locale, page=page):
                    for kind in (pages.BATCH, pages.CONTACT, pages.COVER, pages.STEPS):
                        self.assertIn('href="' + urlparse(pages.url(locale, kind)).path + '"', html)
                    self.assertIn(content['exportQuestion'], html)
                    self.assertIn(escape(content['exportAnswer']), html)
            self.assertIn('id="use-cases"', pages.local_path(locale).read_text())

    def test_guide_descriptions_and_markdown_match_html(self):
        for locale, content in self.content.items():
            for kind, prefix in ((pages.COVER, 'cover'), (pages.STEPS, 'stepsGuide')):
                html = pages.local_path(locale, kind).read_text()
                with self.subTest(locale=locale, kind=kind):
                    page = Page()
                    page.path = pages.local_path(locale, kind)
                    page.feed(html)
                    self.assertEqual(page.description, content[prefix + 'Intro'])
                    self.assertEqual(page.h1, 1)
                    self.assertIn('id="export-formats"', html)
                    self.assertIn('<p class="article-meta">' + escape(content['guideLabel']) + '</p>', html)
                    self.assertEqual(pages.local_path(locale, kind, '.md').read_text(),
                                     pages.Markdown().render(html, pages.url(locale, kind)))
                    self.assertIn('type="text/markdown"', html)

    def test_chinese_product_names_do_not_rename_app_menus(self):
        for locale, product_name, menu in (
            ('zh-Hans', 'PDF 缩略图索引页', '导出 → PDF 联系表'),
            ('zh-Hant', 'PDF 縮圖總覽', '匯出 → PDF 聯絡表'),
        ):
            content = self.content[locale]
            self.assertIn(product_name, content['deliveryTitle'])
            self.assertIn(product_name, content['homeDescription'])
            self.assertIn(menu, content['deliveryBody'])
        self.assertIn('コンタクトシート', self.content['ja']['contactTitle'])

    def test_llms_uses_labeled_facts_and_existing_public_guides(self):
        text = (pages.ROOT / 'llms.txt').read_text()
        for heading in ('Platform support', 'Image formats and overview limits', 'Source resolution',
                        'Saved projects', 'Local video processing', 'Separate CLI and automation'):
            self.assertIn('## ' + heading, text)
        for key in ('exportAnswer', 'useBody', 'cliStatus'):
            self.assertIn(self.content['en'][key], text)
        for kind in (pages.COVER, pages.STEPS):
            self.assertIn(pages.url('en', kind + '.md'), text)
        self.assertIn('MCP integration is not provided.', text)
        self.assertNotIn('If the update is not available', text)

    def test_app_identity_and_existing_canonical_paths_are_preserved(self):
        ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        sitemap = ET.parse(pages.ROOT / 'sitemap.xml')
        locations = [n.text for n in sitemap.findall('.//s:loc', ns)]
        self.assertEqual(len(locations), 109)
        for locale, content in self.content.items():
            for kind in ('', 'help', pages.BATCH, pages.CONTACT, pages.COVER, pages.STEPS):
                self.assertIn(pages.url(locale, kind), locations)
            html = pages.local_path(locale).read_text()
            nodes = json.loads(pages.SCHEMA_RE.search(html)[1])
            app = next(node for node in nodes if node.get('@type') == 'SoftwareApplication')
            self.assertEqual(app['downloadUrl'], pages.STORE)
            self.assertEqual(app['description'], content['homeDescription'])
            self.assertIn('DigIt', app['alternateName'])
            self.assertFalse(re.search(r'<meta\b[^>]*name="keywords"', html))


if __name__ == '__main__':
    unittest.main()
