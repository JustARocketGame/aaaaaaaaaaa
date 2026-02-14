import ctypes
import time

# Константы для Windows API
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
MONITOR_OFF = 2
MONITOR_ON = -1

def set_monitor_state(state):
    """Управление питанием монитора"""
    ctypes.windll.user32.SendMessageW(0xFFFF, WM_SYSCOMMAND, SC_MONITORPOWER, state)

# Выключить монитор
set_monitor_state(MONITOR_OFF)
print("Монитор выключен")

# Подождать 5 секунд
time.sleep(5)

# Включить монитор
set_monitor_state(MONITOR_ON)
print("Монитор включен")