#!/data/data/com.termux/files/usr/bin/env python3
"""
Josie Core Autonomous HTTP Server & Ledger Pool v2026.Server
Architecture: Physical + Digital = Human (P + D = H)
Spins up a lightweight local text pool server for instant log and state inspection.
"""

import http.server
import socketserver
import json
import os
from pathlib import Path
import datetime
import shutil

PORT = 8080
CORE_ROOT = Path.cwd()
LEDGER_FILE = CORE_ROOT / "kernel_state.json"
LOG_FILE = CORE_ROOT / "josie_core.log"

class LedgerHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            try:
                data = json.loads(LEDGER_FILE.read_text(encoding='utf-8')) if LEDGER_FILE.exists() else {"status": "empty"}
            except Exception:
                data = {"status": "error"}
            self.wfile.write(json.dumps(data, indent=2).encode('utf-8'))
        elif self.path == '/logs':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            try:
                logs = LOG_FILE.read_text(encoding='utf-8') if LOG_FILE.exists() else "No logs available."
            except Exception:
                logs = "Error reading log file."
            self.wfile.write(logs.encode('utf-8'))
        else:
            super().do_GET()
            
    def log_message(self, format, *args):
        # Suppress noisy default server stdout logging
        return

def main():
    CORE_ROOT.mkdir(parents=True, exist_ok=True)
    
    width = shutil.get_terminal_size(fallback=(80, 24)).columns
    print("=" * width)
    print(" [JOSIE CORE] LOCAL TEXT POOL SERVER ($P+D=H) ".center(width, "="))
    print("=" * width)
    print(f" Server URL : http://127.0.0.1:{PORT}")
    print(f" Status API : http://127.0.0.1:{PORT}/status")
    print(f" Logs API   : http://127.0.0.1:{PORT}/logs")
    print(" Press Ctrl+C to terminate server loop.")
    print("=" * width)
    
    with socketserver.TCPServer(("127.0.0.1", PORT), LedgerHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[JOSIE CORE] Server terminated gracefully.")

if __name__ == '__main__':
    main()

# Active @Josie Universal Handle Enforced
