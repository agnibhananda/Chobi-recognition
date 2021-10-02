from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position X: 628   Y:400
#Tile 2 Position X: 740   Y:400
#Tile 3 Position X: 851   Y:400
#Tile 4 Position X: 966   Y:400

def click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01) #pauses the script for 0.01 seconds
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
