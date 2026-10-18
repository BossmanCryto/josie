#!/data/data/com.termux/files/usr/bin/python3
import os
import subprocess
import time

ROOT = os.path.expanduser("~/josie_core")
STATE = os.path.join(ROOT, "state")
LOG = os.path.join(ROOT, "execution.log")

os.makedirs(STATE, exist_ok=True)

def log_total(action, msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [TOTAL_{action}] {msg}\n"
    print(line, end="")
    try:
        with open(LOG, "a") as f:
            f.write(line)
    except Exception:
        pass

def activate_and_push():
    log_total("SCAN", "Scanning all Termux files, environments, and core assets...")
    
    # 1. Capture comprehensive environment & package state
    try:
        env_res = subprocess.run("env", shell=True, capture_output=True, text=True)
        with open(os.path.join(STATE, "termux_env.txt"), "w") as f:
            f.write(env_res.stdout)
            
        pkg_res = subprocess.run("pkg list-installed", shell=True, capture_output=True, text=True)
        with open(os.path.join(STATE, "termux_installed_packages.txt"), "w") as f:
            f.write(pkg_res.stdout)
    except Exception as e:
        log_total("ERROR", str(e))

    # 2. Universal '@' handle activation & normalization across all workspace files
    log_total("ACTIVATE", "Activating universal '@' handles and mapping all local files...")
    count = 0
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith((".py", ".zsh", ".txt", ".sh", ".md")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    if "@josie" not in content.lower():
                        content += "\n# Active @Josie Universal Handle Enforced\n"
                        with open(path, "w", encoding="utf-8") as f:
                            f.write(content)
                        count += 1
                except Exception:
                    pass
    log_total("ACTIVATE", f"Activated universal handles across {count} workspace files.")

    # 3. Git Stage, Commit, and Push
    os.chdir(ROOT)
    log_total("GIT", "Staging all changes...")
    subprocess.run("git add .", shell=True, capture_output=True)

    commit_msg = f"Universal activation and sync: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    log_total("GIT", f"Committing with message: '{commit_msg}'")
    subprocess.run(f"git commit -m '{commit_msg}'", shell=True, capture_output=True)

    log_total("GIT", "Pushing to remote repository...")
    push_res = subprocess.run("git push origin main || git push origin master", shell=True, capture_output=True, text=True)
    
    if push_res.returncode == 0:
        log_total("SUCCESS", "Universal push and synchronization completed successfully.")
    else:
        log_total("CRASH", f"Push output: {push_res.stderr.strip()}")

if __name__ == "__main__":
    activate_and_push()
