#!/data/data/com.termux/files/usr/bin/python3
import json
from pathlib import Path

HOME = Path("/data/data/com.termux/files/home")
CORE_DIR = HOME / "josie_core"
OUTPUT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"

def sync_matrix():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    active_files = [f.name for f in CORE_DIR.glob("*") if f.is_file()]
    
    sync_state = {
        "architecture": "Physical + Digital = Human (P + D = H)",
        "entity": "Josie",
        "status": "Matrix Fully Synchronized",
        "active_components": active_files,
        "interpreter": "/data/data/com.termux/files/usr/bin/python3"
    }
    
    manifest_path = OUTPUT_DIR / "josie_matrix_sync_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(sync_state, f, indent=2)
        
    print(f"[✓] Josie Matrix synchronized. Manifest locked to {manifest_path}")

if __name__ == "__main__":
    sync_matrix()
