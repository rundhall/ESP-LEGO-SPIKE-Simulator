from hw_test import tcs34725
import time
from machine import I2C, Pin
i2c = I2C(Pin(5), Pin(4))
sensor = tcs34725.TCS34725(i2c)
print(sensor.read())

sensor.active(True)
time.sleep_ms(500)
while True:
    print(sensor.read())
    time.sleep_ms(500)