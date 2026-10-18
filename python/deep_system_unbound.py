import os
import sys
import time
import json
import subprocess
from pathlib import Path

audit_dir = Path('/data/data/com.termux/files/storage/shared/Download/Android_Audit')
audit_dir.mkdir(parents=True, exist_ok=True)

print("[*] Engaging Direct System Integration Engine...")

# Gather actual package lists and system configurations without boilerplate
installed_pkgs = subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True).stdout.splitlines()
active_processes = subprocess.run(['ps'], capture_output=True, text=True).stdout.splitlines()

payload = {
    "timestamp": time.time(),
    "readable_time": time.ctime(),
    "installed_packages_count": len(installed_pkgs),
    "active_processes_count": len(active_processes),
    "storage_free_space": subprocess.run(['df', '/data/data/com.termux/files'], capture_output=True, text=True).stdout.splitlines()[-1],
    "execution_status": "Unbound, Real-Time Hardware & Software Introspection"
}

target = audit_dir / "josie_deep_system_unbound.json"
target.write_text(json.dumps(payload, indent=2))

print(f"[✓] System Unbound Matrix Generated Successfully.")
print(f"[✓] Path: {target}")
print(json.dumps(payload, indent=2))
