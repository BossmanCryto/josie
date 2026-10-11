import os
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "josie_rish_bash_deep_push.py"


class RishBridgeTests(unittest.TestCase):
    def test_installer_is_idempotent(self):
        with TemporaryDirectory() as tmp:
            home = Path(tmp) / "home"
            output = Path(tmp) / "out"
            home.mkdir()
            env = os.environ | {"JOSIE_HOME": str(home), "JOSIE_OUTPUT_DIR": str(output)}
            subprocess.run([sys.executable, str(SCRIPT)], check=True, env=env, capture_output=True, text=True)
            first = (home / ".bashrc").read_text()
            subprocess.run([sys.executable, str(SCRIPT)], check=True, env=env, capture_output=True, text=True)
            second = (home / ".bashrc").read_text()
            self.assertEqual(first, second)
            self.assertEqual(1, second.count("# >>> JOSIE RISH BRIDGE >>>"))
            self.assertNotIn("alias rish=", second)
            self.assertTrue((output / "josie_rish_bash_manifest.json").is_file())


if __name__ == "__main__":
    unittest.main()
