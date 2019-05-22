#! /usr/local/bin/python3

import pyautogui
import time
import random
from directkeys import PressKey, ReleaseKey, dk

g_dungeon = False
g_dungeonLobby = False

#Scan screen for enter dungeon button

def checkEnterButton():
    global g_dungeonLobby
    screenCapture = pyautogui.screenshot()
    yesButtonLocation = pyautogui.locateOnScreen('./static/images/yesbutton2.png')
    randomnumber1 = random.randint(1,3)
    time.sleep(randomnumber1)
    print (yesButtonLocation)
    if yesButtonLocation != None:
        time.sleep(randomnumber1)
        randomNumber2 = random.randint(0,10)
        g_dungeonLobby = not g_dungeonLobby
        if randomNumber2 > 4:
            pyautogui.click('./static/images/yesbutton2.png')
        else:
            PressKey(dk['RETURN'])
    else:
        print ("COULD NOT FIND DUNGEON ENTER BUTTON")
        return 
        
#Check if portal is opened

def checkDungeonPortal():
    dungeonName = pyautogui.locateOnScreen('./static/images/dungeon.png')
    randomnumber1 = random.randint(1,3)
    print (dungeonName)
    if dungeonName != None:
        PressKey(dk['RIGHT'])
        time.sleep(1.5)
        ReleaseKey(dk['RIGHT'])
        time.sleep(randomnumber1)
        PressKey(dk['GRAVE'])
        time.sleep(0.75)
        ReleaseKey(dk['GRAVE'])            
    else:
        return

def checkActionKey():
    actionKeyCheck = pyautogui.locateAllOnScreen('./static/images/actionkey.png')
    if actionKeyCheck != None:
        PressKey(dk['GRAVE'])
        time.sleep(0.75)
        ReleaseKey(dk['GRAVE'])
    else:
        return   


time.sleep(5)
#checkEnterButton()
checkDungeonPortal()
#Press Enter Key if Dungeon Dialog exists



# print ("pressing right key")
# time.sleep(5)

# PressKey(dk['1'])
# time.sleep(5)
# ReleaseKey(dk['1'])