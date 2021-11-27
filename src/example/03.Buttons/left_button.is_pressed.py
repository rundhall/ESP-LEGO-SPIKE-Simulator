from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()
szamlalo = 0
while True:
    wait_for_seconds(0.2)
    
    if hub.left_button.is_pressed():
        print('Jobb gomb '+str(szamlalo))
        szamlalo=szamlalo+1
    if hub.right_button.is_pressed():
        print('Ball gomb')