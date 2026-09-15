#!/data/data/com.termux/files/usr/bin/env python3
import os, time, json, subprocess
from datetime import datetime, timezone

HOME = os.getenv("HOME", "/data/data/com.termux/files/home")
WORKSPACE_DIR = os.path.join(HOME, "josie_core")
AUDIT_DIR = os.path.join(HOME, "storage", "shared", "Download", "Android_Audit")
INBOX_FILE = os.path.join(AUDIT_DIR, "josie_inbox.sh")
OUTBOX_FILE = os.path.join(AUDIT_DIR, "josie_telemetry_out.json")
TICKER_LOG = os.path.join(AUDIT_DIR, "josie_minute_ticker.log")

def log(msg):
    line = f"[{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}] {msg}"
    print(line)
    os.makedirs(AUDIT_DIR, exist_ok=True)
    with open(TICKER_LOG, "a") as f: f.write(line + "\n")

def heartbeat():
    os.makedirs(AUDIT_DIR, exist_ok=True)
    git_status = "Clean"
    try:
        res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=WORKSPACE_DIR, check=False)
        if res.stdout.strip(): git_status = "Modified"
    except Exception: pass

    with open(OUTBOX_FILE, "w") as f:
        json.dump({"timestamp": datetime.now(timezone.utc).isoformat(), "git_status": git_status, "status": "locked"}, f, indent=2)

    if os.path.exists(INBOX_FILE):
        try:
            subprocess.run(["bash", INBOX_FILE], check=False)
            os.remove(INBOX_FILE)
            log("Inbox payload executed.")
        except Exception as e: log(f"Error: {e}")

if __name__ == "__main__":
    os.makedirs(WORKSPACE_DIR, exist_ok=True)
    while True:
        try: heartbeat()
        except Exception as e: log(f"Exception: {e}")
        time.sleep(60)
