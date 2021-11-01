import time,machine
BUTTONPIN = 0
buttonpin = machine.Pin(BUTTONPIN, machine.Pin.IN, machine.Pin.PULL_UP)
buttonlast = 0

print("wait_until_pressed: Waits until the button is pressed.")
while buttonpin.value()==1:
    print("push the button")
    time.sleep_ms(100)
print("button is pressed") 
