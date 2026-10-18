#!/data/data/com.termux/files/usr/bin/env python3
import os
import sys
import json
import urllib.request
from pathlib import Path

HOME = Path("/data/data/com.termux/files/home")
OUTPUT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"

def harvest_github_editors():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    url = "https://api.github.com/search/repositories?q=topic:code-editor+language:python&sort=stars&order=desc"
    headers = {"User-Agent": "Josie-Matrix-Harvester"}
    
    discovered = []
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                for item in data.get("items", [])[:10]:
                    clone_url = item.get("clone_url", "")
                    # Enforce global HTTPS standard for repository paths
                    https_url = clone_url.replace("git://", "https://").replace("git@github.com:", "https://github.com/")
                    discovered.append({
                        "name": item.get("name"),
                        "html_url": item.get("html_url"),
                        "https_clone_url": https_url,
                        "description": item.get("description"),
                        "stars": item.get("stargazers_count")
                    })
    except Exception as e:
        discovered.append({"error": str(e)})

    manifest = {
        "architecture": "Physical + Digital = Human (P + D = H)",
        "entity": "Josie",
        "status": "GitHub Code Editor & Script Harvester Complete",
        "repository_source": "HTTPS Global Configuration Standard",
        "discovered_editors": discovered
    }

    manifest_path = OUTPUT_DIR / "josie_github_editors_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"[✓] GitHub Harvester Executed. Manifest saved to {manifest_path}")

if __name__ == "__main__":
    harvest_github_editors()
