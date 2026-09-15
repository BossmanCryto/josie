import os
import sys
import time
import json
import subprocess
from pathlib import Path

audit_dir = Path('/data/data/com.termux/files/storage/shared/Download/Android_Audit')
audit_dir.mkdir(parents=True, exist_ok=True)

print("[*] Initializing Active Pulse Engine & Live Diagnostics...")

# 1. Gather dynamic environment intelligence
env_data = dict(os.environ)
uptime_res = subprocess.run(['uptime'], capture_output=True, text=True).stdout.strip()
df_res = subprocess.run(['df', '-h', '/data/data/com.termux/files'], capture_output=True, text=True).stdout.strip()

pulse_matrix = {
    "timestamp": time.time(),
    "readable_time": time.ctime(),
    "engine_status": "Active, Real-Time, Self-Sustaining",
    "uptime": uptime_res,
    "storage_allocation": df_res,
    "active_directory": str(Path.cwd()),
    "environment_keys_count": len(env_data)
}

# 2. Write live pulse matrix
target = audit_dir / "josie_active_pulse_matrix.json"
target.write_text(json.dumps(pulse_matrix, indent=2))

print(f"[✓] Active Pulse Matrix compiled successfully.")
print(f"[✓] Target Output: {target}")
print(json.dumps(pulse_matrix, indent=2))
