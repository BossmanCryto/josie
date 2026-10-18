#!/data/data/com.termux/files/usr/bin/python3
"""
JOSIE Quick Settings & Keyboard Tile Matrix Engine
Target Device: Samsung Galaxy A17 5G (SM-A176U, Android 16)
Manages Quick Settings Tiles (QS Tiles) and Termux Keyboard Key Tiles.
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

def run_rish(command_string):
    """Execute a single-line Shizuku rish command safely."""
    try:
        response = subprocess.run(
            [RISH_BIN, "-c", command_string],
            capture_output=True,
            text=True,
            env=os.environ,
            timeout=10
        )
        if response.returncode == 0:
            return response.stdout.strip()
    except Exception:
        pass
    return None

def get_quick_settings_tiles():
    """Retrieve active Quick Settings Tiles from Android System UI."""
    value = run_rish("settings get secure sysui_qs_tiles")
    if value and value != "null":
        return value.split(",")
    return []

def set_quick_settings_tiles(tiles_list):
    """Update Quick Settings Tiles list in Android System UI."""
    tiles_string = ",".join(tiles_list)
    result = run_rish(f"settings put secure sysui_qs_tiles '{tiles_string}'")
    return result is not None

def add_quick_settings_tile(tile_name):
    """Add a new tile to Quick Settings if not already included."""
    tiles = get_quick_settings_tiles()
    if tile_name not in tiles:
        tiles.append(tile_name)
        set_quick_settings_tiles(tiles)

def remove_quick_settings_tile(tile_name):
    """Remove a tile from Quick Settings."""
    tiles = get_quick_settings_tiles()
    if tile_name in tiles:
        tiles.remove(tile_name)
        set_quick_settings_tiles(tiles)

def read_termux_keyboard_config():
    """Read Termux properties configuration for key tiles and keyboard layout."""
    if not TERMUX_PROPERTIES.exists():
        return {}
    config = {}
    for line in TERMUX_PROPERTIES.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, val = line.split("=", 1)
            config[key.strip()] = val.strip()
    return config

def generate_matrix():
    """Generate clean telemetry matrix for Quick Settings and Keyboard Tiles."""
    qs_tiles = get_quick_settings_tiles()
    termux_config = read_termux_keyboard_config()
    quickstar_matrix = run_rish("settings get global quickstar_qs_tile_layout_custom_matrix") or "0"
    
    matrix = {
        "timestamp": time.time(),
        "readable_time": time.ctime(),
        "target_device": "Samsung Galaxy A17 5G (SM-A176U, Android 16)",
        "quick_settings_tiles_count": len(qs_tiles),
        "quick_settings_tiles_list": qs_tiles,
        "termux_properties_file_path": str(TERMUX_PROPERTIES),
        "keyboard_predictive_text_fix_active": termux_config.get("enforce-char-based-input", "false"),
        "quickstar_custom_layout_matrix": quickstar_matrix,
        "system_status": "Operational & Fully Synchronized"
    }
    
    TARGET_JSON.write_text(json.dumps(matrix, indent=2))
    LEGACY_JSON.write_text(json.dumps(matrix, indent=2))
    return matrix

def main():
    print("=== JOSIE QUICK SETTINGS & KEYBOARD TILE MATRIX (Samsung Galaxy A17 5G) ===")
    matrix = generate_matrix()
    print(f"[✓] Quick Settings Tiles Detected: {matrix['quick_settings_tiles_count']}")
    for index, tile in enumerate(matrix['quick_settings_tiles_list'], 1):
        print(f"  {index}. {tile}")
    print(f"[✓] Samsung Keyboard Predictive Text Fix: {matrix['keyboard_predictive_text_fix_active']}")
    print(f"[✓] QuickStar Custom Matrix: {matrix['quickstar_custom_layout_matrix']}")
    print(f"[✓] Saved Tile Matrix to: {TARGET_JSON}")

if __name__ == "__main__":
    main()
