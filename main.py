import pyautogui as pg
import random as r
import time as t
import sys
import nordvpn_switcher as vpn
global xchoice, ychoice, tries, tries_reset
vpn.initialize_VPN(save=1, area_input=['random regions united states 15'])
sys.setrecursionlimit(150000000)
tries_reset = 0
tries = 0
xchoice = 0
ychoice = 0
int(xchoice)
int(ychoice)
# x = [545, 1053, 1537, 1998]
# y = [415, 800, 1150]
input('Hit any ket to continue, hit Control+ALT+DELETE to stop')


def Click():
    pairs = [(545, 415), (545, 800), (545, 1150), (1053, 415), (1053, 800), (1053, 1150), (1537, 415), (1537, 800),
             (1537, 1150), (1998, 415), (1998, 800), (1998, 1150)]
    pg.click(1288, 1031)
    t.sleep(0.08)
    global tries, tries_reset
    for i in range(12):
        choice = r.choice(pairs)
        pg.click(choice)
        pairs.remove(choice)
        #  print(pairs)
        t.sleep(0.05)
    tries += 1
    tries_reset += 1
    if tries_reset == 25:
        vpn.rotate_VPN()
        t.sleep(3)
        tries_reset = 0
    print('Total Attempts: ', tries)
    t.sleep(0.1)
    pg.hotkey('f5')
    t.sleep(1.1)


while True:
    Click()
