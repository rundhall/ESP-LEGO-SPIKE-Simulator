from machine import Pin
from neopixel import NeoPixel
from machine import sleep
import time
import random


pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels

random.seed(29)

for x in range(8):
    np[x] = (0, 0, 0) # set the first pixel to white
np.write()              # write data to all pixels

for y in range(100):
    for x in range(8):
        np[x] = (random.getrandbits(8), random.getrandbits(8), random.getrandbits(8)) # set the first pixel to white
    np.write()              # write data to all pixels
    sleep(200)

for x in range(8):
    np[x] = (0, 0, 0) # set the first pixel to white
np.write()              # write data to all pixels
