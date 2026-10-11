#!/usr/bin/env python3
"""
JOSIE OS: AI Robot Assistant Server (Port 8080)
Multi-backend resilient AI chat server.
Zero-config free tier (Pollinations AI / OpenAI model) + Optional Gemini fallback.
Accessible on Local: http://127.0.0.1:8080 and Network: http://192.168.1.23:8080
"""
import http.server
import json
import os
import sys
import socketserver
import urllib.request
import urllib.parse
import urllib.error

PORT = int(os.environ.get("PORT", 8080))
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "").strip()

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>🤖 Josie AI Robot Assistant</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
      max-width: 850px;
      margin: 0 auto;
      padding: 16px;
      background: #090d16;
      color: #f1f5f9;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    .box {
      background: #131b2e;
      padding: 20px;
      border-radius: 18px;
      box-shadow: 0 12px 40px rgba(0,0,0,0.7);
      border: 1px solid #1e293b;
      display: flex;
      flex-direction: column;
      flex: 1;
      height: 90vh;
    }
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
      border-bottom: 1px solid #1e293b;
      padding-bottom: 12px;
    }
    .title-area {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    h2 {
      color: #38bdf8;
      font-size: 20px;
      font-weight: 700;
      letter-spacing: -0.5px;
    }
    .subtitle {
      font-size: 11px;
      color: #94a3b8;
    }
    .status-pill {
      font-size: 11px;
      padding: 4px 10px;
      border-radius: 20px;
      background: #064e3b;
      color: #34d399;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .status-pill::before {
      content: "";
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #34d399;
      box-shadow: 0 0 8px #34d399;
    }
    #chat {
      flex: 1;
      overflow-y: auto;
      border: 1px solid #1e293b;
      padding: 16px;
      border-radius: 14px;
      margin-bottom: 14px;
      background: #0b1120;
      display: flex;
      flex-direction: column;
      gap: 12px;
      scroll-behavior: smooth;
    }
    .msg {
      max-width: 85%;
      padding: 12px 16px;
      border-radius: 16px;
      line-height: 1.5;
      font-size: 14.5px;
      word-wrap: break-word;
      white-space: pre-wrap;
    }
    .msg.bot {
      align-self: flex-start;
      background: #1e293b;
      border: 1px solid #334155;
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
    .sender {
      font-weight: 700;
      font-size: 11px;
      margin-bottom: 4px;
      display: block;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .msg.bot .sender { color: #38bdf8; }
    .msg.user .sender { color: #e0e7ff; text-align: right; }
    .input-row {
      display: flex;
      gap: 10px;
    }
    input[type="text"] {
      flex: 1;
      padding: 14px 18px;
      border: 1px solid #334155;
      background: #0b1120;
      color: #ffffff;
      border-radius: 12px;
      font-size: 15px;
      outline: none;
      transition: all 0.2s;
    }
    input[type="text"]:focus {
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
    }
    button {
      padding: 14px 24px;
      background: #38bdf8;
      color: #0b1120;
      font-weight: 700;
      border: none;
      border-radius: 12px;
      cursor: pointer;
      font-size: 15px;
      transition: background 0.2s, transform 0.1s;
    }
    button:hover { background: #0284c7; color: #fff; }
    button:active { transform: scale(0.98); }
    button:disabled { background: #334155; color: #64748b; cursor: not-allowed; }
    .typing {
      font-style: italic;
      color: #94a3b8;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .network-badge {
      font-size: 11px;
      color: #64748b;
      margin-top: 8px;
      text-align: center;
    }
    .network-badge a { color: #38bdf8; text-decoration: none; }
  </style>
</head>
<body>
  <div class="box">
    <div class="header">
      <div class="title-area">
        <div>
          <h2>🤖 Josie AI Robot</h2>
          <div class="subtitle">Autonomous Swarm Companion • Port 8080</div>
        </div>
      </div>
      <span class="status-pill">ONLINE</span>
    </div>

    <div id="chat">
      <div class="msg bot">
        <span class="sender">Josie Robot</span>
Hello Jose! I am your AI Robot Assistant running directly on your Samsung Galaxy A17 5G Termux node.

All intelligence engines are active. You can chat with me here, or access this dashboard from your Chromebook at:
👉 http://192.168.1.23:8080

How can I help you right now?
      </div>
    </div>

    <div class="input-row">
      <input type="text" id="prompt" placeholder="Type your message..." autofocus onkeydown="if(event.key==='Enter') send()">
      <button id="sendBtn" onclick="send()">Send</button>
    </div>
    <div class="network-badge">
      Local: <code>http://127.0.0.1:8080</code> | LAN: <a href="http://192.168.1.23:8080" target="_blank"><code>http://192.168.1.23:8080</code></a>
    </div>
  </div>

  <script>
    const chat = document.getElementById('chat');
    const input = document.getElementById('prompt');
    const sendBtn = document.getElementById('sendBtn');

    function appendMessage(sender, text, isBot) {
      const msgDiv = document.createElement('div');
      msgDiv.className = 'msg ' + (isBot ? 'bot' : 'user');
      const senderSpan = document.createElement('span');
      senderSpan.className = 'sender';
      senderSpan.textContent = sender;
      msgDiv.appendChild(senderSpan);
      msgDiv.appendChild(document.createTextNode(text));
      chat.appendChild(msgDiv);
      chat.scrollTop = chat.scrollHeight;
    }

    async function send() {
      const text = input.value.trim();
      if (!text) return;
      input.value = '';
      appendMessage('You', text, false);

      input.disabled = true;
      sendBtn.disabled = true;

      const typingDiv = document.createElement('div');
      typingDiv.className = 'msg bot typing';
      typingDiv.id = 'typing-indicator';
      typingDiv.textContent = '🤖 Thinking...';
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
        appendMessage('Josie Robot', data.reply || "No response received.", true);
      } catch (err) {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) indicator.remove();
        appendMessage('Josie Robot', '⚠️ Error: ' + err.message, true);
      } finally {
        input.disabled = false;
        sendBtn.disabled = false;
        input.focus();
      }
    }
  </script>
</body>
</html>
"""

def ask_pollinations_post(prompt):
    """Primary high-reliability engine: Pollinations OpenAI endpoint"""
    try:
        payload = json.dumps({
            "messages": [
                {"role": "system", "content": "You are Josie OS AI Robot Assistant on Android Termux. You are fast, highly knowledgeable, friendly, and helpful."},
                {"role": "user", "content": prompt}
            ],
            "model": "openai",
            "seed": 42
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://text.pollinations.ai/",
            data=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Linux; Android 14; Galaxy A17) AppleWebKit/537.36"
            }
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            text = resp.read().decode("utf-8").strip()
            if text:
                return text
    except Exception as e:
        sys.stderr.write(f"⚠️ Pollinations POST failed: {e}\n")
    return None

def ask_pollinations_get(prompt):
    """Fallback: Pollinations GET endpoint"""
    try:
        encoded = urllib.parse.quote(prompt[:200])
        url = f"https://text.pollinations.ai/{encoded}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            text = resp.read().decode("utf-8").strip()
            if text:
                return text
    except Exception as e:
        sys.stderr.write(f"⚠️ Pollinations GET failed: {e}\n")
    return None

def ask_gemini_api(prompt):
    """Gemini 2.5/1.5 Flash endpoint if valid AI Studio API key provided"""
    if not GEMINI_KEY or not GEMINI_KEY.startswith("AIza"):
        return None
    for model in ["gemini-2.5-flash", "gemini-1.5-flash"]:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_KEY}"
            payload = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                candidates = data.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    if parts:
                        return parts[0].get("text", "").strip()
        except Exception as e:
            sys.stderr.write(f"⚠️ Gemini {model} failed: {e}\n")
    return None

def ask_ai(prompt):
    # 1. Try Gemini if valid key configured
    res = ask_gemini_api(prompt)
    if res:
        return res

    # 2. Primary free engine (Pollinations OpenAI)
    res = ask_pollinations_post(prompt)
    if res:
        return res

    # 3. Fallback GET
    res = ask_pollinations_get(prompt)
    if res:
        return res

    return "⚠️ Server temporarily busy or internet connection interrupted. Please try asking again in a moment."

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
        elif self.path == "/healthz":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "port": PORT}).encode("utf-8"))
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
                if not prompt:
                    reply = "Please enter a message."
                else:
                    reply = ask_ai(prompt)
                resp_json = json.dumps({"reply": reply})
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(resp_json.encode("utf-8"))
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
        print(f"🚀 AI Robot Assistant Web Server LIVE on 0.0.0.0:{PORT}", flush=True)
        print(f"👉 Local:   http://127.0.0.1:{PORT}", flush=True)
        print(f"👉 Network: http://192.168.1.23:{PORT}", flush=True)
        httpd.serve_forever()

if __name__ == "__main__":
    main()
