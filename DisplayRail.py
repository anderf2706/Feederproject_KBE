import time

import pyautogui



def automate():

    pyautogui.moveTo(1132, 1052)
    pyautogui.leftClick()

    pyautogui.hotkey('alt', 'f8')

    pyautogui.moveTo(1101, 390)
    pyautogui.leftClick()

    pyautogui.moveTo(1208, 568)
    pyautogui.leftClick()

    time.sleep(10)
    SS = pyautogui.screenshot(region=(250, 200, 1700, 800))
    SS.save('C:\\Users\\Anders Fredriksen\\Desktop\\Schuul\\Auto2\\flask_project3\\static\\render2.png')

"""
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
"""



