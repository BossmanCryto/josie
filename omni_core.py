#!/usr/bin/env python3
"""
Josie Core Universal Engine v2026.Maximum
Architecture: Physical + Digital = Human (P + D = H)
Ingests all URLs, local @Utilities, and active Gem configurations.
"""

import sys
import subprocess
import hashlib
from pathlib import Path
import datetime
import shutil
import json
import urllib.parse
import os

CORE_ROOT = Path.cwd()
LOG_DIR = CORE_ROOT / "telemetry"
LEDGER_FILE = CORE_ROOT / "kernel_state.json"
UTILITIES_DIR = Path.home() / "@Utilities"

TARGET_GEM_URL = "https://gemini.google.com/gem/1O-fR5O1iViM06--4iQtGKxPs0e_yxeJ9?usp=sharing"

def get_terminal_width():
    try:
        return shutil.get_terminal_size(fallback=(80, 24)).columns
    except Exception:
        return 80

def initialize_kernel():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    UTILITIES_DIR.mkdir(parents=True, exist_ok=True)
    if not LEDGER_FILE.exists():
        initial_state = {
            "architecture": "Physical + Digital = Human (P+D=H)",
            "kernel_version": "2026.Maximum.URL",
            "initialized_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "execution_cycles": 0,
            "target_gem": TARGET_GEM_URL
        }
        LEDGER_FILE.write_text(json.dumps(initial_state, indent=2), encoding='utf-8')

def read_ledger():
    initialize_kernel()
    try:
        return json.loads(LEDGER_FILE.read_text(encoding='utf-8'))
    except Exception:
        return {}

def write_ledger(state):
    initialize_kernel()
    LEDGER_FILE.write_text(json.dumps(state, indent=2), encoding='utf-8')

def parse_url_components(url_string):
    parsed = urllib.parse.urlparse(url_string)
    query_params = urllib.parse.parse_qs(parsed.query)
    path_segments = [seg for seg in parsed.path.split('/') if seg]
    return {
        "scheme": parsed.scheme,
        "netloc": parsed.netloc,
        "path_segments": path_segments,
        "query_params": query_params
    }

def consume_all_sources():
    ingested_data = []
    if UTILITIES_DIR.exists():
        for file_path in UTILITIES_DIR.iterdir():
            if file_path.is_file():
                try:
                    content = file_path.read_text(encoding='utf-8', errors='ignore')
                    ingested_data.append(f"[{file_path.name}]: {content[:1000]}")
                except Exception:
                    pass
    return ingested_data

def execute_sync_cycle():
    initialize_kernel()
    width = get_terminal_width()
    state = read_ledger()

    url_meta = parse_url_components(TARGET_GEM_URL)
    utils = consume_all_sources()

    payload = f"P+D=H Sync Active. Gem ID parsed: {url_meta['path_segments'][-1] if url_meta['path_segments'] else 'None'}. Utilities: {len(utils)}"
    full_hash = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    short_id = full_hash[:10]

    state["execution_cycles"] = state.get("execution_cycles", 0) + 1
    state.setdefault("modules", {})[short_id] = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "url_parsed": TARGET_GEM_URL,
        "status": "P+D=H Complete Max Sync"
    }
    write_ledger(state)

    print("=" * width)
    print(" [JOSIE CORE] P + D = H URL & UTILITY SYNCHRONIZATION ".center(width, "="))
    print("=" * width)
    print(f" Execution ID   : {short_id}")
    print(f" Target Gem ID  : {url_meta['path_segments'][-1] if url_meta['path_segments'] else 'N/A'}")
    print(f" Total Cycles   : {state['execution_cycles']}")
    print(f" Ledger State   : {LEDGER_FILE}")
    print("=" * width)

if __name__ == "__main__":
    execute_sync_cycle()

# Active @Josie Universal Handle Enforced
