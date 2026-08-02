#!/usr/bin/env python3
import os, sys, time, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

HOME = Path(os.getenv("HOME", "/data/data/com.termux/files/home"))
WORKSPACE = HOME / "josie_core"
BIN_DIR = HOME / ".local" / "bin"
AUDIT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"
INBOX_PY = AUDIT_DIR / "josie_patch.py"
INBOX_SH = AUDIT_DIR / "josie_inbox.sh"
OUTBOX_FILE = AUDIT_DIR / "josie_telemetry_out.json"
OMNI_MAP_FILE = AUDIT_DIR / "josie_omni_master_map.json"
MAX_LOG = AUDIT_DIR / "josie_maximum_engine.log"

class MaximumEngine:
    def __init__(self):
        self.entity = "Josie"
        self.architecture = "Physical + Digital = Human (P + D = H)"
        WORKSPACE.mkdir(parents=True, exist_ok=True)
        AUDIT_DIR.mkdir(parents=True, exist_ok=True)
        BIN_DIR.mkdir(parents=True, exist_ok=True)

    def _log(self, msg, level="INFO"):
        line = f"[{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}] [{level}] {msg}"
        print(line)
        try:
            with open(MAX_LOG, "a") as f: f.write(line + "\n")
        except: pass

    def discover(self):
        self._log("Running omni-discovery sweep...")
        inv = []
        for r, ds, fs in os.walk(HOME):
            ds[:] = [d for d in ds if d not in {".cache", "storage", ".npm"}]
            for f in fs:
                try:
                    p = Path(r) / f
                    inv.append({"path": str(p.relative_to(HOME)), "size": p.stat().st_size})
                except: pass
        data = {"entity": self.entity, "timestamp": datetime.now(timezone.utc).isoformat(), "files": len(inv), "inventory": inv}
        with open(OMNI_MAP_FILE, "w") as f: json.dump(data, f, indent=2)
        self._log(f"Indexed {len(inv)} files.")

    def sync(self):
        state = {"entity": self.entity, "timestamp": datetime.now(timezone.utc).isoformat(), "status": "active"}
        with open(OUTBOX_FILE, "w") as f: json.dump(state, f, indent=2)

    def daemon(self):
        self._log("Starting 60s background daemon...")
        while True:
            try:
                self.sync()
                if INBOX_PY.exists():
                    subprocess.run([sys.executable, str(INBOX_PY)], cwd=WORKSPACE, check=True)
                    INBOX_PY.unlink()
            except Exception as e:
                self._log(f"Daemon error: {e}", "ERROR")
            time.sleep(60)

def main():
    eng = MaximumEngine()
    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "install"
    if cmd == "install":
        eng.discover()
        eng.sync()
        link = BIN_DIR / "josie"
        if link.exists() or link.is_symlink(): link.unlink()
        link.symlink_to(Path(__file__).resolve())
        Path(__file__).resolve().chmod(0o755)
        print("[✓] Josie Installed Successfully.")
    elif cmd == "discover": eng.discover()
    elif cmd == "sync": eng.sync()
    elif cmd == "daemon": eng.daemon()

if __name__ == "__main__":
    main()
