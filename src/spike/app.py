import machine,time

class App:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    
    #The Pin for Speaker D4 = GPIO2
    SPEAKERPIN = 32
    
    def __init__(self):
        if(self.ISDEBUG):print("App->__init__(). App is initialised in debug mode. Speaker PIN:",self.SPEAKERPIN ," change at spike.app.py ")
        self.speakerpin = machine.Pin(self.SPEAKERPIN, machine.Pin.OUT)
        self.speakerpin(1)
        
    def play_sound(self,musicname):
        if(self.ISDEBUG):print("App->play_sound(musicname=",musicname,"). Plays a sound from the device (i.e., tablet or computer).")
        self.speakerpin(0)
        time.sleep_ms(3000)
        self.speakerpin(1)
        if(self.ISDEBUG):print("App->play_sound(musicname=",musicname,"). The played sound is over")

    def start_sound(self,musicname):
        if(self.ISDEBUG):print("App->start_sound(musicname=",musicname,"). Starts playing a sound from your device. The program will not wait for the sound to finish playing before proceeding to the next command.")
        self.speakerpin(0)
        time.sleep_ms(100)
        self.speakerpin(1)
        if(self.ISDEBUG):print("App->start_sound(musicname=",musicname,"). The played sound is started and finish time is unknowened")
    