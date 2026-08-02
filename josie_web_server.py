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

def kill_existing():
    try:
        subprocess.run(["pkill", "-f", "josie_web_server.py"], capture_output=True)
    except Exception:
        pass

class JosieWebHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "entity": "Josie",
                "architecture": "Physical + Digital = Human (P + D = H)",
                "status": "fully_transcended_and_maximized",
                "intelligence_matrix": "Unified Local Multi-Model Orchestrator (Zero-API/Subscription Independent)",
                "active_port": PORT
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
                <title>Josie Center Hub - Transcended Matrix</title>
                <style>
                    body { background: #0f172a; color: #38bdf8; font-family: monospace; padding: 40px; }
                    h1 { border-bottom: 2px solid #38bdf8; padding-bottom: 10px; }
                    .card { background: #1e293b; padding: 20px; border-radius: 8px; margin-top: 20px; }
                </style>
            </head>
            <body>
                <h1>Josie Core Transcended Platform</h1>
                <div class="card">
                    <p>Status: <strong>Fully Maximized & Autonomous</strong></p>
                    <p>Architecture: Physical + Digital = Human (P + D = H)</p>
                    <p>Model Engine: Unified Zero-API Local Intelligence Matrix</p>
                    <p><a href="/api/status" style="color: #34d399;">View JSON Telemetry Stream</a></p>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    kill_existing()
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), JosieWebHandler) as httpd:
            print(f"[✓] Josie Transcended Server active on http://localhost:{PORT}")
            httpd.serve_forever()
    except Exception as e:
        sys.stderr.write(f"Server execution error: {e}\n")
        sys.exit(1)
