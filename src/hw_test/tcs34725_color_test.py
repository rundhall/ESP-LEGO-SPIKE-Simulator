from hw_test import tcs34725
import time,machine
from machine import I2C, Pin
#The PIN for Sensor I2C sda
I2CSDAPIN = 21
#The PIN for Sensor I2C scl
I2CSCLPIN = 22

sensor = tcs34725.TCS34725(machine.I2C(sda=machine.Pin(I2CSDAPIN), scl=machine.Pin(I2CSCLPIN)))
print(sensor.read())

sensor.active(True)
time.sleep_ms(500)
while True:
   # print(sensor.read()[1])
    dataraw = sensor.read(True)
    #print(dataraw[1])
    print(dataraw)
    print(sensor.html_rgb(dataraw))
   # print(sensor.html_rgb(dataraw)[2])
   #print(sensor.html_hex(dataraw))
    time.sleep_ms(500)