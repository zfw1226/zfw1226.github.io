"""Ensure workflow success represents data actually fetched during that run."""
import importlib.util
import io
from contextlib import redirect_stdout
import json
import os
from pathlib import Path
import runpy
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


class SyncMarkerTests(unittest.TestCase):
    def test_crawler_preserves_counts_and_records_run_marker(self):
        # Explicit unit-test fixture, never used as published citation data.
        author = {
            "name": "Unit test fixture", "citedby": 1,
            "publications": [{"author_pub_id": "fixture:paper", "num_citations": 1}],
        }
        fake = types.ModuleType("scholarly")
        fake.scholarly = types.SimpleNamespace(
            search_author_id=lambda _id: author,
            fill=lambda *_args, **_kwargs: None,
            set_logger=lambda *_args: None,
        )
        source = Path(__file__).resolve().parents[1] / "main.py"
        cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as folder:
            try:
                os.chdir(folder)
                with patch.dict(sys.modules, {"scholarly": fake}), patch.dict(
                    os.environ, {"GOOGLE_SCHOLAR_ID": "fixture", "GITHUB_RUN_ID": "123456", "GITHUB_RUN_ATTEMPT": "1"}
                ):
                    with patch("requests.get", return_value=types.SimpleNamespace(
                        status_code=200, text='<table id="gsc_rsb_st"></table>'
                    )), redirect_stdout(io.StringIO()):
                        runpy.run_path(str(source), run_name="__main__")
                data = json.loads(Path("results/gs_data.json").read_text())
                badge = json.loads(Path("results/gs_data_shieldsio.json").read_text())
                self.assertEqual(data["sync_run_id"], "123456")
                self.assertEqual(data["sync_run_attempt"], "1")
                self.assertEqual(data["citedby"], 1)
                self.assertEqual(badge["message"], "1")
                self.assertIn("fixture:paper", data["publications"])
            finally:
                os.chdir(cwd)

    def test_blocked_runner_fails_before_entering_scholarly_retry_loop(self):
        fake = types.ModuleType("scholarly")
        search_calls = []
        fake.scholarly = types.SimpleNamespace(
            search_author_id=lambda _id: search_calls.append(_id),
            set_logger=lambda *_args: None,
        )
        source = Path(__file__).resolve().parents[1] / "main.py"
        cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as folder:
            try:
                os.chdir(folder)
                with patch.dict(sys.modules, {"scholarly": fake}), patch.dict(
                    os.environ, {"GOOGLE_SCHOLAR_ID": "fixture", "GITHUB_RUN_ID": "123456", "GITHUB_RUN_ATTEMPT": "1"}
                ), patch("requests.get", return_value=types.SimpleNamespace(
                    status_code=403, text='Access denied'
                )):
                    with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
                        runpy.run_path(str(source), run_name="__main__")
                self.assertEqual(search_calls, [])
                self.assertFalse(Path("results/gs_data.json").exists())
            finally:
                os.chdir(cwd)

    def test_verifier_rejects_stale_run_or_mismatched_badge(self):
        source = Path(__file__).resolve().parents[1] / "verify_sync.py"
        spec = importlib.util.spec_from_file_location("verify_sync", source)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        data = {"sync_run_id": "123456", "sync_run_attempt": "1", "citedby": 2754}
        module.verify_sync(data, {"message": "2754"}, "123456")
        with self.assertRaises(ValueError):
            module.verify_sync(data, {"message": "2754"}, "another-run")
        with self.assertRaises(ValueError):
            module.verify_sync(data, {"message": "2638"}, "123456")
        # GitHub reruns keep RUN_ID but increment RUN_ATTEMPT; old data is stale.
        with self.assertRaises(ValueError):
            module.verify_sync(data, {"message": "2754"}, "123456", "2")


if __name__ == "__main__":
    unittest.main()
