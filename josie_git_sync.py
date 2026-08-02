#!/data/data/com.termux/files/usr/bin/python3
import os
import subprocess
import time

ROOT = os.path.expanduser("~/josie_core")
LOG = os.path.join(ROOT, "execution.log")

def log_action(stage, msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [GIT_{stage}] {msg}\n"
    print(line, end="")
    try:
        with open(LOG, "a") as f:
            f.write(line)
    except Exception:
        pass

def push_repository():
    os.chdir(ROOT)
    log_action("SYNC", "Checking repository status for changes...")
    
    # Check for untracked or modified files
    status_res = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if not status_res.stdout.strip():
        log_action("SYNC", "Repository is already clean. No changes to push.")
        return

    log_action("STAGE", "Staging all local workspace changes...")
    subprocess.run("git add .", shell=True, capture_output=True)

    commit_msg = f"Autonomous update: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    log_action("COMMIT", f"Committing with message: '{commit_msg}'")
    subprocess.run(f"git commit -m '{commit_msg}'", shell=True, capture_output=True)

    log_action("PUSH", "Pushing updates to remote repository...")
    push_res = subprocess.run("git push origin main || git push origin master", shell=True, capture_output=True, text=True)
    
    if push_res.returncode == 0:
        log_action("SUCCESS", "Repository successfully synchronized and pushed.")
    else:
        log_action("CRASH", f"Push failed: {push_res.stderr.strip()}")

if __name__ == "__main__":
    push_repository()

# Active @Josie Universal Handle Enforced
