import machine,time

class PrimeHub:
    ISDEBUG = False
    PORT_A = "A"
    PORT_B = "B"
    PORT_C = "C"
    PORT_D = "D"
    PORT_E = "E"
    PORT_F = "F"

    
    def __init__(self):
        self.motion_sensor = Motion_sensor()
        self.left_button = Left_button()
        self.speaker = Speaker()

    
class Left_button:

    def __init__(self):
         self.buttonpin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
         self.buttonlast = 0
    
    def wait_until_pressed(self):
        if(PrimeHub.ISDEBUG):print("wait_until_pressed: Waits until the button is pressed.")
        while self.buttonpin.value()==1:
            if(PrimeHub.ISDEBUG):print("push the button")
        if(PrimeHub.ISDEBUG):print("button is pressed")
    
    def wait_until_released(self):
        if(PrimeHub.ISDEBUG):print("wait_until_released: Waits until the button is released.")
        while self.buttonpin.value()==0:
            if(PrimeHub.ISDEBUG):print("release the button")
        if(PrimeHub.ISDEBUG):print("button is released")
        
    def was_pressed(self):
        if(PrimeHub.ISDEBUG):print("Tests to see whether the button has been pressed since the last time this method called.")
        if self.buttonpin.value()==0:
            if self.buttonlast == 1:
                if(PrimeHub.ISDEBUG):print("button has been pressed since the last time")
                self.buttonlast = 0
                return True
            else:
                return False
        else:
            self.buttonlast = 1
            return False
    
    def is_pressed(self):
        if(PrimeHub.ISDEBUG):print("Tests whether the button is pressed.")
        if self.buttonpin.value()==0:
            if(PrimeHub.ISDEBUG):print("button is pressed")
            return True
        else:
            return False

class Speaker:
    def __init__(self):
        self.ledpin = machine.Pin(2, machine.Pin.OUT)
    
    def start_beep(self):
        if(PrimeHub.ISDEBUG):print("start_beep: Start beep.")
        self.ledpin(1)
        
    def stop(self):
        if(PrimeHub.ISDEBUG):print("stop: stop beep.")
        self.ledpin(0)

class Motion_sensor:
    
    def get_yaw_angle(self):
        if(PrimeHub.ISDEBUG):print("get_yaw_angle: The Motion Sensor inside the Hub.")
        

class Motor:
    def __init__(self,port):
        self.port = port
        
    def run_for_seconds(self,time,speed):
        if(PrimeHub.ISDEBUG):print("Motor run for seconds: "+str(time)+str(speed)+self.port)