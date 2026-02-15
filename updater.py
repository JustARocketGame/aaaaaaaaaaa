from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
import pyglet
import os

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

while True:
    MyRGB = RGB(randrange(255), randrange(255), randrange(255))
    brush = CreateSolidBrush(MyRGB)
    SelectObject(desk, brush)
    PatBlt(desk, 0, 0, x, y, PATINVERT)
    DeleteObject(brush)
    Sleep(1)