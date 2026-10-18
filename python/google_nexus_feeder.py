#!/data/data/com.termux/files/usr/bin/python3
import os
import time
import subprocess

ROOT = os.path.expanduser("~/josie_core")
STATE = os.path.join(ROOT, "state")
LOG = os.path.join(ROOT, "execution.log")
HUB = "/storage/emulated/0/Download/Josie Center Hub"

os.makedirs(STATE, exist_ok=True)

def record_nexus(stage, msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [NEXUS_{stage}] {msg}\n"
    print(line, end="")
    try:
        with open(LOG, "a") as f:
            f.write(line)
    except Exception:
        pass

def harvest_device_and_workspace():
    record_nexus("HARVEST", "Pulling telemetry and storage assets into core memory.")
    
    # Harvest package states and input methods via Rish
    try:
        subprocess.run("rish -c 'pm list packages -f' > " + os.path.join(STATE, "packages_nexus.txt"), shell=True, capture_output=True)
        subprocess.run("rish -c 'dumpsys input_method' > " + os.path.join(STATE, "input_nexus.txt"), shell=True, capture_output=True)
    except Exception:
        pass

    # Index local Hub files if present
    if os.path.exists(HUB):
        try:
            res = subprocess.run(f"find '{HUB}' -maxdepth 3 -type f", shell=True, capture_output=True, text=True)
            with open(os.path.join(STATE, "hub_index.txt"), "w") as f:
                f.write(res.stdout)
        except Exception:
            pass

    record_nexus("OPTIMIZE", "Data ingested and mapped. Autonomous agent parameters updated.")

if __name__ == "__main__":
    while True:
        try:
            harvest_device_and_workspace()
            time.sleep(300)
        except Exception as e:
            record_nexus("ERROR", str(e))
            time.sleep(30)

# Active @Josie Universal Handle Enforced
