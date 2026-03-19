from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog

#creating and hiding tkinter window
root = tk.Tk()
root.withdraw()

source = Path(filedialog.askdirectory(title="Pasta principal:"))

#Apagando metadata/campo claro
patterns = ["*c0x0*", "*.xml"]
for pattern in patterns:
    for file in source.rglob(pattern):
        print("deleting:", file)
        file.unlink()

#movendo imagens

channels = {
    "c1x0": "DAPI",
    "c2x0": "ORO",
    "c3x0": "GFP"
}

for pattern, folder_name in channels.items():
    for files in sorted(source.rglob(f"*{pattern}*")):
        if folder_name in files.parts:
            continue

        pasta_laser = files.parents[1] / folder_name
        pasta_laser.mkdir(exist_ok=True)
        files.rename(pasta_laser / files.name)