import pyautogui as pag
import time

print('start in 5 seconds')
time.sleep(5)

while True:
    pag.press('f5')
    pag.press('enter')
    time.sleep(2)
