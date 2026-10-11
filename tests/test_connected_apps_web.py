import json
import os
import sys
import threading
import unittest
from pathlib import Path
from urllib.request import urlopen
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import connected_apps_web as app
from http.server import ThreadingHTTPServer


class DashboardTests(unittest.TestCase):
    def test_status_does_not_expose_secret(self):
        with patch.dict(os.environ, {"GITHUB_TOKEN": "do-not-return-this"}, clear=True):
            payload = json.dumps(app.get_app_statuses())
            self.assertIn('"github"', payload)
            self.assertIn('"configured"', payload)
            self.assertNotIn("do-not-return-this", payload)

    def test_http_endpoints(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            base = f"http://127.0.0.1:{server.server_port}"
            with urlopen(base + "/health") as response:
                health = json.load(response)
            with urlopen(base + "/api/apps") as response:
                apps = json.load(response)
            self.assertTrue(health["ok"])
            self.assertEqual(9, apps["total"])
            self.assertEqual(9, len(apps["apps"]))
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)


if __name__ == "__main__":
    unittest.main()
