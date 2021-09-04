import machine,time,spike.settings

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
        
    def play_sound(self,musicname):
        if(settings.ISDEBUG):print("Plays a sound from the device (i.e., tablet or computer).")
        if(settings.SPEAKERSIMULATE):
            print (musicname + " starts playing this sound for 3 sec") 
        else:
            self.speakerpin(1)
        time.sleep_ms(3000)
        if(settings.SPEAKERSIMULATE):
            print (musicname + " is played and it is over") 
        else:
            self.speakerpin(0)
        if(settings.ISDEBUG):print("The played sound is over")

    def start_sound(self,musicname):
        if(settings.ISDEBUG):print("Starts playing a sound from your device. The program will not wait for the sound to finish playing before proceeding to the next command.")
        if(settings.SPEAKERSIMULATE):
            print (musicname + " starts playing and continue") 
        else:
            self.speakerpin(1)
        time.sleep_ms(100)
        if(settings.SPEAKERSIMULATE):
            pass
        else:
            self.speakerpin(0)
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
            while self.buttonpin.value()==1:
                if(settings.ISDEBUG):print("release the button")
        if(settings.ISDEBUG):print("button is released")
        
    def was_pressed(self):
        if(settings.ISDEBUG):print("Tests to see whether the button has been pressed since the last time this method called.")
        if(settings.BUTTONSIMULATE):
            correctanswer = True
            while correctanswer:
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
            correctanswer = True
            while correctanswer:
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
    
    def start_beep(self):
        if(settings.ISDEBUG):print("start_beep: Start beep.")
        self.speakerpin(1)
        
    def stop(self):
        if(settings.ISDEBUG):print("stop: stop beep.")
        self.speakerpin(0)

class Motion_sensor:
    
    def get_yaw_angle(self):
        if(settings.ISDEBUG):print("get_yaw_angle: The Motion Sensor inside the Hub.")
        

class Motor:
    def __init__(self,port):
        self.port = port
        
    def run_for_seconds(self,time,speed):
        if(settings.ISDEBUG):print("Motor run for seconds: "+str(time)+str(speed)+self.port)