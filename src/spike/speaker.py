import machine,time


class Speaker:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True

    #If SPEAKERSIMULATE is true then the status of the beep music is written to the console. If false the pin is changed. 
    SPEAKERSIMULATE = True
    
    #The Pin for Speaker D4 = GPIO2
    SPEAKERPIN = 2
    
    
    def __init__(self):
        self.speakerpin = machine.Pin(self.SPEAKERPIN, machine.Pin.OUT)
        if(self.ISDEBUG):print("Speaker is initialised in debug mode. Simulation:",self.SPEAKERSIMULATE, " Speaker PIN:",self.SPEAKERPIN ," change at spike.speaker.py ")
        self.speakerpin(1)
        self.speakerpwm = machine.PWM(self.speakerpin,freq=0)
        self.volume = 0
   
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
        if(self.ISDEBUG):print("start_beep: Start beep.")
        if(self.SPEAKERSIMULATE):
            print (str(note) + " note starts beeping for "+str(seconds)+" sec") 
        else:
            #self.speakerpin(0)
            self.speakerpwm.init(freq=int(note*2))
           # self.speakerpwm.freq(note)
        time.sleep_ms(int(seconds*1000))
        if(self.SPEAKERSIMULATE):
            print (str(note) + " note is finished") 
        else:
            self.speakerpwm.freq(0)
            self.speakerpwm.deinit()
            self.speakerpin(1)
        #self.speakerpin(0)
    
    def start_beep(self):
        if(self.ISDEBUG or setting.SPEAKERSIMULATE):print("start_beep: Start beep.")
        if not self.SPEAKERSIMULATE:
            self.speakerpin(0)
        
    def stop(self):
        if(self.ISDEBUG or setting.SPEAKERSIMULATE):print("stop: stop beep.")
        if not self.SPEAKERSIMULATE:
            self.speakerpin(1)
    
    def set_volume(self,volume=50):
        if(self.ISDEBUG):print("old volume: ",str(self.volume)," changed to new volume:", volume)
        self.volume = volume
    
    def get_volume(self):
        if(self.ISDEBUG):print("get stored volume:", self.volume)
        return self.volume