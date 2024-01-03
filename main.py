import win32gui
import win32api
import win32con
import time
from datetime import datetime
#import pyautogui


def click(x,y):
    hWnd = win32gui.FindWindow(None, "Minecraft* 1.20.2 - Multiplayer (3rd-party Server)")
    lParam = win32api.MAKELONG(x, y)
    #клик
    win32api.SendMessage(hWnd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
    win32api.SendMessage(hWnd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, lParam)
    time.sleep(1)
    #temp = win32api.PostMessage(hWnd, win32con.WM_CHAR, 0x44, 0) #пишет букву
    print("Clicked! Time: " + str(datetime.now()).split(" ")[1])
while True:
    click(50, 50)
    time.sleep(25)
