import pyautogui as pa 
import random 
import keyboard
import os
import time
import sys

## tamaño de
## print(pa.size())

## captura posicion de mouse actual
## print(pa.position())
time.sleep(5)

while True:
    pa.moveTo(x=random.randint(10,1920), y =random.randint(10,1080) )
    print(pa.position())
    if keyboard.is_pressed('e'):
        break
        sys.exit()
