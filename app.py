#! /usr/local/bin/python3

import pyautogui
import time
from directkeys import PressKey, ReleaseKey, dk


#Scan screen for enter dungeon button

def checkEnterButton():
    screenCapture = pyautogui.screenshot()

#Press Enter Key if Dungeon Dialog exists



print ("pressing right key")
time.sleep(5)

PressKey(dk['1'])
time.sleep(5)
ReleaseKey(dk['1'])