import machine,time,spike.settings,spike.light_matrix,random,spike.left_button,spike.force_sensor,spike.distance_sensor

class PrimeHub:
    PORT_A = "A"
    PORT_B = "B"
    PORT_C = "C"
    PORT_D = "D"
    PORT_E = "E"
    PORT_F = "F"

    
    def __init__(self):
        self.motion_sensor = Motion_sensor()
        self.left_button = left_button.Left_button()
        self.speaker = Speaker()
        self.i2c = machine.I2C(sda=machine.Pin(4), scl=machine.Pin(5))
        self.light_matrix = light_matrix.Light_matrix(self.i2c)
        

class App:
    def __init__(self):
        self.speakerpin = machine.Pin(settings.SPEAKERPIN, machine.Pin.OUT)
        self.speakerpin(1)
    def play_sound(self,musicname):
        if(settings.ISDEBUG):print("Plays a sound from the device (i.e., tablet or computer).")
        if(settings.SPEAKERSIMULATE):
            print (musicname + " starts playing this sound for 3 sec") 
        else:
            self.speakerpin(0)
        time.sleep_ms(3000)
        if(settings.SPEAKERSIMULATE):
            print (musicname + " is played and it is over") 
        else:
            self.speakerpin(1)
        if(settings.ISDEBUG):print("The played sound is over")

    def start_sound(self,musicname):
        if(settings.ISDEBUG):print("Starts playing a sound from your device. The program will not wait for the sound to finish playing before proceeding to the next command.")
        if(settings.SPEAKERSIMULATE):
            print (musicname + " starts playing and continue") 
        else:
            self.speakerpin(0)
        time.sleep_ms(100)
        if(settings.SPEAKERSIMULATE):
            pass
        else:
            self.speakerpin(1)
        if(settings.ISDEBUG):print("The played sound is started and finish time is unknowened")
    


class Speaker:
    def __init__(self):
        self.speakerpin = machine.Pin(settings.SPEAKERPIN, machine.Pin.OUT)
        
        self.speakerpin(1)
        self.speakerpwm = machine.PWM(self.speakerpin,freq=0)
   
    '''beep(note=60, seconds=0.2)
    Plays a beep on the Hub.
    Your program will not continue until seconds have passed.
    Parameters note The MIDI note number.
    Type : float (decimal number)
    Values : 44 to 123 ("60" is the middle C note)
    Default : 60 (middle C note) seconds
    The duration of the beep, specified in seconds.
    Type : float (decimal number)
    Values: any values
    Default: 0.2 seconds
    Errors
    TypeError
    note is not an integer or seconds is not a number.
    ValueError
    note is not within the allowed range of 44-123'''
    def beep(self,note = 60,seconds=0.2):
        if(settings.ISDEBUG):print("start_beep: Start beep.")
        if(settings.SPEAKERSIMULATE):
            print (str(note) + " note starts beeping for "+str(seconds)+" sec") 
        else:
            #self.speakerpin(0)
            self.speakerpwm.init(freq=int(note*2))
           # self.speakerpwm.freq(note)
        time.sleep_ms(int(seconds*1000))
        if(settings.SPEAKERSIMULATE):
            print (str(note) + " note is finished") 
        else:
            self.speakerpwm.freq(0)
            self.speakerpwm.deinit()
            self.speakerpin(1)
        #self.speakerpin(0)
    
    def start_beep(self):
        if(settings.ISDEBUG or setting.SPEAKERSIMULATE):print("start_beep: Start beep.")
        self.speakerpin(0)
        
    def stop(self):
        if(settings.ISDEBUG or setting.SPEAKERSIMULATE):print("stop: stop beep.")
        self.speakerpin(1)

class Motion_sensor:
    
    def get_yaw_angle(self):
        if(settings.ISDEBUG):print("get_yaw_angle: The Motion Sensor inside the Hub.")
        
class ForceSensor:
    def __init__(self,port):
        self.force_sensor = force_sensor.ForceSensor(port)
        
    def get_force_newton(self):
        return self.force_sensor.get_force_newton()
    
    def get_force_percentage(self):
        return self.force_sensor.get_force_percentage()
    
    def is_pressed(self):
        return self.force_sensor.is_pressed()
    
    def wait_until_pressed(self):
        return self.force_sensor.wait_until_pressed()
    
    def wait_until_released(self):
        return self.force_sensor.wait_until_released()

class Motor:
    def __init__(self,port):
        self.motor = motor.Motor(port)

class DistanceSensor:
    def __init__(self,port):
        self.distance_sensor = distance_sensor.DistanceSensor(port)
        
    def get_distance_cm(self,short_range=False):
        return self.distance_sensor.get_distance_cm(short_range)
    
    def get_distance_inches(self,short_range=False):
        return self.distance_sensor.get_distance_inches(short_range)
