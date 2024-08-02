import win32gui
import win32api
import win32con
import time
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
type = config.get("main", "type")
x = int(config.get("main", "xCoord"))
y = int(config.get("main", "yCoord"))
delay = float(config.get("main", "delay"))
WindowName = config.get("main", "windowName")


def click():
    hWnd = win32gui.FindWindow(None, WindowName)
    lParam = win32api.MAKELONG(x, y)
    if (type == "right"):
        win32api.SendMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
        win32api.SendMessage(hWnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, lParam)
    elif (type == "left"):
        win32api.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.SendMessage(hWnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
    else:
        print("Wrong mouse button(type). Use: left, right")
        exit()
    print(f"Clicked! Time: " + str(datetime.now()).split(" ")[1])


while True:
    click()
    time.sleep(delay)
