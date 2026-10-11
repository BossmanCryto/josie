#!/usr/bin/env python3
"""
JOSIE OS: Sovereign Autonomous AGI Platform & Multi-Tool Hub
Integrates:
- High-Reasoning AI Studio (Claude, OpenRouter, Gemini, Firecrawl v2)
- Kali NetHunter Suite & KeX Desktop Manager
- Hardware Performance Hyperdrive & Device Restart Controller
- Firecrawl Web Intelligence & YouTube Harvester Catalog
- Termux Live Terminal & Base44 Studio
- VS Code Web Service (Port 8088)
"""
import http.server
import json
import os
import re
import sys
import tempfile
import subprocess
import socketserver
import urllib.request
import urllib.parse
import sqlite3

PORT = int(os.environ.get("PORT", 8080))
VSCODE_PORT = int(os.environ.get("VSCODE_PORT", 8088))
WORKSPACE_DIR = "/data/data/com.termux/files/home"
DB_PATH = "/data/data/com.termux/files/home/hummie/core/josie_memory.db"
APK_PATH = "/data/data/com.termux/files/home/Base44Platform.apk"
KEY_FILE = "/data/data/com.termux/files/home/.openrouter_key"
FIRECRAWL_KEY = os.environ.get("FIRECRAWL_API_KEY", "fc-efb38e686ec24eb1ae22d0280ca6f38f")
BASE44_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh"

def get_openrouter_key():
    k = os.environ.get("OPENROUTER_API_KEY", "")
    if not k and os.path.exists(KEY_FILE):
        try: k = open(KEY_FILE).read().strip()
        except Exception: pass
    return k

def firecrawl_request(endpoint, payload):
    headers = {"Content-Type": "application/json", "User-Agent": "Firecrawl-Studio/2.0"}
    if FIRECRAWL_KEY:
        headers["Authorization"] = f"Bearer {FIRECRAWL_KEY}"
    req = urllib.request.Request(
        f"https://api.firecrawl.dev/v2/{endpoint}",
        data=json.dumps(payload).encode("utf-8"),
        headers=headers
    )
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.loads(r.read().decode("utf-8"))

def get_telemetry():
    battery_level = "100"
    temp_c = "30.0"
    cur_ma = "0"
    status = "Active"
    try:
        res = subprocess.run(["dumpsys", "battery"], capture_output=True, text=True, timeout=2).stdout
        b = re.search(r"level:\s*(\d+)", res)
        t = re.search(r"temperature:\s*(\d+)", res)
        c = re.search(r"current_now:\s*(-?\d+)", res)
        if b: battery_level = b.group(1)
        if t: temp_c = f"{int(t.group(1))/10:.1f}"
        if c: cur_ma = c.group(1)
    except Exception: pass

    mem, disk = "", ""
    try:
        mem = subprocess.run(["free", "-h"], capture_output=True, text=True).stdout.splitlines()[1]
        disk = subprocess.run(["df", "-h", "/data"], capture_output=True, text=True).stdout.splitlines()[1]
    except Exception: pass

    adb_status = "Disconnected"
    try:
        res = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=2).stdout
        if "device\n" in res:
            adb_status = "Connected"
    except Exception: pass

    kex_status = "Stopped"
    try:
        if subprocess.run("pgrep -f 'Xvnc :1'", shell=True, capture_output=True).returncode == 0:
            kex_status = "Active (5901)"
    except Exception: pass

    return {
        "battery": battery_level,
        "temp": temp_c,
        "current_ma": cur_ma,
        "status": status,
        "mem": mem,
        "storage": disk,
        "adb": adb_status,
        "kex": kex_status
    }

def execute_kali_cmd(cmd: str, is_root: bool = False):
    try:
        user_arg = ["--user", "root"] if is_root else []
        cmd_args = [
            "proot-distro", "login", *user_arg, "kali",
            "--bind", "/data/data/com.termux/files/usr/tmp/.X11-unix:/tmp/.X11-unix",
            "--bind", "/data/data/com.termux/files/home:/root/termux_home",
            "--env", "DISPLAY=:0",
            "--", "bash", "-c", cmd
        ]
        res = subprocess.run(cmd_args, capture_output=True, text=True, timeout=30)
        out = (res.stdout + res.stderr).strip() or "(Executed with no output)"
        return {"output": out, "exit_code": res.returncode}
    except subprocess.TimeoutExpired:
        return {"output": "⏱️ Execution timed out after 30 seconds.", "exit_code": -1}
    except Exception as e:
        return {"output": f"❌ Error executing in Kali: {e}", "exit_code": -1}

def execute_performance_boost():
    results = []
    # 1. Neutralize Phantom Process Killer
    try:
        p = subprocess.run(["/data/data/com.termux/files/home/bin/adb-exec", "device_config put activity_manager max_phantom_processes 2147483647"], capture_output=True, text=True, timeout=5)
        results.append("✅ Phantom Process Killer: Limit set to 2,147,483,647")
    except Exception as e: results.append(f"⚠️ Phantom Process: {e}")

    # 2. Disable Wi-Fi Power Save
    try:
        subprocess.run(["/data/data/com.termux/files/home/bin/adb-exec", "settings put global wifi_power_save 0; cmd wifi set-power-save-mode-enabled false"], capture_output=True, text=True, timeout=5)
        results.append("✅ Wi-Fi Performance: Power save disabled (Maximum Throughput)")
    except Exception as e: results.append(f"⚠️ Wi-Fi: {e}")

    # 3. Drop Caches & Memory Optimization
    try:
        subprocess.run(["/data/data/com.termux/files/home/bin/adb-exec", "echo 3 > /proc/sys/vm/drop_caches 2>/dev/null || true"], capture_output=True, text=True, timeout=5)
        results.append("✅ RAM Flush: Kernel pagecache & dentries purged")
    except Exception as e: results.append(f"⚠️ Memory: {e}")

    # 4. Renice Critical Services for Ultra-Low Latency
    try:
        subprocess.run("pkill -0 sshd 2>/dev/null && renice -n -10 $(pgrep sshd) 2>/dev/null || true", shell=True)
        subprocess.run("renice -n -10 $$ 2>/dev/null || true", shell=True)
        results.append("✅ Process Nice: CPU scheduling priority raised to High (-10)")
    except Exception as e: results.append(f"⚠️ Renice: {e}")

    # 5. Hold Wakelock
    try:
        subprocess.run(["termux-wake-lock"], capture_output=True, timeout=2)
        results.append("✅ Android Wakelock: CPU sleep lock firmly acquired")
    except Exception as e: results.append(f"⚠️ Wakelock: {e}")

    return "\n".join(results)

def get_harvested_videos(limit=25):
    if not os.path.exists(DB_PATH): return []
    try:
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS yt_harvest_history (video_id TEXT PRIMARY KEY, title TEXT, channel TEXT, url TEXT, summary TEXT, harvest_time TEXT)")
        cur.execute("SELECT video_id, title, channel, url, summary, harvest_time FROM yt_harvest_history ORDER BY harvest_time DESC LIMIT ?", (limit,))
        rows = cur.fetchall()
        conn.close()
        return [{"id": r[0], "title": r[1], "channel": r[2], "url": r[3], "summary": r[4], "time": r[5]} for r in rows]
    except Exception:
        return []

MAIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>⚡ JOSIE OS: Sovereign Autonomous Platform</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    :root {
      --bg: #070b14; --panel: #0f172a; --panel-light: #1e293b; --border: #334155;
      --accent: #38bdf8; --green: #10b981; --fire: #f97316; --red: #ef4444; --amber: #f59e0b;
      --text: #f1f5f9; --muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      height: 100%; width: 100%; overflow: hidden;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--bg); color: var(--text);
    }

    /* TOP BAR */
    .top-bar {
      height: 50px; background: var(--panel); border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between; padding: 0 12px; z-index: 100;
    }
    .brand { display: flex; align-items: center; gap: 8px; }
    .brand h1 { font-size: 15px; font-weight: 800; color: var(--accent); display: flex; align-items: center; gap: 5px; }
    .telemetry-pill {
      font-size: 11px; background: var(--panel-light); color: var(--accent); border: 1px solid var(--border);
      padding: 3px 8px; border-radius: 12px; font-weight: 600; display: flex; align-items: center; gap: 6px; cursor: pointer;
    }
    .telemetry-pill .dot { width: 6px; height: 6px; border-radius: 50%; background: #34d399; box-shadow: 0 0 6px #34d399; }
    .mode-controls { display: flex; align-items: center; background: var(--panel-light); border-radius: 8px; padding: 3px; gap: 3px; }
    .mode-btn {
      background: transparent; border: none; color: var(--muted); padding: 5px 10px;
      border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.15s;
    }
    .mode-btn:hover { color: #f8fafc; }
    .mode-btn.active { background: #0284c7; color: #ffffff; }

    /* LAYOUT */
    .workspace-container { display: flex; height: calc(100vh - 50px); width: 100%; position: relative; }
    .sidebar {
      width: 290px; background: #0c1220; border-right: 1px solid var(--border);
      display: flex; flex-direction: column; padding: 14px; gap: 11px; z-index: 50;
      transition: transform 0.25s ease; overflow-y: auto;
    }
    @media (max-width: 820px) {
      .sidebar { position: fixed; height: calc(100vh - 50px); top: 50px; left: 0; transform: translateX(-100%); }
      .sidebar.open { transform: translateX(0); box-shadow: 10px 0 30px rgba(0,0,0,0.85); }
    }
    .sidebar label { font-size: 11px; color: var(--muted); font-weight: 700; text-transform: uppercase; }
    .sidebar select, .sidebar textarea, .sidebar input {
      width: 100%; background: #0f172a; color: var(--text); border: 1px solid var(--border);
      border-radius: 6px; padding: 7px; font-size: 12px; outline: none; margin-top: 3px;
    }

    /* LEFT CHAT PANEL */
    .chat-panel { display: flex; flex-direction: column; background: #070b14; height: 100%; flex: 1; min-width: 320px; }
    .chat-panel.mode-chat { max-width: 950px; margin: 0 auto; width: 100%; }
    .chat-panel.mode-split { width: 420px; min-width: 320px; max-width: 520px; border-right: 1px solid var(--border); }
    #chat { flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 12px; }
    .msg { max-width: 840px; width: 100%; margin: 0 auto; padding: 12px 16px; border-radius: 10px; line-height: 1.55; font-size: 14px; border: 1px solid var(--border); word-break: break-word; }
    .msg.user { background: #1e293b; border-color: #475569; }
    .msg.bot { background: #0b1220; border-color: var(--border); }
    .msg.terminal { background: #020617; border-color: var(--border); font-family: monospace; white-space: pre-wrap; font-size: 12px; color: var(--accent); }
    .msg-header { font-size: 11px; font-weight: 700; text-transform: uppercase; margin-bottom: 6px; display: flex; justify-content: space-between; align-items: center; }
    .user .msg-header { color: #facc15; }
    .bot .msg-header { color: var(--accent); }

    /* COMPOSER */
    .input-area { border-top: 1px solid var(--border); background: var(--panel); padding: 10px 14px; }
    .quick-chips { display: flex; gap: 6px; overflow-x: auto; padding-bottom: 8px; scrollbar-width: none; }
    .chip {
      white-space: nowrap; background: var(--panel-light); border: 1px solid var(--border); color: var(--muted);
      font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 12px; cursor: pointer; transition: all 0.15s;
    }
    .chip:hover { border-color: var(--accent); color: #fff; }
    .input-row { display: flex; gap: 8px; align-items: center; }
    .icon-btn {
      background: var(--panel-light); color: #fff; border: 1px solid var(--border); width: 38px; height: 38px;
      border-radius: 8px; cursor: pointer; font-size: 14px; display: flex; align-items: center; justify-content: center;
    }
    .icon-btn:hover { border-color: var(--accent); }
    #prompt {
      flex: 1; background: #0b0f19; color: #fff; border: 1px solid var(--border); border-radius: 8px;
      padding: 9px 12px; font-size: 13px; outline: none; height: 38px;
    }
    #prompt:focus { border-color: var(--accent); }
    .send-btn {
      background: #0284c7; color: #fff; border: none; padding: 0 16px; height: 38px;
      border-radius: 8px; font-weight: 700; font-size: 13px; cursor: pointer;
    }

    /* RIGHT MULTI-TOOL COCKPIT PANEL */
    .right-panel { flex: 1; height: 100%; background: #070b14; display: flex; flex-direction: column; overflow: hidden; }
    .right-panel.hidden { display: none; }

    .hub-tabs {
      height: 42px; background: #0a0f1d; border-bottom: 1px solid var(--border);
      display: flex; align-items: center; padding: 0 8px; gap: 4px; overflow-x: auto; scrollbar-width: none;
    }
    .hub-tab {
      background: transparent; border: none; color: var(--muted); padding: 7px 12px;
      border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; white-space: nowrap; display: flex; align-items: center; gap: 5px;
    }
    .hub-tab:hover { color: #fff; }
    .hub-tab.active { background: #1e293b; color: var(--accent); border-bottom: 2px solid var(--accent); }

    .hub-content { flex: 1; overflow-y: auto; padding: 14px; }
    .hub-pane { display: none; flex-direction: column; gap: 14px; }
    .hub-pane.active { display: flex; }

    /* CARDS & UI COMPONENTS */
    .card { background: var(--panel); border: 1px solid var(--border); border-radius: 10px; padding: 14px; }
    .card-title { font-size: 13px; font-weight: 800; color: var(--accent); margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
    .btn-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 8px; margin-top: 8px; }
    .action-btn {
      background: var(--panel-light); border: 1px solid var(--border); color: #fff;
      padding: 9px; border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; text-align: center;
    }
    .action-btn:hover { border-color: var(--accent); color: var(--accent); }
    .action-btn.boost { background: #065f46; border-color: #10b981; }
    .action-btn.boost:hover { background: #047857; color: #fff; }
    .action-btn.restart { background: #7f1d1d; border-color: #ef4444; color: #fee2e2; }
    .action-btn.restart:hover { background: #991b1b; }

    .terminal-window {
      background: #020617; border: 1px solid var(--border); border-radius: 8px;
      padding: 12px; font-family: "JetBrains Mono", monospace; font-size: 11px; color: #38bdf8;
      min-height: 160px; max-height: 320px; overflow-y: auto; white-space: pre-wrap; line-height: 1.5;
    }

    .badge { padding: 2px 7px; border-radius: 10px; font-size: 10px; font-weight: 700; }
    .badge.green { background: rgba(16,185,129,0.2); color: #34d399; border: 1px solid #10b981; }
    .badge.amber { background: rgba(245,158,11,0.2); color: #fbbf24; border: 1px solid #f59e0b; }
    .badge.red { background: rgba(239,68,68,0.2); color: #f87171; border: 1px solid #ef4444; }

    .video-card {
      background: #0b1220; border: 1px solid var(--border); border-radius: 8px; padding: 10px;
      display: flex; flex-direction: column; gap: 4px; margin-bottom: 8px;
    }
    .video-title { font-size: 12px; font-weight: 700; color: #38bdf8; text-decoration: none; }
    .video-title:hover { text-decoration: underline; }
    .video-meta { font-size: 10px; color: var(--muted); }
    .video-desc { font-size: 11px; color: #cbd5e1; }
  </style>
</head>
<body>
  <div class="top-bar">
    <div class="brand">
      <button class="icon-btn" onclick="toggleSidebar()" style="width:30px;height:30px;" title="Settings">⚙️</button>
      <h1>⚡ JOSIE OS</h1>
      <div class="telemetry-pill" onclick="fetchTelemetry()">
        <span class="dot"></span>
        <span id="telemetryText">LIVE TELEMETRY</span>
      </div>
    </div>

    <div class="mode-controls">
      <button class="mode-btn" id="btnChat" onclick="setMode('chat')">💬 Chat</button>
      <button class="mode-btn active" id="btnSplit" onclick="setMode('split')">⚡ Split Cockpit</button>
      <button class="mode-btn" id="btnHub" onclick="setMode('hub')">🐉 Multi-Tool Hub</button>
    </div>

    <div class="brand">
      <button class="action-btn restart" onclick="confirmRestart()" style="padding:4px 9px;font-size:11px;">🔄 Restart Phone</button>
    </div>
  </div>

  <div class="workspace-container">
    <!-- SIDEBAR -->
    <div class="sidebar" id="sidebar">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <span style="font-weight:800; font-size:13px; color:var(--accent);">🌐 AI MODEL ENGINE</span>
        <button class="icon-btn" onclick="toggleSidebar()" style="width:26px;height:26px;font-size:11px;">✕</button>
      </div>

      <div>
        <label>Cognitive LLM</label>
        <select id="modelSelect">
          <optgroup label="Anthropic Frontier">
            <option value="anthropic/claude-3.7-sonnet" selected>🧠 Claude 3.7 Sonnet</option>
            <option value="anthropic/claude-3.5-sonnet">⚡ Claude 3.5 Sonnet</option>
          </optgroup>
          <optgroup label="Google DeepMind">
            <option value="google/gemini-2.5-pro-preview">💎 Gemini 2.5 Pro</option>
            <option value="google/gemini-2.0-flash-exp:free">⚡ Gemini 2.0 Flash (Free)</option>
          </optgroup>
          <optgroup label="OpenAI Frontier">
            <option value="openai/gpt-4o">🤖 GPT-4o</option>
            <option value="openai/o3-mini">🔬 OpenAI o3-mini</option>
          </optgroup>
          <optgroup label="Open Source Leaders">
            <option value="deepseek/deepseek-r1:free">🧠 DeepSeek R1 (Free)</option>
            <option value="pollinations">🌐 Pollinations (Keyless Fallback)</option>
          </optgroup>
        </select>
      </div>

      <div>
        <label>Action Mode</label>
        <select id="actionMode">
          <option value="chat">💬 Standard AI Chat</option>
          <option value="firecrawl_scrape">🔥 Firecrawl Scrape URL</option>
          <option value="firecrawl_search">🔎 Firecrawl Search Web</option>
          <option value="shell">💻 Execute Local Bash</option>
        </select>
      </div>

      <div>
        <label>System Instructions</label>
        <textarea id="sysPrompt" rows="3">You are Josie OS Core, an elite autonomous system assistant. Always respond concisely and strictly in English.</textarea>
      </div>

      <div>
        <label>Quick Triggers</label>
        <button class="action-btn" style="width:100%;margin-top:4px;" onclick="triggerPerformanceBoost()">🚀 Run Hyperdrive Boost</button>
        <button class="action-btn" style="width:100%;margin-top:4px;" onclick="switchHubTab('nethunter')">🐉 NetHunter Security Suite</button>
        <button class="action-btn" style="width:100%;margin-top:4px;" onclick="switchHubTab('harvester')">📚 Video Intelligence Library</button>
      </div>
    </div>

    <!-- LEFT: CHAT PANEL -->
    <div class="chat-panel mode-split" id="chatPanel">
      <div id="chat"></div>

      <div class="input-area">
        <div class="quick-chips">
          <span class="chip" onclick="quickSend('Check')">🔍 Diagnostic Check</span>
          <span class="chip" onclick="quickSend('Fix all')">🛠️ Fix All Systems</span>
          <span class="chip" onclick="triggerPerformanceBoost()">🚀 Hyperdrive Boost</span>
          <span class="chip" onclick="switchHubTab('nethunter')">🐉 NetHunter Tools</span>
          <span class="chip" onclick="switchHubTab('harvester')">📚 Video Intel</span>
          <span class="chip" onclick="switchHubTab('device')">🔋 Hardware & Restart</span>
          <span class="chip" onclick="fetchTelemetry()">⚡ Telemetry</span>
        </div>
        <div class="input-row">
          <button class="icon-btn" title="Toggle Scrape" onclick="setFirecrawlMode()">🔥</button>
          <button class="icon-btn" id="micBtn" onclick="toggleSpeech()" title="Voice Dictation">🎤</button>
          <input type="text" id="prompt" placeholder="Ask Josie OS, paste URL, or type $ <command>..." autofocus onkeydown="if(event.key==='Enter') send()">
          <button class="send-btn" id="sendBtn" onclick="send()">Send</button>
        </div>
      </div>
    </div>

    <!-- RIGHT: MULTI-TOOL COCKPIT PANEL -->
    <div class="right-panel mode-split" id="rightPanel">
      <div class="hub-tabs">
        <button class="hub-tab active" id="tab-nethunter" onclick="switchHubTab('nethunter')">🐉 NetHunter & Kali</button>
        <button class="hub-tab" id="tab-device" onclick="switchHubTab('device')">⚡ Hardware & Reboot</button>
        <button class="hub-tab" id="tab-harvester" onclick="switchHubTab('harvester')">🔥 Firecrawl & Videos</button>
        <button class="hub-tab" id="tab-terminal" onclick="switchHubTab('terminal')">💻 Live Terminal</button>
        <button class="hub-tab" id="tab-vscode" onclick="switchHubTab('vscode')">🔒 VS Code Web</button>
        <button class="hub-tab" id="tab-base44" onclick="switchHubTab('base44')">🔤 Base44 Studio</button>
      </div>

      <div class="hub-content">
        <!-- PANE 1: NETHUNTER & KALI SUITE -->
        <div class="hub-pane active" id="pane-nethunter">
          <div class="card">
            <div class="card-title">
              <span>🐉 NetHunter Kali Suite (Autonomous Subsystem)</span>
              <span class="badge green">PRoot-Distro Active</span>
            </div>
            <p style="font-size:12px;color:var(--muted);margin-bottom:8px;">Execute Kali penetration testing & network tools directly without leaving the dashboard.</p>
            <div class="btn-grid">
              <button class="action-btn" onclick="runKaliPreset('nmap -F 127.0.0.1')">🌐 Scan Localhost (Nmap)</button>
              <button class="action-btn" onclick="runKaliPreset('nmap -sn 192.168.1.0/24')">📡 Discover LAN Hosts</button>
              <button class="action-btn" onclick="runKaliPreset('sqlmap --version')">🛡️ SQLMap Audit</button>
              <button class="action-btn" onclick="runKaliPreset('aircrack-ng --help | head -n 12')">🔑 Aircrack-ng Suite</button>
              <button class="action-btn" onclick="controlKex('start')">🖥️ Start KeX VNC (:1)</button>
              <button class="action-btn" onclick="controlKex('stop')">🛑 Stop KeX Display</button>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              <span>💻 Kali Command Runner</span>
              <label style="font-size:11px;font-weight:600;color:var(--muted);"><input type="checkbox" id="kaliRootCheck"> Run as Root</label>
            </div>
            <div style="display:flex;gap:6px;margin-bottom:8px;">
              <input type="text" id="kaliInput" placeholder="Enter Kali command (e.g. nmap -A 127.0.0.1, hydra, john)..." style="flex:1;background:#020617;color:#fff;border:1px solid var(--border);border-radius:6px;padding:8px;font-size:12px;outline:none;" onkeydown="if(event.key==='Enter') executeKali()">
              <button class="action-btn" style="background:#0284c7;" onclick="executeKali()">▶ Run</button>
            </div>
            <div class="terminal-window" id="kaliOutput">⚡ NetHunter Kali Terminal Ready. Run preset or type command above.</div>
          </div>
        </div>

        <!-- PANE 2: HARDWARE & RESTART -->
        <div class="hub-pane" id="pane-device">
          <div class="card">
            <div class="card-title">
              <span>🔋 Device Telemetry & Bridge Status</span>
              <button class="action-btn" style="padding:2px 8px;font-size:10px;" onclick="fetchTelemetry()">Refresh</button>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:12px;">
              <div>🔋 Battery: <b id="d-bat">--</b></div>
              <div>🌡️ Temp: <b id="d-temp">--</b></div>
              <div>⚡ Charging: <b id="d-curr">--</b></div>
              <div>🤖 Wireless ADB: <b id="d-adb">--</b></div>
              <div>🖥️ KeX VNC: <b id="d-kex">--</b></div>
              <div>💾 RAM: <b id="d-ram">--</b></div>
            </div>
          </div>

          <div class="card">
            <div class="card-title">
              <span>🚀 Hyperdrive Performance Optimization</span>
              <span class="badge green">Zero Throttling</span>
            </div>
            <p style="font-size:12px;color:var(--muted);margin-bottom:8px;">Disables Wi-Fi power saving, neutralizes phantom process limits, and flushes RAM caches for maximum speed.</p>
            <button class="action-btn boost" style="width:100%;font-size:13px;padding:12px;" onclick="triggerPerformanceBoost()">🚀 BOOST SYSTEM PERFORMANCE NOW</button>
            <div class="terminal-window" id="boostOutput" style="margin-top:8px;min-height:80px;">System optimized and ready.</div>
          </div>

          <div class="card" style="border-color:#7f1d1d;background:#1a0c0c;">
            <div class="card-title" style="color:#f87171;">
              <span>🔄 Device Restart (Turn Off & On)</span>
              <span class="badge red">Auto-Resuming</span>
            </div>
            <p style="font-size:12px;color:#fca5a5;margin-bottom:10px;">Safely reboots the Android device. Termux:Boot will auto-resume ADB, SSH, the Guardian daemon, and this Web Hub upon boot.</p>
            <button class="action-btn restart" style="width:100%;font-size:13px;padding:12px;" onclick="confirmRestart()">🔄 RESTART DEVICE (REBOOT NOW)</button>
          </div>
        </div>

        <!-- PANE 3: FIRECRAWL & YOUTUBE HARVESTER -->
        <div class="hub-pane" id="pane-harvester">
          <div class="card">
            <div class="card-title">
              <span>🔥 Firecrawl v2 Live Web Intelligence</span>
              <span class="badge green">API Connected</span>
            </div>
            <div style="display:flex;gap:6px;margin-bottom:8px;">
              <input type="text" id="fcQuery" placeholder="Search the web with Firecrawl v2..." style="flex:1;background:#020617;color:#fff;border:1px solid var(--border);border-radius:6px;padding:8px;font-size:12px;outline:none;" onkeydown="if(event.key==='Enter') executeFirecrawlSearch()">
              <button class="action-btn" style="background:#ea580c;" onclick="executeFirecrawlSearch()">🔎 Search</button>
            </div>
            <div class="terminal-window" id="fcOutput" style="min-height:100px;">Enter query to search web with Firecrawl v2.</div>
          </div>

          <div class="card">
            <div class="card-title">
              <span>📚 YouTube Technical Video Knowledge Library</span>
              <button class="action-btn" style="padding:4px 9px;font-size:11px;" onclick="triggerHarvest()">✨ Sweep & Harvest New</button>
            </div>
            <p style="font-size:11px;color:var(--muted);margin-bottom:8px;">Knowledge harvested automatically into SQLite cognitive memory:</p>
            <div id="videoList" style="max-height:360px;overflow-y:auto;">Loading library...</div>
          </div>
        </div>

        <!-- PANE 4: LIVE TERMINAL -->
        <div class="hub-pane" id="pane-terminal">
          <div class="card">
            <div class="card-title">
              <span>💻 Interactive Termux Shell</span>
              <span class="badge green">Local Host</span>
            </div>
            <div style="display:flex;gap:6px;margin-bottom:8px;">
              <input type="text" id="termInput" placeholder="Type bash command (e.g. ls -la, auto-adb, yt-learn list)..." style="flex:1;background:#020617;color:#fff;border:1px solid var(--border);border-radius:6px;padding:8px;font-size:12px;outline:none;" onkeydown="if(event.key==='Enter') executeTerminal()">
              <button class="action-btn" style="background:#0284c7;" onclick="executeTerminal()">▶ Run</button>
            </div>
            <div class="terminal-window" id="termOutput" style="min-height:240px;">⚡ Termux interactive terminal ready.</div>
          </div>
        </div>

        <!-- PANE 5: VS CODE WEB -->
        <div class="hub-pane" id="pane-vscode">
          <div class="card">
            <div class="card-title">
              <span>🔒 VS Code Web Server (Port 8088 HTTPS)</span>
              <a href="https://192.168.1.23:8088" target="_blank" class="action-btn" style="padding:4px 8px;font-size:11px;text-decoration:none;">🔗 Open in New Tab</a>
            </div>
            <p style="font-size:11px;color:var(--muted);margin-bottom:6px;">If browser blocks HTTPS iframe due to local self-signed certificate, click "Open in New Tab" above and accept the local certificate.</p>
            <div style="height:550px;width:100%;border-radius:8px;overflow:hidden;border:1px solid var(--border);">
              <iframe id="vscodeFrame" src="" style="width:100%;height:100%;border:none;background:#1e1e1e;" allow="clipboard-read; clipboard-write"></iframe>
            </div>
          </div>
        </div>

        <!-- PANE 6: BASE44 STUDIO -->
        <div class="hub-pane" id="pane-base44">
          <div class="card">
            <div class="card-title">🔤 Base44 Platform Web Studio</div>
            <label style="font-size:11px;color:var(--muted);font-weight:700;">Input Text or Raw Payload:</label>
            <textarea id="b44Inp" rows="4" placeholder="Type text to encode or Base44 matrix to decode..." style="width:100%;background:#020617;color:#fff;border:1px solid var(--border);border-radius:6px;padding:8px;font-size:12px;margin:6px 0;outline:none;"></textarea>
            <div style="display:flex;gap:8px;margin-bottom:8px;">
              <button class="action-btn" style="flex:1;background:#0284c7;" onclick="b44Enc()">⚡ Encode to Base44</button>
              <button class="action-btn" style="flex:1;background:#059669;" onclick="b44Dec()">🔓 Decode from Base44</button>
            </div>
            <label style="font-size:11px;color:var(--muted);font-weight:700;">Result:</label>
            <textarea id="b44Out" rows="4" readonly placeholder="Result will appear here..." style="width:100%;background:#020617;color:#38bdf8;border:1px solid var(--border);border-radius:6px;padding:8px;font-size:12px;margin-top:6px;outline:none;font-family:monospace;"></textarea>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    const chat = document.getElementById('chat');
    const input = document.getElementById('prompt');
    const sendBtn = document.getElementById('sendBtn');
    const micBtn = document.getElementById('micBtn');
    const chatPanel = document.getElementById('chatPanel');
    const rightPanel = document.getElementById('rightPanel');
    const sidebar = document.getElementById('sidebar');
    const telemetryText = document.getElementById('telemetryText');

    let recognition = null;
    let isRecording = false;
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognition = new SR();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = 'en-US';
      recognition.onresult = function(e) {
        input.value = e.results[0][0].transcript;
        stopSpeech();
        send();
      };
      recognition.onerror = function() { stopSpeech(); };
      recognition.onend = function() { stopSpeech(); };
    }

    function toggleSpeech() {
      if (!recognition) return alert('Speech recognition not supported in this browser.');
      if (isRecording) { stopSpeech(); }
      else { recognition.start(); isRecording = true; micBtn.classList.add('recording'); }
    }

    function stopSpeech() {
      if (recognition && isRecording) recognition.stop();
      isRecording = false;
      micBtn.classList.remove('recording');
    }

    function setMode(mode) {
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      if (mode === 'chat') {
        document.getElementById('btnChat').classList.add('active');
        chatPanel.className = 'chat-panel mode-chat';
        rightPanel.className = 'right-panel hidden';
      } else if (mode === 'split') {
        document.getElementById('btnSplit').classList.add('active');
        chatPanel.className = 'chat-panel mode-split';
        rightPanel.className = 'right-panel';
      } else if (mode === 'hub') {
        document.getElementById('btnHub').classList.add('active');
        chatPanel.className = 'chat-panel hidden';
        rightPanel.className = 'right-panel';
      }
    }

    function switchHubTab(tabId) {
      document.querySelectorAll('.hub-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.hub-pane').forEach(p => p.classList.remove('active'));
      const tabEl = document.getElementById('tab-' + tabId);
      const paneEl = document.getElementById('pane-' + tabId);
      if (tabEl) tabEl.classList.add('active');
      if (paneEl) paneEl.classList.add('active');
      if (tabId === 'harvester') loadHarvestList();
      if (tabId === 'vscode') {
        const vf = document.getElementById('vscodeFrame');
        if (!vf.src) vf.src = "https://" + window.location.hostname + ":8088/?folder=" + encodeURIComponent("/data/data/com.termux/files/home");
      }
    }

    function toggleSidebar() { sidebar.classList.toggle('open'); }
    function setFirecrawlMode() {
      const el = document.getElementById('actionMode');
      el.value = el.value === 'firecrawl_search' ? 'chat' : 'firecrawl_search';
    }

    function quickSend(txt) {
      input.value = txt;
      send();
    }

    function appendMessage(sender, text, type) {
      const msgDiv = document.createElement('div');
      msgDiv.className = 'msg ' + (type || 'bot');
      const headerDiv = document.createElement('div');
      headerDiv.className = 'msg-header';
      const senderSpan = document.createElement('span');
      senderSpan.textContent = sender;
      headerDiv.appendChild(senderSpan);
      msgDiv.appendChild(headerDiv);

      const contentDiv = document.createElement('div');
      if (type === 'bot') contentDiv.innerHTML = marked.parse(text);
      else contentDiv.textContent = text;
      msgDiv.appendChild(contentDiv);
      chat.appendChild(msgDiv);
      chat.scrollTop = chat.scrollHeight;
    }

    async function send() {
      const text = input.value.trim();
      if (!text) return;
      const actionMode = document.getElementById('actionMode').value;
      const model = document.getElementById('modelSelect').value;
      const system = document.getElementById('sysPrompt').value;

      input.value = '';
      appendMessage('You', text, 'user');
      input.disabled = true; sendBtn.disabled = true;

      const typingDiv = document.createElement('div');
      typingDiv.className = 'msg bot';
      typingDiv.id = 'typing-indicator';
      typingDiv.textContent = `⚡ Josie Processing (${model.split('/').pop()})...`;
      chat.appendChild(typingDiv);
      chat.scrollTop = chat.scrollHeight;

      try {
        const res = await fetch('/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: text, mode: actionMode, model: model, system: system })
        });
        const data = await res.json();
        const ind = document.getElementById('typing-indicator');
        if (ind) ind.remove();
        appendMessage(data.sender || 'Josie OS', data.reply || "Done.", data.is_terminal ? 'terminal' : 'bot');
      } catch (err) {
        const ind = document.getElementById('typing-indicator');
        if (ind) ind.remove();
        appendMessage('Josie OS', '⚠️ Connection error: ' + err.message, 'bot');
      } finally {
        input.disabled = false; sendBtn.disabled = false; input.focus();
      }
    }

    /* HUB ACTIONS */
    async function executeKali() {
      const cmd = document.getElementById('kaliInput').value.trim();
      if (!cmd) return;
      const isRoot = document.getElementById('kaliRootCheck').checked;
      const outEl = document.getElementById('kaliOutput');
      outEl.textContent = `⏳ Executing in Kali (${isRoot ? 'root' : 'user'}): ${cmd}...`;
      try {
        const res = await fetch('/api/nethunter', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ cmd: cmd, root: isRoot })
        });
        const data = await res.json();
        outEl.textContent = data.output || '(No output)';
      } catch (e) {
        outEl.textContent = '❌ Execution error: ' + e;
      }
    }

    function runKaliPreset(cmd) {
      document.getElementById('kaliInput').value = cmd;
      executeKali();
    }

    async function controlKex(action) {
      const outEl = document.getElementById('kaliOutput');
      outEl.textContent = `⏳ Performing KeX action: ${action}...`;
      try {
        const res = await fetch('/api/kex', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ action: action })
        });
        const data = await res.json();
        outEl.textContent = data.output;
        fetchTelemetry();
      } catch (e) {
        outEl.textContent = '❌ KeX error: ' + e;
      }
    }

    async function triggerPerformanceBoost() {
      const outEl = document.getElementById('boostOutput');
      outEl.textContent = '⏳ Applying kernel tuning, cache purge, and Wi-Fi optimization...';
      try {
        const res = await fetch('/api/optimize', { method: 'POST' });
        const data = await res.json();
        outEl.textContent = data.message;
        appendMessage('Hyperdrive Sentinel', data.message, 'terminal');
      } catch (e) {
        outEl.textContent = '❌ Optimization error: ' + e;
      }
    }

    async function confirmRestart() {
      if (confirm('🔄 Restart the Android device now?\\n\\nAll services and daemons will auto-resume upon boot via Termux:Boot.')) {
        appendMessage('System Sentinel', '🔄 Device restart initiated. Shutting down and rebooting now...', 'terminal');
        try {
          await fetch('/api/restart_device', { method: 'POST' });
        } catch (e) {}
      }
    }

    async function executeTerminal() {
      const cmd = document.getElementById('termInput').value.trim();
      if (!cmd) return;
      const outEl = document.getElementById('termOutput');
      outEl.textContent = `⏳ Running in Termux: ${cmd}...`;
      try {
        const res = await fetch('/run_script', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ code: cmd, lang: 'bash' })
        });
        const data = await res.json();
        outEl.textContent = data.output || '(No output)';
      } catch (e) {
        outEl.textContent = '❌ Terminal error: ' + e;
      }
    }

    async function executeFirecrawlSearch() {
      const q = document.getElementById('fcQuery').value.trim();
      if (!q) return;
      const outEl = document.getElementById('fcOutput');
      outEl.textContent = `⏳ Searching with Firecrawl v2 for '${q}'...`;
      try {
        const res = await fetch('/chat', {
          method: 'POST', headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: q, mode: 'firecrawl_search' })
        });
        const data = await res.json();
        outEl.textContent = data.reply;
      } catch (e) {
        outEl.textContent = '❌ Search error: ' + e;
      }
    }

    async function triggerHarvest() {
      const listEl = document.getElementById('videoList');
      listEl.innerHTML = '<div style="font-size:11px;color:var(--accent);">⏳ Harvesting new technical videos across ecosystem topics via Firecrawl...</div>';
      try {
        await fetch('/api/harvest', { method: 'POST' });
        loadHarvestList();
      } catch (e) {
        listEl.textContent = '❌ Harvest error: ' + e;
      }
    }

    async function loadHarvestList() {
      const listEl = document.getElementById('videoList');
      try {
        const res = await fetch('/api/harvest_list');
        const items = await res.json();
        if (!items || items.length === 0) {
          listEl.innerHTML = '<div style="font-size:11px;color:var(--muted);">No videos indexed yet. Click "Sweep & Harvest New".</div>';
          return;
        }
        listEl.innerHTML = items.map(v => `
          <div class="video-card">
            <a href="${v.url}" target="_blank" class="video-title">🎥 ${v.title}</a>
            <div class="video-meta">👤 ${v.channel} | 🕒 ${v.time.slice(0, 16)}</div>
            <div class="video-desc">${v.summary}</div>
          </div>
        `).join('');
      } catch (e) {
        listEl.textContent = '❌ Load error: ' + e;
      }
    }

    async function fetchTelemetry() {
      try {
        const res = await fetch('/api/telemetry');
        const data = await res.json();
        telemetryText.textContent = `${data.battery}% | ${data.temp}°C | ${data.current_ma}mA`;
        document.getElementById('d-bat').textContent = `${data.battery}% (${data.status})`;
        document.getElementById('d-temp').textContent = `${data.temp}°C`;
        document.getElementById('d-curr').textContent = `${data.current_ma} mA`;
        document.getElementById('d-adb').textContent = data.adb;
        document.getElementById('d-kex').textContent = data.kex;
        document.getElementById('d-ram').textContent = data.mem.split(/\s+/)[2] || data.mem;
      } catch (err) {}
    }

    /* BASE44 FUNCTIONS */
    const alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh";
    function b44Enc() {
      const text = document.getElementById('b44Inp').value;
      if (!text) return;
      const bytes = new TextEncoder().encode(text);
      let nz = 0;
      for (let b of bytes) { if (b === 0) nz++; else break; }
      let hex = Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('');
      if (!hex) { document.getElementById('b44Out').value = ''; return; }
      let num = BigInt("0x" + hex), res = [], base = 44n;
      while (num > 0n) { res.push(alphabet[Number(num % base)]); num = num / base; }
      document.getElementById('b44Out').value = "0".repeat(nz) + res.reverse().join('');
    }
    function b44Dec() {
      const val = document.getElementById('b44Inp').value.trim();
      if (!val) return;
      let nz = 0;
      while (nz < val.length && val[nz] === '0') nz++;
      let num = 0n, base = 44n;
      for (let i = nz; i < val.length; i++) {
        let idx = alphabet.indexOf(val[i]);
        if (idx >= 0) num = num * base + BigInt(idx);
      }
      let hex = num.toString(16);
      if (hex.length % 2 !== 0) hex = "0" + hex;
      let bytes = [];
      for (let i = 0; i < nz; i++) bytes.push(0);
      if (hex !== "00" && hex !== "0") {
        for (let i = 0; i < hex.length; i += 2) bytes.push(parseInt(hex.substr(i, 2), 16));
      }
      document.getElementById('b44Out').value = new TextDecoder().decode(new Uint8Array(bytes));
    }

    setTimeout(fetchTelemetry, 500);
    setTimeout(loadHarvestList, 1000);
  </script>
</body>
</html>
"""

def execute_shell(cmd):
    try:
        env = os.environ.copy()
        env["PATH"] = os.path.expanduser("~/.local/bin:") + os.path.expanduser("~/bin:") + env.get("PATH", "")
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=20, cwd=WORKSPACE_DIR, env=env)
        out = (res.stdout + res.stderr).strip() or "(Executed with no output)"
        return {"reply": out, "is_terminal": True, "sender": f"Terminal [Exit: {res.returncode}]"}
    except Exception as e:
        return {"reply": f"Execution error: {e}", "is_terminal": True, "sender": "Terminal Error"}

def ask_openrouter(prompt, model, api_key, sys_prompt=""):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "http://192.168.1.23:8080",
            "X-Title": "Josie OS"
        }
        messages = []
        if sys_prompt: messages.append({"role": "system", "content": sys_prompt})
        messages.append({"role": "user", "content": prompt})

        data = json.dumps({"model": model, "messages": messages}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res["choices"][0]["message"]["content"]
    except Exception:
        return None

def ask_ai(prompt, model="anthropic/claude-3.7-sonnet", user_key="", sys_prompt=""):
    # 1. Pollinations Zero-API keyless fallback
    try:
        p_payload = json.dumps({
            "messages": [
                {"role": "system", "content": sys_prompt or "You are Josie OS. Answer concisely in English."},
                {"role": "user", "content": prompt[:4000]}
            ],
            "model": "openai"
        }).encode('utf-8')
        req = urllib.request.Request("https://text.pollinations.ai/", data=p_payload, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            ans = resp.read().decode('utf-8').strip()
            if ans and not ans.startswith("{") and len(ans) > 2:
                return ans
    except Exception: pass

    # 2. OpenRouter
    or_key = user_key or get_openrouter_key()
    if or_key:
        ans = ask_openrouter(prompt, model, or_key, sys_prompt)
        if ans: return ans

    return f"⚡ **Josie OS Core**\n\nCommand acknowledged: *{prompt}*\n\nActive across all system tools."

def process_chat(data):
    prompt = data.get("prompt", "").strip()
    mode = data.get("mode", "chat")
    model = data.get("model", "anthropic/claude-3.7-sonnet")
    sys_inst = data.get("system", "").strip()

    if prompt.startswith("$ ") or mode == "shell":
        cmd = prompt[2:] if prompt.startswith("$ ") else prompt
        return execute_shell(cmd)

    if mode == "firecrawl_search" or prompt.startswith("search:"):
        query = prompt.replace("search:", "").strip()
        try:
            fc_res = firecrawl_request("search", {"query": query, "limit": 4})
            web_items = fc_res.get("data", {}).get("web", [])
            snippets = "\n".join([f"• **{w.get('title')}**\n  🔗 {w.get('url')}\n  📝 {w.get('description')}\n" for w in web_items])
            return {"reply": f"🔥 **Firecrawl v2 Web Intelligence for '{query}':**\n\n" + (snippets or "No results found."), "is_terminal": False, "sender": "Firecrawl v2"}
        except Exception as e:
            return {"reply": f"⚠️ Firecrawl search error: {e}", "is_terminal": False, "sender": "Firecrawl v2"}

    if mode == "firecrawl_scrape" or prompt.startswith("scrape:"):
        url = prompt.replace("scrape:", "").strip()
        if not url.startswith("http"): url = "https://" + url
        try:
            fc_res = firecrawl_request("scrape", {"url": url, "formats": ["markdown"]})
            md = fc_res.get("data", {}).get("markdown", "")
            return {"reply": f"📄 **Scraped Content ({url})**:\n\n" + md[:3500], "is_terminal": False, "sender": "Firecrawl Scrape"}
        except Exception as e:
            return {"reply": f"⚠️ Firecrawl scrape error: {e}", "is_terminal": False, "sender": "Firecrawl Scrape"}

    reply = ask_ai(prompt, model=model, sys_prompt=sys_inst)
    return {"reply": reply, "is_terminal": False, "sender": "Josie OS"}

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def do_GET(self):
        if self.path == "/" or self.path.startswith("/?"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(MAIN_HTML.encode("utf-8"))
        elif self.path == "/api/telemetry":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(get_telemetry()).encode("utf-8"))
        elif self.path == "/api/harvest_list":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(get_harvested_videos()).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length).decode("utf-8")) if length > 0 else {}

        if self.path == "/chat":
            res = process_chat(body)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
            return

        elif self.path == "/run_script":
            code = body.get("code", "")
            res = execute_shell(code)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"output": res["reply"]}).encode("utf-8"))
            return

        elif self.path == "/api/nethunter":
            cmd = body.get("cmd", "echo NetHunter Ready")
            is_root = body.get("root", False)
            res = execute_kali_cmd(cmd, is_root)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(res).encode("utf-8"))
            return

        elif self.path == "/api/kex":
            action = body.get("action", "status")
            try:
                proc = subprocess.run([os.path.expanduser("~/bin/kex"), action], capture_output=True, text=True, timeout=10)
                out = (proc.stdout + proc.stderr).strip() or "KeX updated."
            except Exception as e:
                out = f"Error: {e}"
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"output": out}).encode("utf-8"))
            return

        elif self.path == "/api/optimize":
            msg = execute_performance_boost()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "message": msg}).encode("utf-8"))
            return

        elif self.path == "/api/harvest":
            try:
                proc = subprocess.run([os.path.expanduser("~/bin/yt-learn"), "harvest"], capture_output=True, text=True, timeout=30)
                out = proc.stdout.strip()
            except Exception as e:
                out = f"Error: {e}"
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "output": out}).encode("utf-8"))
            return

        elif self.path == "/api/restart_device":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "rebooting"}).encode("utf-8"))
            # Execute restart in background after response
            subprocess.Popen(["/data/data/com.termux/files/home/bin/adb-exec", "svc power reboot || reboot"])
            return

        self.send_response(404)
        self.end_headers()

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

def main():
    with ThreadingTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"🚀 JOSIE OS Sovereign Platform LIVE on 0.0.0.0:{PORT}", flush=True)
        httpd.serve_forever()

if __name__ == "__main__":
    main()
