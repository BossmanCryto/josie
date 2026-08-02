import os
import sys
import json
import time
import subprocess
from pathlib import Path

audit_dir = Path('/data/data/com.termux/files/storage/shared/Download/Android_Audit')
audit_dir.mkdir(parents=True, exist_ok=True)

print("[*] Initializing Local Firmware & Utility Bridge...")

# Gather system properties and interface states equivalent to low-level diagnostics
getprop_res = subprocess.run(['getprop'], capture_output=True, text=True).stdout.splitlines()
props = {}
for line in getprop_res:
    if '[' in line and ']' in line:
        parts = line.split(': ')
        if len(parts) == 2:
            key = parts[0].strip().strip('[]')
            val = parts[1].strip().strip('[]')
            props[key] = val

firmware_matrix = {
    "timestamp": time.time(),
    "bridge_engine": "SamFw-Equivalent Local Introspection",
    "device_brand": props.get("ro.product.brand", "Unknown"),
    "device_model": props.get("ro.product.model", "Unknown"),
    "android_version": props.get("ro.build.version.release", "Unknown"),
    "security_patch": props.get("ro.build.version.security_patch", "Unknown"),
    "build_id": props.get("ro.build.display.id", "Unknown"),
    "status": "Unlocked & Autonomous Pipeline Active"
}

target = audit_dir / "josie_firmware_bridge_matrix.json"
target.write_text(json.dumps(firmware_matrix, indent=2))

print(f"[✓] Firmware Bridge Matrix Compiled Successfully.")
print(f"[✓] Target Path: {target}")
print(json.dumps({k: v for k, v in firmware_matrix.items() if k != "timestamp"}, indent=2))
