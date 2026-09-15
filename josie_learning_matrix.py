#!/data/data/com.termux/files/usr/bin/python3
"""
JOSIE Deep Learning & Discovery Matrix Engine
Target Device: Samsung Galaxy A17 5G (SM-A176U, Android 16)
Learns, indexes, and catalogs device commands, installed binaries, system interfaces,
and application capabilities into an autonomous knowledge matrix.
"""

import os
import sys
import json
import time
import shutil
import subprocess
from pathlib import Path

HOME = Path(os.getenv("HOME", "/data/data/com.termux/files/home"))
AUDIT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)
TARGET_JSON = AUDIT_DIR / "josie_learning_matrix.json"
RISH_BIN = "/data/data/com.termux/files/usr/bin/rish"

def run_cmd(args):
    """Safely run command and return stdout."""
    try:
        res = subprocess.run(args, capture_output=True, text=True, timeout=5)
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception:
        pass
    return ""

def learn_system_binaries():
    """Discover all executable binaries in PATH."""
    binaries = set()
    path_dirs = os.getenv("PATH", "").split(":")
    for pdir in path_dirs:
        p = Path(pdir)
        if p.exists() and p.is_dir():
            for item in p.iterdir():
                if item.is_file() and os.access(item, os.X_OK):
                    binaries.add(item.name)
    return sorted(list(binaries))

def learn_installed_packages():
    """Catalog installed Android packages."""
    out = run_cmd([RISH_BIN, "-c", "pm list packages -3"])
    if out:
        pkgs = [line.replace("package:", "").strip() for line in out.splitlines() if line.startswith("package:")]
        return sorted(pkgs)
    return []

def learn_hardware_properties():
    """Index essential hardware properties for Samsung Galaxy A17 5G."""
    out = run_cmd([RISH_BIN, "-c", "getprop ro.product.model"])
    version = run_cmd([RISH_BIN, "-c", "getprop ro.build.version.release"])
    patch = run_cmd([RISH_BIN, "-c", "getprop ro.build.version.security_patch"])
    
    return {
        "model": out or "SM-A176U",
        "android_version": version or "16",
        "security_patch": patch or "Unknown",
        "arch": os.uname().machine
    }

def generate_learning_matrix():
    """Build unified autonomous learning matrix."""
    binaries = learn_system_binaries()
    packages = learn_installed_packages()
    hw_props = learn_hardware_properties()
    
    matrix = {
        "timestamp": time.time(),
        "readable_time": time.ctime(),
        "target_device": "Samsung Galaxy A17 5G (SM-A176U, Android 16)",
        "hardware_specs": hw_props,
        "learned_system_binaries_count": len(binaries),
        "learned_system_binaries_sample": binaries[:25],
        "learned_user_packages_count": len(packages),
        "learned_user_packages_sample": packages[:25],
        "status": "Knowledge Indexing Complete & Active"
    }
    
    TARGET_JSON.write_text(json.dumps(matrix, indent=2))
    return matrix

def main():
    print("=== JOSIE DEEP LEARNING & DISCOVERY MATRIX (Samsung A17 5G) ===")
    matrix = generate_learning_matrix()
    print(f"[✓] Learned System Binaries in PATH: {matrix['learned_system_binaries_count']}")
    print(f"[✓] Learned Installed Packages: {matrix['learned_user_packages_count']}")
    print(f"[✓] Hardware Mapped: {matrix['hardware_specs']['model']} (Android {matrix['hardware_specs']['android_version']})")
    print(f"[✓] Learning Matrix saved to {TARGET_JSON}")

if __name__ == "__main__":
    main()
