import pyautogui as pg
import time

time.sleep(8)

for _ in range(50):
    pg.write('Hello')
    pg.press('enter')

