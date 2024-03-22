import os
import time
from pathlib import Path
import keyboard
import pyautogui
import pydirectinput

os.chdir('Images')


def run():
    for item in Path('.').glob('*'):
        if item.is_file():
            try:
                x, y = pyautogui.locateCenterOnScreen(str(item), confidence=0.8)
                print(x, y)
                pydirectinput.click(x, y)
                pydirectinput.moveTo(x-250, y-250)
                pyautogui.sleep(1)
            except pyautogui.ImageNotFoundException:
                pass


def main():
    time.sleep(1)
    status = 0
    while True:
        if keyboard.is_pressed('space'):
            status = 1
        elif keyboard.is_pressed('x'):
            status = 0
            print("Pause")
        elif keyboard.is_pressed('esc'):
            print("Stop")
            break
        elif status == 1:
            run()
        else:
            pass


main()
