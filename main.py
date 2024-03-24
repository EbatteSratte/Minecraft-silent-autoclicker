import win32gui
import win32api
import win32con
import time
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


def click(x, y, type):
    hWnd = win32gui.FindWindow(None, config.get("main", "windowName"))
    lParam = win32api.MAKELONG(x, y)
    if (type == "right"):
        win32api.SendMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
        win32api.SendMessage(hWnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, lParam)
    elif (type == "left"):
        win32api.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        win32api.SendMessage(hWnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
    print(f"Clicked! Time: " + str(datetime.now()).split(" ")[1])


while True:
    click(int(config.get("main", "xCoord")), int(config.get("main", "yCoord")), config.get("main", "type"))
    time.sleep(int(config.get("main", "delay")))
