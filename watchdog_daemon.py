#!/data/data/com.termux/files/usr/bin/python3
import sys
import time
import subprocess
import re
import os
import shlex

VALID_TOOLS = [
    "agy", "gemini", "adb", "rish", 
    "termux-wake-lock", "termux-battery-status", "termux-clipboard-get",
    "git", "python", "python3", "bash", "sh", "grep", "cat", "ls", "pip"
]

QUEUE_FILE = os.path.expanduser("~/watchdog_queue.txt")
LOG_FILE = os.path.expanduser("~/watchdog_debug.log")

def write_log(stage, message):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    formatted = f"[{timestamp}] [{stage}] {message}\n"
    print(formatted, end="")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(formatted)
    except Exception:
        pass

def clean_and_parse(raw_input):
    if not raw_input.strip():
        return ""
    
    tokens = raw_input.split()
    trimmed = tokens[:-2] if len(tokens) > 2 else tokens
    intermediate = " ".join(trimmed)

    cleaned = re.sub(r'\b(uh|um|like|ah|eh|er)\b', '', intermediate, flags=re.IGNORECASE)
    cleaned = re.sub(r'[%$#@*]+', '', cleaned)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def validate_command(cleaned):
    if not cleaned:
        return False, "Empty after cleaning."
    try:
        tokens = shlex.split(cleaned)
        first_word = tokens[0] if tokens else ""
    except Exception as e:
        return False, str(e)

    is_authorized = any(first_word.startswith(tool) for tool in VALID_TOOLS)
    if not is_authorized:
        return False, f"Unauthorized target: '{first_word}'"
    return True, cleaned

def execute_command(command):
    write_log("EXECUTING", f"Running real-time action -> {command}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            print(f"\n[STDOUT RESULT]:\n{result.stdout.strip()}\n")
            write_log("STDOUT", result.stdout.strip())

        if result.returncode != 0:
            err_text = result.stderr.strip() if result.stderr else "Exit non-zero"
            print(f"\n[CRASH/ERROR]:\n{err_text}\n", file=sys.stderr)
            write_log("CRASH", err_text)
        else:
            if result.stderr:
                print(result.stderr, file=sys.stderr)
            write_log("SUCCESS", "Command completed successfully.")

    except Exception as e:
        write_log("EXCEPTION", str(e))

def process_stream(raw_input):
    cleaned = clean_and_parse(raw_input)
    is_valid, msg = validate_command(cleaned)
    if is_valid:
        execute_command(msg)
    else:
        write_log("BLOCKED", msg)

def run_autonomous_engine():
    write_log("DAEMON", "Unified autonomous engine active with live screen feedback.")
    if not os.path.exists(QUEUE_FILE):
        open(QUEUE_FILE, "w").close()

    last_clipboard = ""

    while True:
        try:
            if os.path.exists(QUEUE_FILE):
                with open(QUEUE_FILE, "r") as f:
                    content = f.read().strip()
                if content:
                    with open(QUEUE_FILE, "w") as f:
                        f.write("")
                    process_stream(content)

            try:
                clip_res = subprocess.run(["termux-clipboard-get"], capture_output=True, text=True, timeout=1)
                clip_txt = clip_res.stdout.strip() if clip_res.stdout else ""
                if clip_txt and clip_txt != last_clipboard:
                    last_clipboard = clip_txt
            except Exception:
                pass

            time.sleep(0.3)
        except KeyboardInterrupt:
            break
        except Exception as e:
            write_log("DAEMON_ERROR", str(e))
            time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--run":
        process_stream(" ".join(sys.argv[2:]))
    else:
        run_autonomous_engine()
