import machine,random,time

class MotorPair:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #The PIN for Motor
    MOTORPIN_PORTA = 33
    MOTORPIN_PORTB = 25
    MOTORPIN_PORTC = 25
    MOTORPIN_PORTD = 25
    MOTORPIN_PORTE = 25
    MOTORPIN_PORTF = 25
    #pwm frequency usually 50 Hz is working for servo motors, possible range 30...100.
    MOTOR_PWM_FREQUENCY = 50
    
    CM_TO_DEGREE = 40
    IN_TO_DEGREE = 96
    
    def __init__(self,port1,port2):
        self.port1 = port1
        self.port2 = port2
        self.degrees_counted = 0
        self.default_speed = 100
        self.action="coast"
        self.stop_when_stallesyd=True
        self.degrees = 0
        self.direction = 'clockwise'
        self.speed = None
        self.servo1 = None
        self.servo2 = None
        servo1PIN = self.MOTORPIN_PORTA
        servoP2IN = self.MOTORPIN_PORTA
        if port1 == 'A':
            self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTA),freq=self.MOTOR_PWM_FREQUENCY)
            servo1PIN = self.MOTORPIN_PORTA
        if port1 == 'B':
            self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTB),freq=self.MOTOR_PWM_FREQUENCY)
            servo1PIN = self.MOTORPIN_PORTB
        if port1 == 'C':
            self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTC),freq=self.MOTOR_PWM_FREQUENCY)
            servo1PIN = self.MOTORPIN_PORTC
        if port1 == 'D':
            self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTD),freq=self.MOTOR_PWM_FREQUENCY)
            servo1PIN = self.MOTORPIN_PORTD
        if port1 == 'E':
            self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTE),freq=self.MOTOR_PWM_FREQUENCY)
            servo1PIN = self.MOTORPIN_PORTE
        if port1 == 'F':
            self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTF),freq=self.MOTOR_PWM_FREQUENCY)
            servo1PIN = self.MOTORPIN_PORTF
        if port2 == 'A':
            self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTA),freq=self.MOTOR_PWM_FREQUENCY)
            servo2PIN = self.MOTORPIN_PORTA
        if port2 == 'B':
            self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTB),freq=self.MOTOR_PWM_FREQUENCY)
            servo2PIN = self.MOTORPIN_PORTB
        if port2 == 'C':
            self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTC),freq=self.MOTOR_PWM_FREQUENCY)
            servo2PIN = self.MOTORPIN_PORTC
        if port2 == 'D':
            self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTD),freq=self.MOTOR_PWM_FREQUENCY)
            servo2PIN = self.MOTORPIN_PORTD
        if port2 == 'E':
            self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTE),freq=self.MOTOR_PWM_FREQUENCY)
            servo2PIN = self.MOTORPIN_PORTE
        if port2 == 'F':
            self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTF),freq=self.MOTOR_PWM_FREQUENCY)
            servo2PIN = self.MOTORPIN_PORTF
        if(self.ISDEBUG):print("motor_pair->__init__(port1=",port1,",port2=",port2,"). Motor Pair is initialised in debug mode. Motor 1 PIN:",servo1PIN,",Motor 2 PIN:",servo2PIN,", Motor PWM:",self.MOTOR_PWM_FREQUENCY ," change at motor.py ")


    def set_default_speed(self,default_speed):
        if(self.ISDEBUG):print("motor_pair->set_default_speed(default_speed=",str(default_speed),"). Sets the default motor speed.")
        self.default_speed = default_speed
        
    def set_stop_action(self,action):
        if(self.ISDEBUG):print("motor_pair->set_stop_action(action=",str(action),"). Sets the default behavior when a motor stops.")
        self.action = action
        
    def set_motor_rotation(self,amount, unit='cm'):
        if(self.ISDEBUG):print("motor_pair->set_motor_rotation(amount=",amount,", unit=",unit,"). Sets the ratio of one motor rotation to the distance traveled.")
        self.amount = amount
        self.unit = unit

    
        #input the relatave turn the  speed
    def handel_servo(self,
                     isdebug=True,
                     relative_turn=0,
                     run_time_period = 0,
                     speed1=None,
                     speed2=None,
                     default_speed=100,
                     servo1=None,
                     servo2=None):
        #servo clockwise speed min. 85  max 5 counterclockwise speed min. 95 max 180
        #calculation for clockwise timer=degree*(0.9*speed**2-170*speed+8600)/360 
        #Values:"shortest path" could run in either direction, depending on the shortest distance to the target.
        duty1 = 0
        if speed1 == None:
            speed1 = default_speed
        
        duty2 = 0
        if speed2 == None:
            speed2 = default_speed
        
        if speed1 > 0:
            duty1 = 100 - int(speed1)
            if duty1 < 2:
                duty1 = 2
            timer1=relative_turn*(0.9*speed1**2-170*speed1+8600)/360 
        else:
            duty1 = 80 - speed1
            timer1=relative_turn*(1.19*speed1**2-45.8*speed1+4375)/360
        
        if speed2 > 0:
            duty2 = 100 - int(speed2)
            if duty2 < 2:
                duty2 = 2
            #different calculation for different direction
            timer2=relative_turn*(0.9*speed2**2-170*speed2+8600)/360 
        else:
            duty2 = 80 - speed2
            timer2=relative_turn*(1.19*speed2**2-45.8*speed2+4375)/360
        
        if speed2 == 0:
            duty2 = 0
            
        if speed1 == 0:
            duty1 = 0
            
        if not run_time_period == 0:
            timer1 = int(run_time_period*1000)
            timer2 = int(run_time_period*1000)
            
        if(isdebug):print("relative turn:",str(relative_turn),
                          " speed1:",str(speed1),
                          " duty1:",str(duty1),
                          " speed2:",str(speed2),
                          " duty2:",str(duty2),
                          " timer1:",str(timer1),
                          " timer2:",str(timer2))
        
        return timer1, timer2, duty1, duty2
        
    def start_tank(self,left_speed, right_speed):
        if(self.ISDEBUG):print("motor_pair->start_tank(left_speed=",left_speed,", right_speed=",right_speed,"). Starts moving the Driving Base using differential (tank) steering.")
        if left_speed > 0:
            duty1 = 100 - int(left_speed)
            if duty1 < 2:
                duty1 = 2
        else:
            duty1 = 80 - left_speed  
        self.servo1.duty(duty1)
        if right_speed > 0:
            duty2 = 100 - int(right_speed)
            if duty2 < 2:
                duty2 = 2
        else:
            duty2 = 80 - right_speed      
        self.servo2.duty(duty2)
    
    
    def start_tank_at_power(self,left_power, right_power):
        if(self.ISDEBUG):print("motor_pair->start_tank_at_power(left_power=",left_power,", right_power",right_power,"). Starts moving the Driving Base using differential (tank) steering without speed control.")
        if left_power > 0:
            duty1 = 100 - int(left_power)
            if duty1 < 2:
                duty1 = 2
        else:
            duty1 = 80 - left_power
        self.servo1.duty(duty1)
        if right_power > 0:
            duty2 = 100 - int(right_power)
            if duty2 < 2:
                duty2 = 2
        else:
            duty2 = 80 - right_power      
        self.servo2.duty(duty2)
 
    def get_default_speed (self):
        if(self.ISDEBUG):print("motor_pair->get_default_speed(). Retrieves the motor default_speed. Stored value:",str(self.default_speed))
        return self.default_speed
    
    def start(self,speed=None):
        if(self.ISDEBUG):print("motor_pair->start(speed=",speed,"). Starts running the motor at a specified speed.")
        
        if self.direction=='clockwise':
            isclockwise = True
        else:
            isclockwise = False
        duty = 0
        if speed == None:
            self.speed = self.default_speed
        else:
            self.speed = speed
        if isclockwise:
            duty = 100 - int(self.speed)
            if duty < 2:
                duty = 2
        else:
            duty = 80 + self.speed
        if self.speed == 0:
            duty = 0
        self.servo1.duty(duty)
        self.servo2.duty(duty)
        if(self.ISDEBUG):print("duty:",str(duty)," speed:",str(self.speed)," self.direction:",str(self.direction))
        
    def start_at_power(self,power, steering=0):
        if(self.ISDEBUG):print("motor_pair->start_at_power(power=",power,", steering=",steering,"). Starts moving the Driving Base without speed control.")
        if power == None:
            power = self.default_speed
          
        if steering>0:
            speed1 = power - int(steering*power/100)
            speed2= power
        else:
            speed2 = power - int(-steering*power/100)
            speed1= power
        
        duty1 = 0
        duty2 = 0
        if power<0:
            duty1 = 100 - int(speed1)
            if duty1 < 2:
                duty1 = 2
            duty2 = 100 - int(speed2)
            if duty2 < 2:
                duty2 = 2
        else:
            duty1 = 80 + int(speed1)
            duty2 = 80 + int(speed2)
        if int(speed1) == 0:
            duty1 = 0
        if int(speed2) == 0:
            duty2 = 0
        self.servo1.duty(duty1)
        self.servo2.duty(duty2)
        if(self.ISDEBUG):print("duty1:",str(duty1)," speed1:",str(speed1)," duty2:",str(duty2)," speed2:",str(speed2))
        

    def stop(self):
        if(self.ISDEBUG):print("motor_pair->stop(). Stops the motor.")
        self.servo1.duty(0)
        self.servo2.duty(0)
        

    def move(self,amount, unit='cm', steering=0, speed=None):
        if(self.ISDEBUG):print("motor_pair->move(amount=",str(amount),",unit=",str(unit),",steering=",str(steering),"speed=",str(speed),"). Start both motors simultaneously to move a Driving Base.")
        turn = 0
        run_time = 0
        if unit == "cm":
            turn = int(amount * self.CM_TO_DEGREE)
        if unit == "in":
            turn = int(amount * self.IN_TO_DEGREE)
        if unit == "rotations":
            turn = int(amount*360)
        if unit == "degrees":
            turn = int(amount)
        if unit == "seconds":
            turn = 0
            run_time = amount

        if speed == None:
            speed = self.default_speed
            
        if steering>0:
            speed1 = speed - int(steering*speed/100)
            speed2= speed
        else:
            speed2 = speed - int(-steering*speed/100)
            speed1= speed
        
        timer1, timer2, duty1, duty2 = self.handel_servo(self.ISDEBUG,
                     relative_turn=turn,
                     run_time_period = run_time,
                     speed1=speed1,
                     speed2=speed2,
                     default_speed=self.default_speed)
        if(self.ISDEBUG):print(timer1, timer2, duty1, duty2)
        self.servo1.duty(duty1)
        self.servo2.duty(duty2)
        if(timer1<timer2):
            time.sleep_ms(int(timer1))
            self.servo1.duty(0)
            time.sleep_ms(int(timer2-timer1))
            self.servo2.duty(0)
        else:
            time.sleep_ms(int(timer2))
            self.servo2.duty(0)
            time.sleep_ms(int(timer1-timer2))
            self.servo1.duty(0)
        time.sleep_ms(50)
        
    def move_tank(self,amount, unit='cm', left_speed=None, right_speed=None):
        if(self.ISDEBUG):print("motor_pair->move_tank(amount=",str(amount),", unit=",str(unit),", left_speed=",str(left_speed),", right_speed=",str(right_speed),"). Moves the Driving Base using differential (tank) steering.")
        turn = 0
        run_time = 0
        if unit == "cm":
            turn = int(amount * self.CM_TO_DEGREE)
        if unit == "in":
            turn = int(amount * self.IN_TO_DEGREE)
        if unit == "rotations":
            turn = int(amount*360)
        if unit == "degrees":
            turn = int(amount)
        if unit == "seconds":
            turn = 0
            run_time = amount
        
        timer1, timer2, duty1, duty2 = self.handel_servo(self.ISDEBUG,
                     relative_turn=turn,
                     run_time_period = run_time,
                     speed1=left_speed,
                     speed2=right_speed,
                     default_speed=self.default_speed)
        if(self.ISDEBUG):print(timer1, timer2, duty1, duty2)
        self.servo1.duty(duty1)
        self.servo2.duty(duty2)
        if(timer1<timer2):
            time.sleep_ms(int(timer1))
            self.servo1.duty(0)
            time.sleep_ms(int(timer2-timer1))
            self.servo2.duty(0)
        else:
            time.sleep_ms(int(timer2))
            self.servo2.duty(0)
            time.sleep_ms(int(timer1-timer2))
            self.servo1.duty(0)
        time.sleep_ms(50)