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

# while True:
#     pa.moveTo(x=random.randint(10,1920), y =random.randint(10,1080) )
#     print(pa.position())
#     if keyboard.is_pressed('e'):
#         break
#         sys.exit()
pa.moveTo(x=random.randint(10,1920), y =random.randint(10,1080) )

while True:

    pa.moveTo(300,200)
    pa.doubleClick(button="right")
    pa.moveTo(600,900)
    pa.doubleClick(button="right")

    if keyboard.is_pressed('e'):
        break
        sys.exit()
