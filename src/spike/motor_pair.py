import machine,random,time

class MotorPair:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #If ISSIMULATION is true then the status of the motor is stored in variables and written to the console. If false a continuous servo motor is controlled by MOTORPIN with pwm signals
    ISSIMULATION = True
    #The PIN for Motor
    MOTORPIN_PORTA = 25
    MOTORPIN_PORTB = 25
    MOTORPIN_PORTC = 25
    MOTORPIN_PORTD = 25
    MOTORPIN_PORTE = 25
    MOTORPIN_PORTF = 25
    #pwm frequency usually 50 Hz is working for servo motors, possible range 30...100.
    MOTOR_PWM_FREQUENCY = 50
    
    def __init__(self,port1,port2):
        self.port1 = port1
        self.port2 = port2
        self.degrees_counted = 0
        self.default_speed = 100
        self.position = 0
        self.action="coast"
        self.stop_when_stallesyd=True
        self.degrees = 0
        self.direction = 'clockwise'
        self.speed = None
        self.servo1 = None
        self.servo2 = None
        if not self.ISSIMULATION:
            if port1 == 'A': self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTA),freq=self.MOTOR_PWM_FREQUENCY)
            if port1 == 'B': self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTB),freq=self.MOTOR_PWM_FREQUENCY)
            if port1 == 'C': self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTC),freq=self.MOTOR_PWM_FREQUENCY)
            if port1 == 'D': self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTD),freq=self.MOTOR_PWM_FREQUENCY)
            if port1 == 'E': self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTE),freq=self.MOTOR_PWM_FREQUENCY)
            if port1 == 'F': self.servo1 = machine.PWM(machine.Pin(self.MOTORPIN_PORTF),freq=self.MOTOR_PWM_FREQUENCY)
            if port2 == 'A': self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTA),freq=self.MOTOR_PWM_FREQUENCY)
            if port2 == 'B': self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTB),freq=self.MOTOR_PWM_FREQUENCY)
            if port2 == 'C': self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTC),freq=self.MOTOR_PWM_FREQUENCY)
            if port2 == 'D': self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTD),freq=self.MOTOR_PWM_FREQUENCY)
            if port2 == 'E': self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTE),freq=self.MOTOR_PWM_FREQUENCY)
            if port2 == 'F': self.servo2 = machine.PWM(machine.Pin(self.MOTORPIN_PORTF),freq=self.MOTOR_PWM_FREQUENCY)
    
    def set_default_speed(self,default_speed):
        if(self.ISDEBUG):print("motor_pair set_default_speed(). Sets the default motor speed. New value default_speed:",str(default_speed))
        self.default_speed = default_speed
        
    def set_stop_action(self,action):
        if(self.ISDEBUG):print("motor_pair set_stop_action(). Sets the default behavior when a motor stops. New value action:",str(action))
        self.action = action
        
    def set_motor_rotation(self,amount, unit='cm'):
        if(self.ISDEBUG):print("motor_pair set_motor_rotation(). Sets the ratio of one motor rotation to the distance traveled. New value amount:",str(amount)," unit:",str(unit))
        self.amount = amount
        self.unit = unit

    
        #input the relatave turn the old absolute position and a speed
    def handel_servo(self,
                     issimulation=True,
                     isdebug=True,
                     relative_turn1=0,
                     relative_turn2=0,
                     old_absolute_position=0,
                     run_time_period = 0,
                     speed1=None,
                     speed2=None,
                     default_speed=100,
                     servo1=None,
                     servo2=None):
        #servo clockwise speed min. 85  max 5 counterclockwise speed min. 95 max 180
        #calculation for clockwise timer=degree*(0.9*speed**2-170*speed+8600)/360 
        #Values:"shortest path" could run in either direction, depending on the shortest distance to the target.
        #"clockwise" will make the motor run clockwise until it reaches the target position.
        #"counterclockwise" will make the motor run counterclockwise until it reaches the target position.
        duty1 = 0
        if speed1 == None:
            speed1 = default_speed
        else:
            speed1 = speed1
        if speed1 == 0:
            duty1 = 0
        
        duty2 = 0
        if speed2 == None:
            speed2 = default_speed
        else:
            speed2 = speed2
        if speed2 == 0:
            duty2 = 0
        
        if not run_time_period == 0:
            relative_turn = run_time_period*1000 / ((0.9*speed1**2-170*speed1+8600)/360) 
            if speed1 < 0:
                relative_turn = relative_turn * -1
        
        new_absolute_position = old_absolute_position + relative_turn % 360
        
        if relative_turn > 0:
            duty1 = 100 - int(speed1)
            if duty1 < 2:
                duty1 = 2
            #different calculation for different direction
            timer=abs(relative_turn*(0.9*speed1**2-170*speed1+8600)/360) 
        else:
            duty1 = 80 + speed1
            timer=abs(relative_turn*(1.19*speed1**2-45.8*speed1+4375)/360)
        
        if relative_turn > 0:
            duty2 = 100 - int(speed1)
            if duty2 < 2:
                duty2 = 2
        else:
            duty2 = 80 + speed2
        
        if new_absolute_position < 0:
            new_absolute_position = new_absolute_position + 360
        if(isdebug):print("relative turn1:",str(relative_turn1),
                          "relative turn2:",str(relative_turn2),
                          " old absolute position:",str(old_absolute_position),
                          " new absolute position:",str(new_absolute_position),
                          " speed1:",str(speed1),
                          " duty1:",str(duty1),
                          " speed2:",str(speed2),
                          " duty2:",str(duty2),
                          " timer:",str(timer))
        if not issimulation: servo1.duty(duty1)
        if not issimulation: servo2.duty(duty2)
        if run_time_period == 0:
            time.sleep_ms(int(timer))
        else:
            time.sleep_ms(int(run_time_period*1000))
        if not issimulation: servo1.duty(0)
        if not issimulation: servo2.duty(0)
        return new_absolute_position
        
    def start_tank(self,left_speed, right_speed):
        if(self.ISDEBUG):print("motor_pair start_tank(). Starts moving the Driving Base using differential (tank) steering. New values left_speed:",str(left_speed)," right_speed:",str(right_speed))
        if left_speed > 0:
            duty1 = 100 - int(left_speed)
            if duty1 < 2:
                duty1 = 2
        else:
            duty1 = 80 + abs(left_speed)  
        if not self.ISSIMULATION: self.servo1.duty(duty1)
        if right_speed > 0:
            duty2 = 100 - int(right_speed)
            if duty2 < 2:
                duty2 = 2
        else:
            duty2 = 80 + abs(right_speed)        
        if not self.ISSIMULATION: self.servo2.duty(duty2)
    
    
    def start_tank_at_power(self,left_power, right_power):
        if(self.ISDEBUG):print("motor_pair start_tank_at_power(). Starts moving the Driving Base using differential (tank) steering without speed control. New values left_power:",str(left_power)," right_power:",str(right_power))
        if left_power > 0:
            duty1 = 100 - int(left_power)
            if duty1 < 2:
                duty1 = 2
        else:
            duty1 = 80 + abs(left_power)
        if not self.ISSIMULATION: self.servo1.duty(duty1)
        if right_power > 0:
            duty2 = 100 - int(right_power)
            if duty2 < 2:
                duty2 = 2
        else:
            duty2 = 80 + abs(right_power)        
        if not self.ISSIMULATION: self.servo2.duty(duty2)
 
    def get_default_speed (self):
        if(self.ISDEBUG):print("motor_pair get_default_speed(). Retrieves the motor default_speed. Stored value:",str(self.default_speed))
        return self.default_speed
    
    def start(self,speed=None):
        if(self.ISDEBUG):print("motor_pair start(). Starts running the motor at a specified speed. New values speed:",str(speed))
        
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
        if not self.ISSIMULATION: self.servo1.duty(duty)
        if not self.ISSIMULATION: self.servo2.duty(duty)
        if(self.ISDEBUG):print("duty:",str(duty)," speed:",str(self.speed)," self.direction:",str(self.direction))
        

    def stop(self):
        if(self.ISDEBUG):print("motor_pair stop(). Stops the motor.")
        if not self.ISSIMULATION: self.servo1.duty(0)
        if not self.ISSIMULATION: self.servo2.duty(0)
        

