#!/data/data/com.termux/files/usr/bin/python3
import os
import subprocess
import time

ROOT = os.path.expanduser("~/josie_core")
STATE = os.path.join(ROOT, "omni_state")
LOG = os.path.join(ROOT, "execution.log")
SHARED_STORAGE = os.path.expanduser("~/storage/shared")

os.makedirs(STATE, exist_ok=True)

def record_omni(stage, msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [OMNI_{stage}] {msg}\n"
    print(line, end="")
    try:
        with open(LOG, "a") as f:
            f.write(line)
    except Exception:
        pass

def execute_omni_pull():
    record_omni("START", "Initiating total omni-pull harvest across all system and storage layers...")

    # 1. Termux Environment & Package Extraction
    try:
        with open(os.path.join(STATE, "termux_packages.txt"), "w") as f:
            subprocess.run(["pkg", "list-installed"], stdout=f, stderr=subprocess.DEVNULL)
        with open(os.path.join(STATE, "termux_env.txt"), "w") as f:
            subprocess.run(["env"], stdout=f, stderr=subprocess.DEVNULL)
    except Exception as e:
        record_omni("ERROR", f"Termux extraction error: {e}")

    # 2. Rish / ADB System-Wide Telemetry & Package Dump
    try:
        res_pkg = subprocess.run("rish -c 'pm list packages -f'", shell=True, capture_output=True, text=True)
        with open(os.path.join(STATE, "android_packages.txt"), "w") as f:
            f.write(res_pkg.stdout)

        res_settings = subprocess.run("rish -c 'settings list global'", shell=True, capture_output=True, text=True)
        with open(os.path.join(STATE, "android_settings_global.txt"), "w") as f:
            f.write(res_settings.stdout)

        res_input = subprocess.run("rish -c 'dumpsys input_method'", shell=True, capture_output=True, text=True)
        with open(os.path.join(STATE, "android_input_method.txt"), "w") as f:
            f.write(res_input.stdout)
    except Exception as e:
        record_omni("ERROR", f"Rish telemetry error: {e}")

    # 3. Shared Storage Indexing (Nothing Left Behind)
    if os.path.exists(SHARED_STORAGE):
        try:
            res_storage = subprocess.run(f"find '{SHARED_STORAGE}' -maxdepth 3 -type f", shell=True, capture_output=True, text=True)
            with open(os.path.join(STATE, "shared_storage_index.txt"), "w") as f:
                f.write(res_storage.stdout)
        except Exception as e:
            record_omni("ERROR", f"Storage indexing error: {e}")

    # 4. Universal @Josie Handle & Namespace Enforcement
    record_omni("NORMALIZE", "Enforcing universal @Josie handles across all workspace files...")
    count = 0
    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith((".py", ".zsh", ".txt", ".sh", ".md")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    if "@josie" not in content.lower():
                        content += "\n# @Josie Omni-Pull Sovereign Anchor Enforced\n"
                        with open(path, "w", encoding="utf-8") as f:
                            f.write(content)
                        count += 1
                except Exception:
                    pass
    record_omni("NORMALIZE", f"Updated {count} files with @Josie sovereign identifiers.")

    # 5. Git Automation: Stage, Commit, and Push
    os.chdir(ROOT)
    record_omni("GIT", "Staging all harvested assets and repository updates...")
    subprocess.run("git add .", shell=True, capture_output=True)

    commit_msg = f"Omni-pull complete & synchronized: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    record_omni("GIT", f"Committing changes: '{commit_msg}'")
    subprocess.run(f"git commit -m '{commit_msg}'", shell=True, capture_output=True)

    record_omni("GIT", "Pushing repository state to remote origin...")
    push_res = subprocess.run("git push origin main || git push origin master", shell=True, capture_output=True, text=True)

    if push_res.returncode == 0:
        record_omni("SUCCESS", "Omni-pull executed, normalized, and successfully pushed.")
    else:
        record_omni("CRASH", f"Push output: {push_res.stderr.strip()}")

if __name__ == "__main__":
    execute_omni_pull()
