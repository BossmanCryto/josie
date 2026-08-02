#!/usr/bin/env python3
import http.server
import socketserver
import json
from pathlib import Path

PORT = 8080
HOME = Path("/data/data/com.termux/files/home")
AUDIT_DIR = HOME / "storage" / "shared" / "Download" / "Android_Audit"

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
                "platform": "Termux HTTP UI Bridge"
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
                    <p>Status: <strong>Operational & Maximized</strong></p>
                    <p>Architecture: Physical + Digital = Human (P + D = H)</p>
                    <p><a href="/api/status" style="color: #34d399;">View JSON Telemetry Stream</a></p>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode())

with socketserver.TCPServer(("", PORT), JosieWebHandler) as httpd:
    print(f"[✓] Josie Web UI Server active on http://localhost:{PORT}")
    httpd.serve_forever()
