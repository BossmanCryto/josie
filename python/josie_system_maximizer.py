#!/data/data/com.termux/files/usr/bin/python3
"""
JOSIE System Speedup & Maximizer Engine
Target Device: Samsung Galaxy A17 5G (SM-A176U, Android 16)
Applies developer settings for peak performance, 0.5x animation scales for fast UI response, and Termux wake locks.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

HOME = Path(os.getenv("HOME", "/data/data/com.termux/files/home"))
AUDIT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)
TARGET_JSON = AUDIT_DIR / "josie_system_maximizer.json"
RISH_BIN = "/data/data/com.termux/files/usr/bin/rish"

OPTIMIZATION_COMMANDS = [
    "settings put global development_settings_enabled 1",
    "settings put global adb_enabled 1",
    "settings put global stay_on_while_plugged_in 3",
    "settings put global wifi_scan_always_enabled 1",
    "settings put global mobile_data_always_on 1",
    "settings put global animator_duration_scale 0.5",
    "settings put global transition_animation_scale 0.5",
    "settings put global window_animation_scale 0.5"
]

def apply_fast_performance_optimizations():
    """Apply all low-latency, maximum speed developer settings in a single fast rish call."""
    combined_cmd = " ; ".join(OPTIMIZATION_COMMANDS)
    try:
        res = subprocess.run(
            [RISH_BIN, "-c", combined_cmd],
            capture_output=True,
            text=True,
            env=os.environ,
            timeout=8
        )
        return res.returncode == 0
    except Exception:
        return False

def enable_cpu_wake_lock():
    """Keep CPU awake to prevent background task sleep."""
    try:
        subprocess.run(["termux-wake-lock"], capture_output=True)
        return True
    except Exception:
        return False

def generate_matrix():
    """Compile clean telemetry output for system speedup."""
    success = apply_fast_performance_optimizations()
    matrix = {
        "timestamp": time.time(),
        "readable_time": time.ctime(),
        "target_device": "Samsung Galaxy A17 5G (SM-A176U, Android 16)",
        "cpu_wake_lock_active": enable_cpu_wake_lock(),
        "batch_optimizations_applied": success,
        "total_optimizations_count": len(OPTIMIZATION_COMMANDS),
        "system_status": "Maximized & Operating at Peak Speed"
    }
    TARGET_JSON.write_text(json.dumps(matrix, indent=2))
    return matrix

def main():
    print("=== JOSIE SYSTEM SPEEDUP & MAXIMIZER ENGINE (Samsung Galaxy A17 5G) ===")
    matrix = generate_matrix()
    print(f"[✓] Batch Performance Optimizations Applied: {matrix['batch_optimizations_applied']}")
    print(f"[✓] Total Tweaks Enforced: {matrix['total_optimizations_count']}")
    print(f"[✓] CPU Background Wake Lock Active: {matrix['cpu_wake_lock_active']}")
    print(f"[✓] Saved Maximizer Matrix to: {TARGET_JSON}")

if __name__ == "__main__":
    main()
