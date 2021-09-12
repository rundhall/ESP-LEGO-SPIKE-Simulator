import time
import random
speakerpin = machine.Pin(2, machine.Pin.OUT)
speakerpin(1)

for x in range(10):
    print("Plays a sound")
    speakerpin(0)
    time.sleep_ms(random.getrandbits(8))
    speakerpin(1)
    time.sleep_ms(random.getrandbits(8))
    print("The played sound is over")

