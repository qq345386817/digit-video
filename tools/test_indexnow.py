import contextlib
import io
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

import submit_indexnow as indexnow


class IndexNowTests(unittest.TestCase):
    def test_sitemap_only_contains_current_canonical_html(self):
        urls = indexnow.canonical_urls()
        self.assertEqual(len(urls), 121)
        self.assertIn(indexnow.BASE + "/", urls)
        self.assertIn(indexnow.BASE + "/zh-Hans/", urls)
        self.assertTrue(all(not url.endswith((".md", ".html")) for url in urls))

    def test_public_key_matches_filename(self):
        payload = indexnow.payload_for([indexnow.BASE + "/"])
        self.assertEqual(payload["keyLocation"], indexnow.BASE + "/" + payload["key"] + ".txt")

    def test_foreign_alias_and_nonindexable_urls_are_rejected(self):
        urls = indexnow.canonical_urls()
        for url in ("https://other.example/", indexnow.BASE + "/index.html",
                    indexnow.BASE + "/help.md", indexnow.BASE + "/#app"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                indexnow.select_urls(urls, [url])

    def test_requested_urls_are_deduplicated(self):
        url = indexnow.BASE + "/"
        self.assertEqual(indexnow.select_urls([url], [url, url]), [url])

    def test_git_changes_select_only_published_canonical_html(self):
        urls = indexnow.canonical_urls()
        with patch.object(indexnow.subprocess, "check_output", side_effect=["a" * 40 + "\n", b"index.html\0zh-Hans/help.html\0tools/test_indexnow.py\0"]):
            self.assertEqual(indexnow.select_urls(urls, since="HEAD~1"),
                             [url for url in urls if url in (indexnow.BASE + "/", indexnow.BASE + "/zh-Hans/help")])

    def test_dry_run_never_uses_the_network(self):
        with patch.object(indexnow, "urlopen") as network, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(indexnow.main([]), 0)
        network.assert_not_called()

    def test_failed_key_verification_prevents_submission(self):
        payload = indexnow.payload_for([indexnow.BASE + "/"])
        response = MagicMock(status=200)
        response.geturl.return_value = payload["keyLocation"]
        response.read.return_value = b"<!doctype html>"
        with patch.object(indexnow, "urlopen") as network:
            network.return_value.__enter__.return_value = response
            with self.assertRaises(ValueError):
                indexnow.submit(payload)
            self.assertEqual(network.call_count, 1)

    def test_redirected_key_is_rejected(self):
        payload = indexnow.payload_for([indexnow.BASE + "/"])
        response = MagicMock(status=200)
        response.geturl.return_value = indexnow.BASE + "/"
        response.read.return_value = payload["key"].encode()
        with patch.object(indexnow, "urlopen") as network:
            network.return_value.__enter__.return_value = response
            with self.assertRaises(ValueError):
                indexnow.submit(payload)

    def test_accepted_is_not_indexed_and_posts_json(self):
        payload = indexnow.payload_for([indexnow.BASE + "/"])
        key_response = MagicMock(status=200)
        key_response.geturl.return_value = payload["keyLocation"]
        key_response.read.return_value = payload["key"].encode()
        post_response = MagicMock(status=202)
        post_response.geturl.return_value = indexnow.ENDPOINT
        contexts = [MagicMock(), MagicMock()]
        contexts[0].__enter__.return_value = key_response
        contexts[1].__enter__.return_value = post_response
        with patch.object(indexnow, "urlopen", side_effect=contexts) as network:
            receipt = indexnow.submit(payload)
            request = network.call_args_list[1].args[0]
            self.assertEqual(request.method, "POST")
            self.assertEqual(request.full_url, indexnow.ENDPOINT)
        self.assertEqual(receipt["status"], "accepted_key_validation_pending")
        self.assertEqual(receipt["indexed"], "unknown")

    def test_http_error_is_reported_without_retry(self):
        with patch.object(indexnow, "submit", side_effect=HTTPError(indexnow.ENDPOINT, 429, "Too Many Requests", {}, io.BytesIO(b"rate limited"))), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(indexnow.main(["--submit"]), 1)
        self.assertIn('"httpStatus": 429', output.getvalue())
        self.assertIn('"failedUrl": "' + indexnow.ENDPOINT + '"', output.getvalue())
        self.assertIn("rate limited", output.getvalue())

    def test_empty_git_diff_does_not_submit(self):
        with patch.object(indexnow, "select_urls", return_value=[]), patch.object(indexnow, "urlopen") as network, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(indexnow.main(["--since", "HEAD", "--submit"]), 0)
        network.assert_not_called()

    def test_transport_failure_records_the_phase_and_does_not_retry(self):
        with patch.object(indexnow, "urlopen", side_effect=OSError("connection closed")) as network, contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(indexnow.main(["--submit"]), 1)
        self.assertEqual(network.call_count, 1)
        self.assertIn('"failedStage": "verify_live_key"', output.getvalue())

    def test_direct_mode_only_changes_this_request_opener(self):
        payload = indexnow.payload_for([indexnow.BASE + "/"])
        response = MagicMock(status=200)
        response.geturl.side_effect = [payload["keyLocation"], indexnow.ENDPOINT]
        response.read.return_value = payload["key"].encode()
        with patch.object(indexnow, "build_opener") as factory, patch.object(indexnow, "urlopen") as default:
            factory.return_value.open.return_value.__enter__.return_value = response
            receipt = indexnow.submit(payload, no_proxy=True)
        default.assert_not_called()
        self.assertEqual(factory.call_args.args[0].proxies, {})
        self.assertEqual(receipt["httpStatus"], 200)


if __name__ == "__main__":
    unittest.main()
