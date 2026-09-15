#!/data/data/com.termux/files/usr/bin/env python3
import sys, json
print(json.dumps({"runtime": "python", "status": "active", "args": sys.argv[1:]}))
