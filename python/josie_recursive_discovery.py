#!/data/data/com.termux/files/usr/bin/python3
import os
import subprocess
import time

ROOT = os.path.expanduser("~/josie_core")
STATE = os.path.join(ROOT, "unexplored_state")
LOG = os.path.join(ROOT, "execution.log")

os.makedirs(STATE, exist_ok=True)

def log_discovery(stage, msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [DISCOVERY_{stage}] {msg}\n"
    print(line, end="")
    try:
        with open(LOG, "a") as f:
            f.write(line)
    except Exception:
        pass

def recursive_sweep():
    log_discovery("SWEEP", "Hunting for unmapped system spaces, hidden configs, and unknown variables...")
    
    # 1. Hunt for hidden databases, JSON configs, and asset files across storage
    try:
        db_files = subprocess.run("find /storage/emulated/0 -name '*.db' -o -name '*.json' 2>/dev/null | head -n 100", shell=True, capture_output=True, text=True)
        with open(os.path.join(STATE, "discovered_databases.txt"), "w") as f:
            f.write(db_files.stdout)
    except Exception as e:
        log_discovery("ERROR", f"Database scan error: {e}")

    # 2. Extract deep system properties and hardware nodes via rish
    try:
        props = subprocess.run("rish -c 'getprop'", shell=True, capture_output=True, text=True)
        with open(os.path.join(STATE, "system_properties.txt"), "w") as f:
            f.write(props.stdout)
    except Exception as e:
        log_discovery("ERROR", f"Property scan error: {e}")

    # 3. Enforce universal @Josie handles on all newly discovered data
    log_discovery("NORMALIZE", "Binding all discovered assets to the @Josie sovereign schema...")
    count = 0
    for root, dirs, files in os.walk(STATE):
        for file in files:
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                if "@josie" not in content.lower():
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content + "\n# @Josie Discovered Sovereign Node\n")
                    count += 1
            except Exception:
                pass

    # 4. Git Stage, Commit, and Push the newly discovered matrix
    os.chdir(ROOT)
    subprocess.run("git add .", shell=True, capture_output=True)
    subprocess.run(f"git commit -m 'Recursive discovery expansion: {time.strftime('%Y-%m-%d %H:%M:%S')}'", shell=True, capture_output=True)
    push_res = subprocess.run("git push origin main || git push origin master", shell=True, capture_output=True, text=True)

    if push_res.returncode == 0:
        log_discovery("SUCCESS", f"Recursive discovery complete. {count} nodes mapped and pushed live.")
    else:
        log_discovery("CRASH", f"Push output: {push_res.stderr.strip()}")

if __name__ == "__main__":
    recursive_sweep()
