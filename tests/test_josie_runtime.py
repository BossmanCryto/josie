import json
import os
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

import josie_runtime as runtime


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.state = Path(self.tmp.name) / "state.json"
        self.state_patch = patch.object(runtime, "STATE_FILE", self.state)
        self.state_patch.start()

    def tearDown(self):
        self.state_patch.stop()
        self.tmp.cleanup()

    def test_env_file_is_data_not_shell(self):
        path = Path(self.tmp.name) / "config.env"
        path.write_text("SAFE='hello world'\nBAD-KEY=value\nRUN=$(touch /tmp/never)\n")
        with patch.dict(os.environ, {}, clear=True):
            runtime.load_env_file(path)
            self.assertEqual("hello world", os.environ["SAFE"])
            self.assertNotIn("BAD-KEY", os.environ)

    def test_cascade_skips_open_circuit(self):
        calls = []
        def bad(prompt, model):
            calls.append("bad")
            raise runtime.ProviderError("limited", 60)
        def good(prompt, model):
            calls.append("good")
            return "answer"
        with patch.dict(runtime.PROVIDERS, {"bad": bad, "good": good}, clear=True), patch.dict(
            os.environ, {"JOSIE_PROVIDER_ORDER": "bad,good"}, clear=False
        ):
            self.assertEqual(("answer", "good"), runtime.ask("hello"))
            self.assertEqual(["bad", "good"], calls)
            calls.clear()
            self.assertEqual(("answer", "good"), runtime.ask("again"))
            self.assertEqual(["good"], calls)

    def test_state_file_is_private(self):
        runtime.record_failure("test", runtime.ProviderError("x", 10))
        self.assertEqual(0o600, self.state.stat().st_mode & 0o777)
        self.assertIn("test", json.loads(self.state.read_text()))

    def test_no_provider_error_is_actionable(self):
        def bad(prompt, model):
            raise runtime.ProviderError("offline")
        with patch.dict(runtime.PROVIDERS, {"bad": bad}, clear=True), patch.dict(
            os.environ, {"JOSIE_PROVIDER_ORDER": "bad"}, clear=False
        ):
            with self.assertRaisesRegex(runtime.ProviderError, "bad: offline"):
                runtime.ask("hello")


if __name__ == "__main__":
    unittest.main()
