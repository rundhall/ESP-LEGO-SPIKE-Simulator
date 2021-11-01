import machine
import time
adc = machine.ADC(machine.Pin(36))
adc.atten(machine.ADC.ATTN_11DB)       #Full range: 3.3v
servo = machine.PWM(machine.Pin(25),freq=50)
# duty for servo is between 40 - 115

def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

buttonpin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

'''
#Test duty cycle with a potentiometer
for x in range (1000):
    duty =int(remap(adc.read(),0,4096,0,180))
    servo.duty(duty)
    print (x,'//',duty,'//',adc.read())
    time.sleep_ms(500)
    
servo.duty(0)
'''
'''
#test different time period to find one round 360 degree for every speed
buttonpressed = False 
while True:
    if buttonpin.value()==0:
        if not buttonpressed:
            buttonpressed = True 
            servo.duty(50)
            timer = adc.read()
            time.sleep_ms(timer)
            print("servo run for ms:", str(timer))
    else:
        buttonpressed = False 
    servo.duty(0)
'''
'''
#Test calculation 1,3*A2*A2-23*A2+580
servo.duty(0)
speed = 2.0
degree = 180

# degree = float(input("Set degree :"))
servo.duty(int(speed))
timer = degree*(0.9*speed**2-10*speed+615)/360
print("timer:", str(timer),"degree:", str(degree),"speed:", str(speed))
time.sleep_ms(int(timer))
servo.duty(0)
'''

speed = 170.0
degree = 180
# degree = float(input("Set degree :"))
servo.duty(int(speed))
timer = 8000
print("timer:", str(timer),"degree:", str(degree),"speed:", str(speed))
time.sleep_ms(int(timer))
servo.duty(0)
