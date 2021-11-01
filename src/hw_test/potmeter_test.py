# Complete project details at https://RandomNerdTutorials.com

import machine
from time import sleep

pot = machine.ADC(machine.Pin(36))
pot.atten(machine.ADC.ATTN_11DB)       #Full range: 3.3v

while True:
  pot_value = pot.read()
  print(pot_value)
  sleep(0.1)