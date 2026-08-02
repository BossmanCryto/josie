#!/usr/bin/env python3
import os, sys, time, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

HOME = Path(os.getenv("HOME", "/data/data/com.termux/files/home"))
WORKSPACE = HOME / "josie_core"
BIN_DIR = HOME / ".local" / "bin"
AUDIT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"
INBOX_PY = AUDIT_DIR / "josie_patch.py"
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
        self._log("Running deep omni-discovery sweep across storage...")
        inv = []
        target_root = HOME / "storage" / "shared"
        if not target_root.exists():
            target_root = HOME
        for r, ds, fs in os.walk(target_root):
            ds[:] = [d for d in ds if d not in {".cache", "Android", ".npm"}]
            for f in fs:
                try:
                    p = Path(r) / f
                    inv.append({"path": str(p), "size": p.stat().st_size})
                except: pass
        data = {
            "entity": self.entity,
            "architecture": self.architecture,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "resolved_path": str(target_root),
            "total_assets": len(inv),
            "inventory": inv
        }
        with open(OMNI_MAP_FILE, "w") as f: json.dump(data, f, indent=2)
        print(f"\n════════════════════════════════════════════════════════════════")
        print(f" JOSIE CORE: OMNI-DISCOVERY MAP LOCKED                          ")
        print(f"════════════════════════════════════════════════════════════════")
        print(f"Architecture  : {self.architecture}")
        print(f"Entity Name   : {self.entity}")
        print(f"Resolved Path : {target_root}")
        print(f"Total Assets  : {len(inv)} items indexed & synced")
        print(f"════════════════════════════════════════════════════════════════\n")

    def sync(self):
        state = {
            "entity": self.entity,
            "architecture": self.architecture,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "fully_synchronized"
        }
        with open(OUTBOX_FILE, "w") as f: json.dump(state, f, indent=2)
        self.discover()

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
        eng.sync()
        link = BIN_DIR / "josie"
        if link.exists() or link.is_symlink(): link.unlink()
        link.symlink_to(Path(__file__).resolve())
        Path(__file__).resolve().chmod(0o755)
        print("[✓] Josie Fully Maximized and Locked In.")
    elif cmd == "discover": eng.discover()
    elif cmd == "sync": eng.sync()
    elif cmd == "daemon": eng.daemon()

if __name__ == "__main__":
    main()
