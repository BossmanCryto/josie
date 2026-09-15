#!/data/data/com.termux/files/usr/bin/python3
"""
JOSIE Quick Settings & Keyboard Tile Matrix Engine
Target Device: Samsung Galaxy A17 5G (SM-A176U, Android 16)
Provides deep introspection, dynamic reconfiguration, and autonomous management
strictly for Android Quick Settings (QS) Tiles and Termux Key/Word Tiles.
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
TARGET_JSON = AUDIT_DIR / "josie_qs_tile_matrix.json"
LEGACY_JSON = AUDIT_DIR / "josie_wordtile_matrix.json"
TERMUX_PROPERTIES = HOME / ".termux" / "termux.properties"
RISH_BIN = "/data/data/com.termux/files/usr/bin/rish"

def run_rish(cmd):
    """Execute a single-line rish command safely."""
    try:
        res = subprocess.run(
            [RISH_BIN, "-c", cmd],
            capture_output=True,
            text=True,
            env=os.environ,
            timeout=10
        )
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception:
        pass
    return None

def get_qs_tiles():
    """Retrieve active sysui_qs_tiles setting from Android System UI."""
    val = run_rish("settings get secure sysui_qs_tiles")
    if val and val != "null":
        return val.split(",")
    return []

def set_qs_tiles(tiles_list):
    """Update sysui_qs_tiles setting in Android System UI."""
    tiles_str = ",".join(tiles_list)
    res = run_rish(f"settings put secure sysui_qs_tiles '{tiles_str}'")
    return res is not None

def add_qs_tile(tile_name):
    """Add a custom tile to Quick Settings if not already present."""
    tiles = get_qs_tiles()
    if tile_name not in tiles:
        tiles.append(tile_name)
        set_qs_tiles(tiles)

def remove_qs_tile(tile_name):
    """Remove a custom tile from Quick Settings."""
    tiles = get_qs_tiles()
    if tile_name in tiles:
        tiles.remove(tile_name)
        set_qs_tiles(tiles)

def read_termux_tile_config():
    """Read Termux properties configuration for key & word prediction tiles."""
    if not TERMUX_PROPERTIES.exists():
        return {}
    config = {}
    for line in TERMUX_PROPERTIES.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            config[k.strip()] = v.strip()
    return config

def generate_matrix():
    """Generate complete telemetry matrix strictly for Quick Settings & Keyboard Tiles."""
    qs_tiles = get_qs_tiles()
    termux_cfg = read_termux_tile_config()
    quickstar_matrix = run_rish("settings get global quickstar_qs_tile_layout_custom_matrix") or "0"
    
    matrix = {
        "timestamp": time.time(),
        "readable_time": time.ctime(),
        "target_device": "Samsung Galaxy A17 5G (SM-A176U, Android 16)",
        "qs_tiles_count": len(qs_tiles),
        "qs_tiles": qs_tiles,
        "termux_properties_path": str(TERMUX_PROPERTIES),
        "termux_word_input_fixed": termux_cfg.get("enforce-char-based-input", "false"),
        "quickstar_custom_matrix": quickstar_matrix,
        "status": "Operational & Synchronized"
    }
    
    TARGET_JSON.write_text(json.dumps(matrix, indent=2))
    LEGACY_JSON.write_text(json.dumps(matrix, indent=2))
    return matrix

def main():
    print("=== JOSIE QUICK SETTINGS & KEYBOARD TILE MATRIX (Samsung A17 5G) ===")
    matrix = generate_matrix()
    print(f"[✓] Quick Settings Tiles Detected: {matrix['qs_tiles_count']}")
    for idx, tile in enumerate(matrix['qs_tiles'], 1):
        print(f"  {idx}. {tile}")
    print(f"[✓] Termux Char-based Input Fix: {matrix['termux_word_input_fixed']}")
    print(f"[✓] QuickStar Custom Matrix: {matrix['quickstar_custom_matrix']}")
    print(f"[✓] Matrix state saved to {TARGET_JSON}")

if __name__ == "__main__":
    main()
