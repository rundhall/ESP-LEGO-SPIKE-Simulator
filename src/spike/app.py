import machine,time

class App:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True

    #If APPSIMULATE is true then the status of the played music is written to the console. If false the pin is changed. 
    APPSIMULATE = True
    
    #The Pin for Speaker D4 = GPIO2
    SPEAKERPIN = 2
    
    def __init__(self):
        if(self.ISDEBUG):print("App is initialised in debug mode. Simulation:",self.APPSIMULATE, " Speaker PIN:",self.SPEAKERPIN ," change at spike.app.py ")
        if not self.APPSIMULATE:
            self.speakerpin = machine.Pin(self.SPEAKERPIN, machine.Pin.OUT)
            self.speakerpin(1)
        
    def play_sound(self,musicname):
        if(self.ISDEBUG):print("Plays a sound from the device (i.e., tablet or computer).")
        if(self.APPSIMULATE):
            print (musicname + " starts playing this sound for 3 sec") 
        else:
            self.speakerpin(0)
        time.sleep_ms(3000)
        if(self.APPSIMULATE):
            print (musicname + " is played and it is over") 
        else:
            self.speakerpin(1)
        if(self.ISDEBUG):print("The played sound is over")

    def start_sound(self,musicname):
        if(self.ISDEBUG):print("Starts playing a sound from your device. The program will not wait for the sound to finish playing before proceeding to the next command.")
        if(self.APPSIMULATE):
            print (musicname + " starts playing and continue") 
        else:
            self.speakerpin(0)
        time.sleep_ms(100)
        if(self.APPSIMULATE):
            pass
        else:
            self.speakerpin(1)
        if(self.ISDEBUG):print("The played sound is started and finish time is unknowened")
    