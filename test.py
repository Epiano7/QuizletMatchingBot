import pyautogui as pg
import random as r
import nordvpn_switcher as vpn
def Click():
    pairs = [(545, 415), (545, 800), (545, 1150), (1053, 415), (1053, 800), (1053, 1150), (1537, 415), (1537, 800), (1537, 1150), (1998, 415), (1998, 800), (1998, 1150)]
    pg.click(1288, 1031)
    for i in range(12):
        choice = r.choice(pairs)
        print(choice)
        pg.click(choice)
        pairs.remove(choice)

settings = vpn.initialize_VPN()
vpn.rotate_VPN(settings)


#vpn.rotate_VPN()
#pg.moveTo(1357, 815)
#pg.mouseDown()
#t.sleep(12)
#pg.mouseUp()
#tries_reset = 0
#t.sleep(5)
#vpn.rotate_VPN()