import pyautogui as pag
import random
import time


try:
    while True:
        x = random.randint(0, 1919)
        y = random.randint(0, 1079)
        pag.moveTo(x, y, 0.5)
        # pag.click()
        # time.sleep(2)
        pag.sleep(2)
except KeyboardInterrupt:
    print("exit")
