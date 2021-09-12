import machine,time,spike.settings,random

class PrimeHub:
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
    
class Left_button:

    def __init__(self):
         self.buttonpin = machine.Pin(settings.BUTTONPIN, machine.Pin.IN, machine.Pin.PULL_UP)
         self.buttonlast = 0
    
    def wait_until_pressed(self):
        if(settings.ISDEBUG):print("wait_until_pressed: Waits until the button is pressed.")
        if(settings.BUTTONSIMULATE):
            while input("press 'p' to simulate a button press :") != "p":
                pass
        else:
            while self.buttonpin.value()==1:
                if(settings.ISDEBUG):print("push the button")
        if(settings.ISDEBUG):print("button is pressed")
    
    def wait_until_released(self):
        if(settings.ISDEBUG):print("wait_until_released: Waits until the button is released.")
        if(settings.BUTTONSIMULATE):
            while input("press 'r' to simulate a button release: ") != "r":
                pass
        else:
            while self.buttonpin.value()==0:
                if(settings.ISDEBUG):print("release the button")
        if(settings.ISDEBUG):print("button is released")
        
    def was_pressed(self):
        if(settings.ISDEBUG):print("Tests to see whether the button has been pressed since the last time this method called.")
        if(settings.BUTTONSIMULATE):
            readcharacter = input("press 'y' to simulate that the button was pressed 'n' if it was not (y/n): ")
            if(readcharacter =="y"):
                return True
            if(readcharacter =="n"):
                return False
            
        else:
            if self.buttonpin.value()==0:
                if self.buttonlast == 1:
                    if(settings.ISDEBUG):print("button has been pressed since the last time")
                    self.buttonlast = 0
                    return True
                else:
                    return False
            else:
                self.buttonlast = 1
                return False
    
    def is_pressed(self):
        if(settings.ISDEBUG):print("Tests whether the button is pressed.")
        if(settings.BUTTONSIMULATE):
            readcharacter = input("press 'y' to simulate that the button is pressed 'n' if it is not (y/n): ")
            if(readcharacter =="y"):
                return True
            if(readcharacter =="n"):
                return False
        else:
            if self.buttonpin.value()==0:
                if(settings.ISDEBUG):print("button is pressed")
                return True
            else:
                return False

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
        

class Motor:
    def __init__(self,port):
        self.port = port
        
    def run_for_seconds(self,time,speed):
        if(settings.ISDEBUG):print("Motor run for seconds: "+str(time)+str(speed)+self.port)
        
class ForceSensor:
    def __init__(self,port):
        self.port = port
        self.adc = machine.ADC(settings.FORCESENSORPIN)
        self.newton = 0
        self.newtondirection = True
        self.percentage = 0
        self.percentagedirection = True
    def remap(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def get_force_newton(self):
        if(settings.ISDEBUG):print("Retrieves the measured force, in newtons.")
        if(settings.FORCESENSORSIMULATE):
            if(settings.FORCESENSORTYPE == "Random"):
                self.newton = self.remap(random.getrandbits(8), 0, 255, 0, 10)
            elif(settings.FORCESENSORTYPE == "Circular"):
                if(self.newtondirection):
                    self.newton += settings.FORCESENSORCHANGE
                    if(self.newton > 9):
                        self.newtondirection = False
                else:
                    self.newton -= settings.FORCESENSORCHANGE
                    if(self.newton < 2):
                        self.newtondirection = True
            elif(settings.FORCESENSORTYPE == "Consol"):
                self.newton = int(input("new Force Sensor reading in newton (0..10): "))
                if self.newton>10 :
                    self.newton = 10
                if self.newton<0 :
                    self.newton = 0
            return int(self.newton)
        else:
            adcread = self.adc.read()
            if(settings.ISDEBUG):print("ADC newtons value:"+str(adcread))
            adcread = self.remap(adcread, 0, 1024, 0, 10)
            return int(adcread)
    
    def get_force_percentage(self):
        if(settings.ISDEBUG):print("Retrieves the measured force as a percentage of the maximum force.")
        if(settings.FORCESENSORSIMULATE):
            if(settings.FORCESENSORTYPE == "Random"):
                self.percentage = self.remap(random.getrandbits(8), 0, 255, 0, 100)
            elif(settings.FORCESENSORTYPE == "Circular"):
                if(self.percentagedirection):
                    self.percentage += settings.FORCESENSORCHANGE
                    if(self.percentage > 99):
                        self.percentagedirection = False
                else:
                    self.percentage -= settings.FORCESENSORCHANGE
                    if(self.percentage < 2):
                        self.percentagedirection = True
            elif(settings.FORCESENSORTYPE == "Consol"):
                self.percentage = int(input("new Force Sensor reading in percentage (0..100): "))
                if self.percentage>100 :
                    self.percentage = 100
                if self.percentage<0 :
                    self.percentage = 0
            return int(self.percentage)
        else:
            adcread = self.adc.read()
            if(settings.ISDEBUG):print("ADC percentage value:"+str(adcread))
            adcread = self.remap(adcread, 0, 1024, 0, 100)
            return int(adcread)
        
    def is_pressed(self):
        if(settings.ISDEBUG):print("Tests whether the button on the sensor is pressed.")
        if(settings.FORCESENSORSIMULATE):
            if(settings.FORCESENSORTYPE == "Random"):
                self.percentage = self.remap(random.getrandbits(8), 0, 255, 0, 100)  
            elif(settings.FORCESENSORTYPE == "Circular"):
                if(self.percentagedirection):
                    self.percentage += settings.FORCESENSORCHANGE
                    if(self.percentage > 99):
                        self.percentagedirection = False
                else:
                    self.percentage -= settings.FORCESENSORCHANGE
                    if(self.percentage < 2):
                        self.percentagedirection = True
            elif(settings.FORCESENSORTYPE == "Consol"):
                readcharacter = input("press 'y' to simulate that the force sensor is pressed 'n' if it is not (y/n): ")
                if(readcharacter =="y"):
                    return True
                if(readcharacter =="n"):
                    return False
            if(settings.ISDEBUG):print("Force sensor actual value: "+str(int(self.percentage))+" Switch value:" +str(settings.FORCESENSORSWITCH))
            if self.percentage < settings.FORCESENSORSWITCH :
                if(settings.ISDEBUG):print("force sensor button is pressed")
                return True
            else:
                return False 
        else:
            if(settings.ISDEBUG):print("Retrieves the measured force as a percentage of the maximum force.")
            adcread = self.adc.read()
            adcread = self.remap(adcread, 0, 1024, 0, 100)
            if adcread<settings.FORCESENSORSWITCH :
                if(settings.ISDEBUG):print("force sensor button is pressed")
                return True
            else:
                return False

    def wait_until_pressed(self):
        if(settings.ISDEBUG):print("Waits until the Force Sensor is pressed.")
        if(settings.FORCESENSORSIMULATE):
            while input("press 'p' to simulate a Force Sensor press :") != "p":
                pass
        else:
            while self.remap(adcread, 0, 1024, 0, 100) > settings.FORCESENSORSWITCH:
                if(settings.ISDEBUG):print("push the Force Sensor")
        if(settings.ISDEBUG):print("Force Sensor is pressed")
    
    def wait_until_released(self):
        if(settings.ISDEBUG):print("Waits until the Force Sensor is released.")
        if(settings.BUTTONSIMULATE):
            while input("press 'r' to simulate a Force Sensor release: ") != "r":
                pass
        else:
            while self.remap(adcread, 0, 1024, 0, 100) < settings.FORCESENSORSWITCH:
                if(settings.ISDEBUG):print("release the Force Sensor")
        if(settings.ISDEBUG):print("Force Sensor is released")