import win32gui
import win32api
import win32con
import time
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")


def click(x, y):
    hWnd = win32gui.FindWindow(None, "Minecraft* 1.20.2 - Multiplayer (3rd-party Server)")
    lParam = win32api.MAKELONG(x, y)
    win32api.SendMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
    win32api.SendMessage(hWnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, lParam)
    time.sleep(1)
    print(f"Clicked! Time: " + str(datetime.now()).split(" ")[1])


while True:
    click(int(config.get("main", "xCoord")), int(config.get("main", "yCoord")))
    time.sleep(int(config.get("main", "delay")))
