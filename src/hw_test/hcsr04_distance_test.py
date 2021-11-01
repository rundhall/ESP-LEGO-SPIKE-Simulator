from hw_test.hcsr04 import HCSR04
import time
from machine import Pin

sensor = HCSR04(trigger_pin=14, echo_pin=12)
time.sleep_ms(500)
while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    time.sleep_ms(500)
    






