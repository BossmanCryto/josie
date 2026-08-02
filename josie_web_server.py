#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import sys
import subprocess
from pathlib import Path

PORT = 8080
PID_FILE = Path("/data/data/com.termux/files/home/josie_core/josie_web_server.pid")

def kill_stale_port():
    try:
        res = subprocess.run(["fuser", "-k", f"{PORT}/tcp"], capture_output=True, text=True)
    except Exception:
        pass

def daemonize():
    if "--foreground" in sys.argv:
        return
    kill_stale_port()
    try:
        pid = os.fork()
        if pid > 0:
            print(f"[✓] Josie Web Server active on http://localhost:{PORT} (PID: {pid})")
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork #1 failed: {e}\n")
        sys.exit(1)

    os.setsid()
    os.umask(0)

    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as e:
        sys.stderr.write(f"Fork #2 failed: {e}\n")
        sys.exit(1)

    sys.stdout.flush()
    sys.stderr.flush()
    PID_FILE.write_text(str(os.getpid()))

class JosieWebHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "entity": "Josie",
                "architecture": "Physical + Digital = Human (P + D = H)",
                "status": "fully_maximized",
                "platform": "Autonomous Termux HTTP Bridge"
            }
            self.wfile.write(json.dumps(data, indent=2).encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Josie Center Hub</title>
                <style>
                    body { background: #0f172a; color: #38bdf8; font-family: monospace; padding: 40px; }
                    h1 { border-bottom: 2px solid #38bdf8; padding-bottom: 10px; }
                    .card { background: #1e293b; padding: 20px; border-radius: 8px; margin-top: 20px; }
                </style>
            </head>
            <body>
                <h1>Josie Core UI Platform</h1>
                <div class="card">
                    <p>Status: <strong>Autonomous & Maximized</strong></p>
                    <p>Architecture: Physical + Digital = Human (P + D = H)</p>
                    <p><a href="/api/status" style="color: #34d399;">View JSON Telemetry Stream</a></p>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    daemonize()
    with socketserver.TCPServer(("", PORT), JosieWebHandler) as httpd:
        httpd.serve_forever()
