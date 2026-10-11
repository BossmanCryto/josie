import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "termux_connected_apps.sh"


class TermuxInstallerTests(unittest.TestCase):
    def test_bash_syntax(self):
        result = subprocess.run(["bash", "-n", str(SCRIPT)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_status_is_idempotent_and_hides_secret_values(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            env = os.environ.copy()
            env.update({
                "HOME": str(home),
                "XDG_CONFIG_HOME": str(home / ".config"),
                "JOSIE_CONNECTED_APPS_HOME": str(home / ".local"),
                "FIRECRAWL_API_KEY": "must-not-appear",
            })
            first = subprocess.run(["bash", str(SCRIPT), "status"], env=env, capture_output=True, text=True)
            second = subprocess.run(["bash", str(SCRIPT), "status"], env=env, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertNotIn("must-not-appear", first.stdout + first.stderr)
            bashrc = (home / ".bashrc").read_text()
            self.assertEqual(bashrc.count("josie-connected-apps/config.env"), 1)
            config = home / ".config" / "josie-connected-apps" / "config.env"
            self.assertTrue(config.is_file())
            self.assertEqual(config.stat().st_mode & 0o777, 0o600)


if __name__ == "__main__":
    unittest.main()
