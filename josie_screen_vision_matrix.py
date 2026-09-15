#!/data/data/com.termux/files/usr/bin/python3
"""
JOSIE Screen Vision & Multimodal UI Matrix Engine ("JOSIE Eyes")
Target Device: Samsung Galaxy A17 5G (SM-A176U, Android 16)
Inspects live screen windows, focused application activities, display bounds,
screen resolution, density, and UI layout states.
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
TARGET_JSON = AUDIT_DIR / "josie_screen_vision_matrix.json"
RISH_BIN = "/data/data/com.termux/files/usr/bin/rish"

def run_rish(command_string):
    """Execute a single-line Shizuku rish command safely."""
    try:
        response = subprocess.run(
            [RISH_BIN, "-c", command_string],
            capture_output=True,
            text=True,
            env=os.environ,
            timeout=8
        )
        if response.returncode == 0:
            return response.stdout.strip()
    except Exception:
        pass
    return None

def get_screen_dimensions():
    """Retrieve physical screen size and density."""
    size_raw = run_rish("wm size") or "Physical size: Unknown"
    density_raw = run_rish("wm density") or "Physical density: Unknown"
    return {
        "display_size": size_raw.replace("Physical size: ", "").strip(),
        "display_density": density_raw.replace("Physical density: ", "").strip()
    }

def get_focused_screen_activity():
    """Inspect top focused window and application activity."""
    top_raw = run_rish("dumpsys activity top | grep -m 1 'ACTIVITY'") or ""
    focused_raw = run_rish("dumpsys window | grep -m 1 'mCurrentFocus'") or ""
    
    activity_name = "Unknown"
    if "ACTIVITY" in top_raw:
        activity_name = top_raw.strip().split()[-2] if len(top_raw.strip().split()) >= 2 else top_raw.strip()
        
    focused_window = "Unknown"
    if "mCurrentFocus" in focused_raw:
        parts = focused_raw.split("mCurrentFocus=")
        if len(parts) > 1:
            focused_window = parts[1].strip().strip("{}")
            
    return {
        "focused_activity": activity_name,
        "focused_window": focused_window,
        "raw_focus_string": focused_raw
    }

def get_display_orientation_and_mode():
    """Inspect screen orientation and refresh rate parameters."""
    display_info = run_rish("dumpsys window displays | grep -E 'mDisplayId|init=|mCurrentOrientation'") or ""
    orientation = "0 (Portrait)"
    if "mCurrentOrientation=1" in display_info:
        orientation = "1 (Landscape)"
    elif "mCurrentOrientation=2" in display_info:
        orientation = "2 (Reverse Portrait)"
    elif "mCurrentOrientation=3" in display_info:
        orientation = "3 (Reverse Landscape)"
        
    return {
        "screen_orientation": orientation,
        "display_info_summary": display_info.splitlines()[:5] if display_info else []
    }

def generate_matrix():
    """Compile clean screen vision telemetry matrix."""
    dims = get_screen_dimensions()
    focus = get_focused_screen_activity()
    orientation_data = get_display_orientation_and_mode()
    
    matrix = {
        "timestamp": time.time(),
        "readable_time": time.ctime(),
        "target_device": "Samsung Galaxy A17 5G (SM-A176U, Android 16)",
        "vision_engine": "JOSIE Screen Vision Matrix (Multimodal Eyes)",
        "screen_dimensions": dims,
        "screen_focused_state": focus,
        "screen_orientation_state": orientation_data,
        "system_status": "Screen Visual Telemetry Active & Mapped"
    }
    TARGET_JSON.write_text(json.dumps(matrix, indent=2))
    return matrix

def main():
    print("=== JOSIE SCREEN VISION & MULTIMODAL UI MATRIX (Samsung Galaxy A17 5G) ===")
    matrix = generate_matrix()
    print(f"[✓] Screen Resolution: {matrix['screen_dimensions']['display_size']}")
    print(f"[✓] Screen Density: {matrix['screen_dimensions']['display_density']}")
    print(f"[✓] Focused Screen Window: {matrix['screen_focused_state']['focused_window']}")
    print(f"[✓] Screen Orientation: {matrix['screen_orientation_state']['screen_orientation']}")
    print(f"[✓] Saved Screen Vision Matrix to: {TARGET_JSON}")

if __name__ == "__main__":
    main()
