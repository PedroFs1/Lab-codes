from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog

#creating and hiding tkinter window
root = tk.Tk()
root.withdraw()

source = Path(filedialog.askdirectory(title="Pasta principal:"))

#Apagando metadata/campo claro
#Para apagar campo claro, adicionar pattern [..., "c0x0"], se houver
patterns = ["*.xml"]
for pattern in patterns:
    for file in source.rglob(pattern):
        print("deleting:", file)
        file.unlink()

#movendo imagens
#Alterar aqui as pastas e grupos usados no experimento. c1x0 = laser 1...
channels = {
    "c1x0": "DAPI",
    "c2x0": "ORO",
    "c3x0": "GFP"
}
#o script considera as pastas no formato "pasta escolhida/pasta grupos/pastas fotos/fotos
for pattern, folder_name in channels.items():
    for files in sorted(source.rglob(f"*{pattern}*")):
        if folder_name in files.parts:
            continue

        pasta_laser = files.parents[1] / folder_name
        pasta_laser.mkdir(exist_ok=True)
        files.rename(pasta_laser / files.name)
