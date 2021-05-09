import pyautogui as pag
import time
from colorama import Fore, Back, Style

refresh_frequency = int(
    input(Fore.BLACK + Back.WHITE + 'refresh frequency:' + Style.RESET_ALL + ' '))

print(Back.BLUE + Fore.CYAN + 'start in 5 seconds' + Style.RESET_ALL)
time.sleep(5)

while True:
    pag.press('f5')
    pag.press('enter')
    time.sleep(refresh_frequency)
print(Fore.GREEN + 'done')
