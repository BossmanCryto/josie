#!/data/data/com.termux/files/usr/bin/python3
"""
JST Global Repository & Intelligence Harvester Engine
Target Device: Samsung Galaxy A17 5G (SM-A176U, Android 16)
Surveys, indexes, and catalogs all local repositories from Cryptoboyyyy_backup,
intelligence_repos, and JST workspaces under Josie's autonomous agent framework.
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

HOME = Path(os.getenv("HOME", "/data/data/com.termux/files/home"))
JST_DIR = HOME / "JOSIE_PROJECTS" / "jst"
AUDIT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)
TARGET_JSON = AUDIT_DIR / "jst_global_harvester_matrix.json"

SEARCH_LOCATIONS = [
    HOME / "JOSIE_PROJECTS",
    HOME / "Cryptoboyyyy_backup",
    HOME / "intelligence_repos",
    HOME / "josie_core",
    HOME / "josie_data",
    HOME / "scripts"
]

def run_cmd(args_list, cwd=None):
    """Safely run command and return output."""
    try:
        res = subprocess.run(args_list, capture_output=True, text=True, cwd=cwd, timeout=5)
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception:
        pass
    return ""

def scan_repositories():
    """Discover all git repositories and asset folders across user workspaces."""
    discovered_repos = []
    
    for base_loc in SEARCH_LOCATIONS:
        if not base_loc.exists():
            continue
            
        if (base_loc / ".git").exists():
            remote = run_cmd(["git", "-C", str(base_loc), "remote", "get-url", "origin"])
            last_commit = run_cmd(["git", "-C", str(base_loc), "log", "-n", "1", "--oneline"])
            discovered_repos.append({
                "repo_name": base_loc.name,
                "path": str(base_loc),
                "is_git_repo": True,
                "git_remote": remote or "local_only",
                "last_commit": last_commit or "none"
            })
        else:
            for item in base_loc.iterdir():
                if item.is_dir():
                    is_git = (item / ".git").exists()
                    remote = run_cmd(["git", "-C", str(item), "remote", "get-url", "origin"]) if is_git else ""
                    last_commit = run_cmd(["git", "-C", str(item), "log", "-n", "1", "--oneline"]) if is_git else ""
                    discovered_repos.append({
                        "repo_name": item.name,
                        "path": str(item),
                        "is_git_repo": is_git,
                        "git_remote": remote or "none",
                        "last_commit": last_commit or "none"
                    })
                    
    return discovered_repos

def check_crypto_assets():
    """Check presence of crypto asset telemetry files."""
    crypto_file = HOME / "crypto_found.txt"
    if crypto_file.exists():
        try:
            return {
                "file_path": str(crypto_file),
                "content_summary": crypto_file.read_text().strip()[:200],
                "size_bytes": crypto_file.stat().st_size
            }
        except Exception as e:
            return {"file_path": str(crypto_file), "error": str(e)}
    return {"file_path": str(crypto_file), "status": "not_present"}

def generate_matrix():
    """Compile global repository & intelligence telemetry matrix."""
    repos = scan_repositories()
    crypto_data = check_crypto_assets()
    
    matrix = {
        "timestamp": time.time(),
        "readable_time": time.ctime(),
        "target_device": "Samsung Galaxy A17 5G (SM-A176U, Android 16)",
        "entity": "Josie Autonomous Intelligence Agent Ecosystem",
        "primary_workspace": str(JST_DIR),
        "total_repositories_scanned": len(repos),
        "git_repositories_count": sum(1 for r in repos if r['is_git_repo']),
        "discovered_repositories": repos,
        "crypto_asset_telemetry": crypto_data,
        "system_status": "All User Repositories & Intelligence Assets Indexed"
    }
    TARGET_JSON.write_text(json.dumps(matrix, indent=2))
    return matrix

def main():
    print("=== JST GLOBAL REPOSITORY & INTELLIGENCE HARVESTER (Samsung Galaxy A17 5G) ===")
    matrix = generate_matrix()
    print(f"[✓] Total Repositories & Folders Scanned: {matrix['total_repositories_scanned']}")
    print(f"[✓] Valid Git Repositories Discovered: {matrix['git_repositories_count']}")
    print(f"[✓] Crypto Asset Telemetry: {matrix['crypto_asset_telemetry'].get('file_path', 'N/A')}")
    print(f"[✓] Saved Global Harvester Matrix to: {TARGET_JSON}")

if __name__ == "__main__":
    main()
