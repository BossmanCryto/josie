#!/usr/bin/env python3
"""
JOSIE OS: Supercharged AI Robot Assistant & Workspace Cockpit
Coupled directly with VS Code Web (HTTPS :8088).
Equipped with full Termux tools: Terminal execution, Telemetry, Memory Vault, and File Explorer.
"""
import http.server
import json
import os
import sys
import glob
import subprocess
import socketserver
import urllib.request
import urllib.parse
import urllib.error
import sqlite3

PORT = int(os.environ.get("PORT", 8080))
VSCODE_PORT = int(os.environ.get("VSCODE_PORT", 8088))
WORKSPACE_DIR = "/data/data/com.termux/files/home"
DB_PATH = "/data/data/com.termux/files/home/hummie/core/josie_memory.db"
URL_FILE = "/data/data/com.termux/files/home/.vscode_public_url.txt"
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>⚡ JOSIE AGI COCKPIT</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      height: 100%;
      width: 100%;
      overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
      background: #070b14;
      color: #f1f5f9;
    }

    /* Top Navigation Toolbar */
    .top-bar {
      height: 50px;
      background: #0f172a;
      border-bottom: 1px solid #1e293b;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16px;
      z-index: 100;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .brand h1 {
      font-size: 16px;
      font-weight: 800;
      color: #38bdf8;
      letter-spacing: -0.3px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .brand .telemetry-pill {
      font-size: 11px;
      background: #1e293b;
      color: #38bdf8;
      border: 1px solid #334155;
      padding: 3px 8px;
      border-radius: 12px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
    }
    .telemetry-pill .dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #34d399;
      box-shadow: 0 0 6px #34d399;
    }
    .mode-controls {
      display: flex;
      align-items: center;
      background: #1e293b;
      border-radius: 8px;
      padding: 3px;
      gap: 4px;
    }
    .mode-btn {
      background: transparent;
      border: none;
      color: #94a3b8;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }
    .mode-btn:hover { color: #f8fafc; }
    .mode-btn.active {
      background: #0284c7;
      color: #ffffff;
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.4);
    }
    .external-links {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ext-btn {
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .ext-btn:hover { background: #0369a1; }

    /* Main Workspace Layout */
    .workspace-container {
      display: flex;
      height: calc(100vh - 50px);
      width: 100%;
      position: relative;
    }

    /* Left / Split Chat Panel */
    .chat-panel {
      display: flex;
      flex-direction: column;
      background: #0b0f19;
      border-right: 1px solid #1e293b;
      transition: width 0.25s ease;
      height: 100%;
    }
    .chat-panel.mode-chat {
      width: 100%;
      max-width: 950px;
      margin: 0 auto;
      border-right: none;
    }
    .chat-panel.mode-split {
      width: 440px;
      min-width: 320px;
      max-width: 600px;
    }
    .chat-panel.mode-code {
      display: none;
    }

    /* Chat Messages Box */
    #chat {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      scroll-behavior: smooth;
    }
    .msg {
      max-width: 90%;
      padding: 12px 16px;
      border-radius: 14px;
      line-height: 1.5;
      font-size: 14px;
      word-wrap: break-word;
      white-space: pre-wrap;
    }
    .msg.bot {
      align-self: flex-start;
      background: #131b2e;
      border: 1px solid #1e293b;
      color: #e2e8f0;
      border-bottom-left-radius: 4px;
    }
    .msg.user {
      align-self: flex-end;
      background: #6366f1;
      color: #ffffff;
      border-bottom-right-radius: 4px;
      box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    .msg.terminal {
      align-self: flex-start;
      background: #050810;
      border: 1px solid #0284c7;
      color: #38bdf8;
      font-family: monospace;
      font-size: 12.5px;
      width: 95%;
      border-radius: 10px;
    }
    .sender {
      font-weight: 700;
      font-size: 11px;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .msg.bot .sender { color: #38bdf8; }
    .msg.user .sender { color: #e0e7ff; text-align: right; }
    .msg.terminal .sender { color: #34d399; }

    /* Input Footer & Quick Actions */
    .input-area {
      padding: 10px 16px;
      background: #0f172a;
      border-top: 1px solid #1e293b;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .quick-chips {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 2px;
    }
    .chip {
      background: #1e293b;
      color: #94a3b8;
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 11.5px;
      cursor: pointer;
      white-space: nowrap;
      border: 1px solid #334155;
      transition: all 0.15s;
    }
    .chip:hover {
      background: #38bdf820;
      color: #38bdf8;
      border-color: #38bdf8;
    }
    .input-row {
      display: flex;
      gap: 8px;
      align-items: center;
    }
    input[type="text"] {
      flex: 1;
      padding: 12px 16px;
      border: 1px solid #334155;
      background: #070b14;
      color: #ffffff;
      border-radius: 10px;
      font-size: 14px;
      outline: none;
      transition: all 0.2s;
    }
    input[type="text"]:focus {
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }
    button.icon-btn {
      padding: 12px;
      background: #1e293b;
      color: #94a3b8;
      border: 1px solid #334155;
      border-radius: 10px;
      cursor: pointer;
      font-size: 14px;
      transition: all 0.15s;
    }
    button.icon-btn.recording {
      background: #ef4444;
      color: #fff;
      animation: pulse 1s infinite;
    }
    button.send-btn {
      padding: 12px 20px;
      background: #38bdf8;
      color: #070b14;
      font-weight: 700;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      font-size: 14px;
      transition: background 0.2s, transform 0.1s;
    }
    button.send-btn:hover { background: #0284c7; color: #fff; }
    button.send-btn:active { transform: scale(0.98); }
    button.send-btn:disabled { background: #334155; color: #64748b; cursor: not-allowed; }

    /* Right / Embedded VS Code Panel */
    .vscode-panel {
      flex: 1;
      height: 100%;
      background: #1e1e1e;
      position: relative;
      display: flex;
      flex-direction: column;
    }
    .vscode-panel.mode-chat {
      display: none;
    }
    .vscode-panel.mode-split,
    .vscode-panel.mode-code {
      display: flex;
    }
    iframe#vscodeFrame {
      width: 100%;
      height: 100%;
      border: none;
      background: #1e1e1e;
    }

    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }

    /* Mobile Adaptations */
    @media (max-width: 768px) {
      .chat-panel.mode-split { width: 100%; }
      .vscode-panel.mode-split { display: none; }
    }
  </style>
</head>
<body>
  <!-- Top Navigation Bar -->
  <div class="top-bar">
    <div class="brand">
      <h1>⚡ JOSIE AGI</h1>
      <div class="telemetry-pill" onclick="fetchTelemetry()">
        <span class="dot"></span>
        <span id="telemetryText">LIVE TELEMETRY</span>
      </div>
    </div>

    <!-- Mode Switcher -->
    <div class="mode-controls">
      <button class="mode-btn" id="btnChat" onclick="setMode('chat')">💬 Chat</button>
      <button class="mode-btn active" id="btnSplit" onclick="setMode('split')">⚡ Split Screen</button>
      <button class="mode-btn" id="btnCode" onclick="setMode('code')">💻 VS Code</button>
    </div>

    <!-- External HTTPS Launcher -->
    <div class="external-links">
      <a class="ext-btn" id="extVscodeLink" href="https://192.168.1.23:8088" target="_blank">
        🔒 Open VS Code HTTPS
      </a>
    </div>
  </div>

  <!-- Main Unified Workspace -->
  <div class="workspace-container">
    <!-- Josie AGI Chat Panel -->
    <div class="chat-panel mode-split" id="chatPanel">
      <div id="chat">
        <div class="msg bot">
          <span class="sender">Josie AGI Core</span>
Welcome Jose! All Josie AGI Swarm Tools & Hardware Bridges are fully active.

• **⚡ Terminal Execution**: Type <code>$ &lt;command&gt;</code> to run native bash in Termux.
• **📁 Workspace Intelligence**: Ask *"List workspace"* or *"Read file &lt;name&gt;"*.
• **🧠 Cognitive Recall**: Ask *"Search memory for X"* to query permanent SQLite storage.
• **🔒 VS Code HTTPS**: Access directly or toggle Split-Screen view anytime!
        </div>
      </div>

      <div class="input-area">
        <div class="quick-chips">
          <span class="chip" onclick="quickSend('$ git -C ~/josie-git status')">🌿 Git Status</span>
          <span class="chip" onclick="quickSend('$ free -h && df -h /data')">💾 RAM & Disk</span>
          <span class="chip" onclick="quickSend('Search memory for CVE-2024-3094')">🧠 Memory: XZ Attack</span>
          <span class="chip" onclick="quickSend('List files in workspace')">📁 List Files</span>
          <span class="chip" onclick="fetchTelemetry()">🔋 Telemetry</span>
        </div>
        <div class="input-row">
          <button class="icon-btn" id="micBtn" onclick="toggleSpeech()" title="Voice Dictation">🎤</button>
          <input type="text" id="prompt" placeholder="Ask AI, command workspace, or type $ <command>..." autofocus onkeydown="if(event.key==='Enter') send()">
          <button class="send-btn" id="sendBtn" onclick="send()">Send</button>
        </div>
      </div>
    </div>

    <!-- VS Code Web Frame Panel -->
    <div class="vscode-panel mode-split" id="vscodePanel">
      <iframe id="vscodeFrame" src="" allow="clipboard-read; clipboard-write"></iframe>
    </div>
  </div>

  <script>
    const chat = document.getElementById('chat');
    const input = document.getElementById('prompt');
    const sendBtn = document.getElementById('sendBtn');
    const micBtn = document.getElementById('micBtn');
    const chatPanel = document.getElementById('chatPanel');
    const vscodePanel = document.getElementById('vscodePanel');
    const vscodeFrame = document.getElementById('vscodeFrame');
    const extVscodeLink = document.getElementById('extVscodeLink');
    const telemetryText = document.getElementById('telemetryText');

    const host = window.location.hostname || "192.168.1.23";
    let vscodeUrl = "https://" + host + ":8088/?folder=" + encodeURIComponent("/data/data/com.termux/files/home");
    extVscodeLink.href = vscodeUrl;

    // Check if public Cloudflare tunnel exists
    fetch('/api/public_url').then(r => r.json()).then(d => {
      if (d.url) {
        vscodeUrl = d.url;
        extVscodeLink.href = vscodeUrl;
        extVscodeLink.innerHTML = "🌐 Open Public HTTPS";
      }
    }).catch(() => {});

    function initFrame() {
      if (!vscodeFrame.src || vscodeFrame.src === "about:blank") {
        vscodeFrame.src = vscodeUrl;
      }
    }

    function setMode(mode) {
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      if (mode === 'chat') {
        document.getElementById('btnChat').classList.add('active');
        chatPanel.className = 'chat-panel mode-chat';
        vscodePanel.className = 'vscode-panel mode-chat';
      } else if (mode === 'split') {
        document.getElementById('btnSplit').classList.add('active');
        chatPanel.className = 'chat-panel mode-split';
        vscodePanel.className = 'vscode-panel mode-split';
        initFrame();
      } else if (mode === 'code') {
        document.getElementById('btnCode').classList.add('active');
        chatPanel.className = 'chat-panel mode-code';
        vscodePanel.className = 'vscode-panel mode-code';
        initFrame();
      }
    }

    if (window.innerWidth < 768) {
      setMode('chat');
    } else {
      setMode('split');
    }

    function quickSend(txt) {
      input.value = txt;
      send();
    }

    function appendMessage(sender, text, type) {
      const msgDiv = document.createElement('div');
      msgDiv.className = 'msg ' + (type || 'bot');
      const senderSpan = document.createElement('span');
      senderSpan.className = 'sender';
      senderSpan.textContent = sender;
      msgDiv.appendChild(senderSpan);
      msgDiv.appendChild(document.createTextNode(text));
      chat.appendChild(msgDiv);
      chat.scrollTop = chat.scrollHeight;
    }

    async function fetchTelemetry() {
      try {
        const res = await fetch('/api/telemetry');
        const data = await res.json();
        telemetryText.textContent = `${data.battery}% | ${data.temp}°C | ${data.current_ma}mA`;
        appendMessage('Hardware Guardian', `🔋 Battery: ${data.battery}% (${data.status})\n⚡ Current: ${data.current_ma} mA\n🌡️ Temperature: ${data.temp} °C\n💾 Memory: ${data.mem}\n📁 Storage: ${data.storage}`, 'terminal');
      } catch (err) {
        telemetryText.textContent = "Telemetry Error";
      }
    }

    // Voice Dictation
    let recognition;
    let isRecording = false;
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognition = new SpeechRec();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.onresult = (e) => {
        input.value = e.results[0][0].transcript;
        stopSpeech();
        send();
      };
      recognition.onerror = () => stopSpeech();
      recognition.onend = () => stopSpeech();
    }

    function toggleSpeech() {
      if (!recognition) return alert('Speech recognition not supported in this browser.');
      if (isRecording) {
        stopSpeech();
      } else {
        recognition.start();
        isRecording = true;
        micBtn.classList.add('recording');
      }
    }

    function stopSpeech() {
      if (recognition && isRecording) recognition.stop();
      isRecording = false;
      micBtn.classList.remove('recording');
    }

    async function send() {
      const text = input.value.trim();
      if (!text) return;
      input.value = '';
      appendMessage('You', text, 'user');

      input.disabled = true;
      sendBtn.disabled = true;

      const typingDiv = document.createElement('div');
      typingDiv.className = 'msg bot';
      typingDiv.id = 'typing-indicator';
      typingDiv.textContent = '🤖 Executing...';
      chat.appendChild(typingDiv);
      chat.scrollTop = chat.scrollHeight;

      try {
        const res = await fetch('/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: text })
        });
        const data = await res.json();
        const indicator = document.getElementById('typing-indicator');
        if (indicator) indicator.remove();
        const msgType = data.is_terminal ? 'terminal' : 'bot';
        appendMessage(data.sender || 'Josie AGI', data.reply || "No response received.", msgType);
      } catch (err) {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) indicator.remove();
        appendMessage('Josie AGI', '⚠️ Error: ' + err.message, 'bot');
      } finally {
        input.disabled = false;
        sendBtn.disabled = false;
        input.focus();
      }
    }

    // Auto-fetch initial telemetry
    setTimeout(fetchTelemetry, 1000);
  </script>
</body>
</html>
"""

def execute_shell(cmd):
    """Executes bash commands in Termux."""
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15, cwd=WORKSPACE_DIR)
        out = res.stdout + res.stderr
        return {
            "reply": out.strip() if out.strip() else "(Command executed with no output)",
            "is_terminal": True,
            "sender": f"Terminal [Exit: {res.returncode}]"
        }
    except Exception as e:
        return {"reply": f"Execution error: {e}", "is_terminal": True, "sender": "Terminal Error"}

def query_memory_db(q):
    """Queries permanent SQLite knowledge database."""
    if not os.path.exists(DB_PATH):
        return None
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT timestamp, event, outcome FROM memory WHERE event LIKE ? OR outcome LIKE ? ORDER BY id DESC LIMIT 3", (f"%{q}%", f"%{q}%"))
        rows = c.fetchall()
        conn.close()
        if rows:
            formatted = ["🧠 **Permanent Memory Vault Recall:**"]
            for r in rows:
                formatted.append(f"• **[{r[0]}]** {r[1]}\n  ↳ *Outcome*: {r[2]}")
            return "\n\n".join(formatted)
    except Exception as e:
        return f"Memory DB query error: {e}"
    return None

def get_telemetry():
    """Extracts live battery and system telemetry."""
    # Battery
    battery_level = "100"
    temp_c = "30.0"
    cur_ma = "0"
    status = "Active"
    try:
        res = subprocess.run(["dumpsys", "battery"], capture_output=True, text=True, timeout=2).stdout
        import re
        b = re.search(r"level:\s*(\d+)", res)
        t = re.search(r"temperature:\s*(\d+)", res)
        c = re.search(r"current_now:\s*(-?\d+)", res)
        if b: battery_level = b.group(1)
        if t: temp_c = f"{int(t.group(1))/10:.1f}"
        if c: cur_ma = c.group(1)
    except Exception:
        pass

    # RAM & Disk
    mem = ""
    disk = ""
    try:
        mem = subprocess.run(["free", "-h"], capture_output=True, text=True).stdout.splitlines()[1]
        disk = subprocess.run(["df", "-h", "/data"], capture_output=True, text=True).stdout.splitlines()[1]
    except Exception:
        pass

    return {
        "battery": battery_level,
        "temp": temp_c,
        "current_ma": cur_ma,
        "status": status,
        "mem": mem,
        "storage": disk
    }

def ask_pollinations_get(prompt):
    """Clean high-speed Pollinations GET endpoint."""
    try:
        clean = urllib.parse.quote(prompt.strip())
        url = f"https://text.pollinations.ai/{clean}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception as e:
        sys.stderr.write(f"⚠️ Pollinations error: {e}\n")
    return None

def process_ai_turn(prompt):
    p_strip = prompt.strip()

    # 1. Direct Shell Execution ($ <cmd> or sh: <cmd>)
    if p_strip.startswith("$ ") or p_strip.startswith("sh: ") or p_strip.startswith("run: "):
        cmd = p_strip.split(" ", 1)[1] if " " in p_strip else p_strip[1:]
        return execute_shell(cmd)

    # 2. Memory Vault Query
    if "memory" in p_strip.lower() or "recall" in p_strip.lower() or "vault" in p_strip.lower():
        q_term = p_strip.replace("search memory for", "").replace("search memory", "").replace("recall", "").strip()
        mem_res = query_memory_db(q_term if q_term else "XZ")
        if mem_res:
            return {"reply": mem_res, "is_terminal": False}

    # 3. Workspace Inspection
    if any(k in p_strip.lower() for k in ["list file", "what file", "files in workspace", "show files"]):
        try:
            items = sorted([f for f in os.listdir(WORKSPACE_DIR) if not f.startswith(".")])[:40]
            dirs = [f + "/" for f in items if os.path.isdir(os.path.join(WORKSPACE_DIR, f))]
            files = [f for f in items if os.path.isfile(os.path.join(WORKSPACE_DIR, f))]
            reply = f"📁 **Workspace (`~`) Files**:\n\n**Directories:** {', '.join(dirs)}\n\n**Files:** {', '.join(files)}\n\n👉 Edit any file directly in VS Code Web on the right!"
            return {"reply": reply, "is_terminal": False}
        except Exception as e:
            return {"reply": f"Error: {e}", "is_terminal": False}

    # 4. Standard AI Intelligence Call
    ai_resp = ask_pollinations_get(prompt)
    if ai_resp:
        return {"reply": ai_resp, "is_terminal": False}

    return {"reply": "⚠️ Service temporarily busy. Please try asking again.", "is_terminal": False}

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode("utf-8"))
        elif self.path == "/api/telemetry":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(get_telemetry()).encode("utf-8"))
        elif self.path == "/api/public_url":
            pub_url = ""
            if os.path.exists(URL_FILE):
                try:
                    pub_url = open(URL_FILE).read().strip()
                except Exception:
                    pass
        elif self.path in ["/download/base44.apk", "/download/Base44Platform.apk"]:
            apk_path = "/data/data/com.termux/files/home/Base44Platform.apk"
            if os.path.exists(apk_path):
                self.send_response(200)
                self.send_header("Content-Type", "application/vnd.android.package-archive")
                self.send_header("Content-Disposition", 'attachment; filename="Base44Platform.apk"')
                self.end_headers()
                with open(apk_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/chat":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                data = json.loads(body)
                prompt = data.get("prompt", "").strip()
                res = process_ai_turn(prompt)
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(res).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def main():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"🚀 JOSIE COCKPIT LIVE on 0.0.0.0:{PORT}", flush=True)
        print(f"👉 Local:   http://127.0.0.1:{PORT}", flush=True)
        print(f"👉 Network: http://192.168.1.23:{PORT}", flush=True)
        httpd.serve_forever()

if __name__ == "__main__":
    main()
