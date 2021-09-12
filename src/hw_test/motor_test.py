import machine
import time
adc = machine.ADC(0)
p4 = machine.Pin(12)
servo = machine.PWM(p4,freq=20)
# duty for servo is between 40 - 115

for frek in range (20,200,10):
    servo.freq(frek)
    for x in range (30):
        duty =adc.read()
        servo.duty(duty)
        print (x,'/',frek,'/',duty)
        time.sleep_ms(500)
    
servo.duty(0)
    