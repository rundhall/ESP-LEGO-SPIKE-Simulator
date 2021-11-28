import machine,random,time

class Motor:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #The PIN for Motor
    MOTORPIN_PORTA = 33
    MOTORPIN_PORTB = 33
    MOTORPIN_PORTC = 33
    MOTORPIN_PORTD = 33
    MOTORPIN_PORTE = 33
    MOTORPIN_PORTF = 33
    #pwm frequency usually 50 Hz is working for servo motors, possible range 30...100.
    MOTOR_PWM_FREQUENCY = 50
    
    def __init__(self,port):
        self.port = port
        self.degrees_counted = 0
        self.default_speed = 100
        self.position = 0
        self.action="coast"
        self.stop_when_stallesyd=True
        self.degrees = 0
        self.direction = 'clockwise'
        self.speed = None
        self.servo = None
        servoPIN = self.MOTORPIN_PORTA
        if port == 'A':
            self.servo = machine.PWM(machine.Pin(self.MOTORPIN_PORTA),freq=self.MOTOR_PWM_FREQUENCY)
            servoPIN = self.MOTORPIN_PORTA
        if port == 'B':
            self.servo = machine.PWM(machine.Pin(self.MOTORPIN_PORTB),freq=self.MOTOR_PWM_FREQUENCY)
            servoPIN = self.MOTORPIN_PORTB
        if port == 'C':
            self.servo = machine.PWM(machine.Pin(self.MOTORPIN_PORTC),freq=self.MOTOR_PWM_FREQUENCY)
            servoPIN = self.MOTORPIN_PORTC
        if port == 'D':
            self.servo = machine.PWM(machine.Pin(self.MOTORPIN_PORTD),freq=self.MOTOR_PWM_FREQUENCY)
            servoPIN = self.MOTORPIN_PORTD
        if port == 'E':
            self.servo = machine.PWM(machine.Pin(self.MOTORPIN_PORTE),freq=self.MOTOR_PWM_FREQUENCY)
            servoPIN = self.MOTORPIN_PORTE
        if port == 'F':
            self.servo = machine.PWM(machine.Pin(self.MOTORPIN_PORTF),freq=self.MOTOR_PWM_FREQUENCY)
            servoPIN = self.MOTORPIN_PORTF
        if(self.ISDEBUG):print("Motor->__init__(port=",port,"). Motor is initialised in debug mode. Motor PIN:",servoPIN,", Motor PWM:",self.MOTOR_PWM_FREQUENCY ," change at motor.py ")


    def set_degrees_counted(self,degrees_counted):
        if(self.ISDEBUG):print("Motor->set_degrees_counted(degrees_counted=",str(degrees_counted),"). Sets the number of degrees counted to the desired value. ")
        self.degrees_counted = degrees_counted
        
    def set_default_speed(self,default_speed):
        if(self.ISDEBUG):print("Motor->set_default_speed(default_speed=",str(default_speed),"). Sets the default motor speed.")
        self.default_speed = default_speed
        
    def set_stop_action(self,action):
        if(self.ISDEBUG):print("Motor->set_stop_action(action=",str(action),"). Sets the default behavior when a motor stops. ")
        self.action = action
        
    def set_stall_detection(self,stop_when_stalled):
        if(self.ISDEBUG):print("Motor->set_stall_detection(stop_when_stalled=",str(stop_when_stalled),"). Turns stall detection on or off. ")
        self.stop_when_stalled = stop_when_stalled
        
        #input the relatave turn the old absolute position and a speed
    def handel_servo(self,
                     isdebug=True,
                     relative_turn=0,
                     old_absolute_position=0,
                     run_time_period = 0,
                     speed=None,
                     default_speed=100):
        #servo clockwise speed min. 85  max 5 counterclockwise speed min. 95 max 180
        #calculation for clockwise timer=degree*(0.9*speed**2-170*speed+8600)/360 
        #Values:"shortest path" could run in either direction, depending on the shortest distance to the target.
        #"clockwise" will make the motor run clockwise until it reaches the target position.
        #"counterclockwise" will make the motor run counterclockwise until it reaches the target position.
        duty = 0
        if speed == None:
            speed = default_speed
        isclockwise = True
        absspeed = speed
        absturn = relative_turn
        if speed > 0:
            if relative_turn > 0:
                isclockwise = True
            else:
                isclockwise = False
                absturn = -absturn 
        else:
            absspeed = -absspeed
            if relative_turn > 0:
                isclockwise = False
            else:
                isclockwise = True
                absturn = -absturn 
            
        if isclockwise:       
            duty = 100 - int(absspeed)
            if duty < 2:
                duty = 2
            timer=absturn*(0.9*absspeed**2-170*absspeed+8600)/360 
        else:
            duty = 80 + absspeed
            timer=absturn*(1.19*absspeed**2-45.8*absspeed+4375)/360
        
        
        if speed == 0:
            duty = 0
        
        if not run_time_period == 0:
            timer = int(run_time_period*1000)
            relative_turn = absturn*1000 / ((0.9*absspeed**2-170*absspeed+8600)/360) 
            if speed < 0:
                relative_turn = relative_turn * -1
                
        new_absolute_position = old_absolute_position + relative_turn % 360
        if new_absolute_position < 0:
            new_absolute_position = new_absolute_position + 360
        
        if(isdebug):print("relative turn:",str(relative_turn),
                          " old absolute position:",str(old_absolute_position),
                          " new absolute position:",str(new_absolute_position),
                          " speed:",str(speed),
                          " duty:",str(duty),
                          " timer:",str(timer))    
        return new_absolute_position,timer, duty
        
                     

    def run_to_position(self,degrees, direction='Shortest path', speed=None):
        if(self.ISDEBUG):print("Motor->run_to_position(degrees=",str(degrees),",direction=",str(direction),",speed=",str(speed),"). Runs the motor to an absolute position. ")
        self.degrees = degrees
        self.direction = direction
        self.speed = speed
        if degrees > 359:
                degrees = 359
        if degrees < 0:
                degrees = 0
        relative_turn = 0
        direction = direction[:1].lower() + direction[1:]
        if direction=='shortest path':
            if degrees > self.position:
                if degrees - self.position > 180:
                    relative_turn = -1*(360 - (degrees-self.position))
                else:
                    relative_turn = degrees-self.position
            else:
                if degrees - self.position < -180:
                    relative_turn = degrees-self.position
                else:
                    relative_turn = -1*(360 - (degrees-self.position))
                   
        if degrees > self.position:
            if direction=='clockwise':
                relative_turn = degrees-self.position
            if direction=='counterclockwise':
                relative_turn = -1*(360 - (degrees-self.position))
        else:
            if direction=='clockwise':
                relative_turn = -1*(360 - (degrees-self.position)) 
            if direction=='counterclockwise':
                relative_turn = degrees-self.position
        if degrees == self.position:
            relative_turn = 0
        self.position,timer,duty = self.handel_servo(
                     isdebug=self.ISDEBUG,
                     relative_turn = relative_turn,
                     old_absolute_position =self.position,
                     run_time_period = 0,
                     speed=self.speed,
                     default_speed=self.default_speed)
        self.servo.duty(duty)
        time.sleep_ms(int(timer))
        self.servo.duty(0)
        
    def run_to_degrees_counted(self,degrees, speed=None):
        if(self.ISDEBUG):print("Motor->run_to_degrees_counted(degrees=",str(degrees),", speed=",str(speed),"). Runs the motor until the number of degrees counted is equal to the value. ")
        self.degrees = degrees
        self.speed = speed
        self.position,timer,duty = self.handel_servo(
                     isdebug=self.ISDEBUG,
                     relative_turn = degrees,
                     old_absolute_position =self.position,
                     run_time_period = 0,
                     speed=self.speed,
                     default_speed=self.default_speed)
        self.servo.duty(duty)
        time.sleep_ms(int(timer))
        self.servo.duty(0)
    
    def run_for_degrees(self,degrees, speed=None):
        if(self.ISDEBUG):print("Motor->run_for_degrees(degrees=",str(degrees),", speed=",str(speed),"). Runs the motor for a specified number of degrees.")
        self.degrees = degrees
        self.speed = speed
        self.position,timer,duty = self.handel_servo(
                     isdebug=self.ISDEBUG,
                     relative_turn = degrees,
                     old_absolute_position =self.position,
                     run_time_period = 0,
                     speed=self.speed,
                     default_speed=self.default_speed)
        self.servo.duty(duty)
        time.sleep_ms(int(timer))
        self.servo.duty(0)

    def run_for_rotations(self,rotations, speed=None):
        if(self.ISDEBUG):print("Motor->run_for_rotations(rotations=",str(rotations),", speed=",str(speed),"). Runs the motor for a specified number of rotations. ")
        self.rotations = rotations
        self.speed = speed
        self.degrees = rotations*360
        self.position = self.handel_servo(
                     isdebug=self.ISDEBUG,
                     relative_turn = self.degrees,
                     old_absolute_position =self.position,
                     run_time_period = 0,
                     speed=self.speed,
                     default_speed=self.default_speed,
                     servo=self.servo)
               
    def run_for_seconds(self,seconds, speed=None):
        if(self.ISDEBUG):print("Motor->run_for_seconds(seconds=",str(seconds),", speed=",str(speed),"). Runs the motor for a specified number of seconds. ")
        self.seconds = seconds
        self.speed = speed
        self.position = self.handel_servo(
             isdebug=self.ISDEBUG,
             relative_turn = self.position,
             old_absolute_position = self.position,
             run_time_period = seconds,
             speed=self.speed,
             default_speed=self.default_speed,
             servo=self.servo)
        
        
        
    def get_speed(self):
        if(self.ISDEBUG):print("Motor->get_speed(). Retrieves the motor speed. Stored value:",str(self.speed))
        return self.speed
    
    def get_position(self):
        if(self.ISDEBUG):print("Motor->get_position(). Retrieves the motor position. Stored value:",str(self.position))
        return self.position
    
    def get_degrees_counted(self):
        if(self.ISDEBUG):print("Motor->get_degrees_counted(). Retrieves the motor degrees_counted. Stored value:",str(self.degrees_counted))
        return self.degrees_counted    

    def get_default_speed (self):
        if(self.ISDEBUG):print("Motor->get_default_speed(). Retrieves the motor default_speed. Stored value:",str(self.default_speed))
        return self.default_speed
    
    def start(self,speed=None):
        if(self.ISDEBUG):print("Motor->start(speed=",speed,"). Starts running the motor at a specified speed. ")
        
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
        self.servo.duty(duty)
        if(self.ISDEBUG):print("duty:",str(duty)," speed:",str(self.speed)," self.direction:",str(self.direction))
        

    def start_at_power(self,power=100):
        if(self.ISDEBUG):print("Motor->start_at_power(power=",str(power),"). Starts rotating the motor at a specified power level. ")
        
        if power > 0:
            isclockwise = True
            self.speed = power
        else:
            isclockwise = False
            self.speed = -power
        duty = 0
        if isclockwise:
            duty = 100 - int(self.speed)
            if duty < 2:
                duty = 2
        else:
            duty = 80 + self.speed
        if self.speed == 0:
            duty = 0
        self.servo.duty(duty)
        if(self.ISDEBUG):print("duty:",str(duty)," speed:",str(self.speed)," self.direction:",str(self.direction))


    def stop(self):
        if(self.ISDEBUG):print("Motor->stop(). Stops the motor.")
        self.servo.duty(0)
        
    def was_interrupted(self):
        if(self.ISDEBUG):print("Motor->was_interrupted(). Tests whether the motor was interrupted.")
        return False
    
    def was_stalled(self):
        if(self.ISDEBUG):print("Motor->was_stalled(). Tests whether the motor was stalled.")
        return False
