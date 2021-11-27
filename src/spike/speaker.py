import machine,time


class Speaker:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    
    #The Pin for Speaker D4 = GPIO2
    SPEAKERPIN = 32
    
    
    def __init__(self):
        self.speakerpin = machine.Pin(self.SPEAKERPIN, machine.Pin.OUT)
        if(self.ISDEBUG):print("Speaker->__init__(). Speaker is initialised in debug mode. Speaker PIN:",self.SPEAKERPIN ," change at spike.speaker.py ")
        self.speakerpin(1)
        
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
        if(self.ISDEBUG):print("Speaker->beep(note=",note,",seconds=",seconds,"). Plays a beep on the Hub.")
        self.speakerpwm = machine.PWM(self.speakerpin,freq=0,duty=0)
        #self.speakerpin(0)
        self.speakerpwm.init(freq=int(note*2),duty=512)
        #self.speakerpwm.freq(note)
        time.sleep_ms(int(seconds*1000))
        self.speakerpwm.freq(0)
        self.speakerpwm.deinit()
        self.speakerpin(1)
        #self.speakerpin(0)
    
    def start_beep(self):
        if(self.ISDEBUG):print("Speaker->start_beep(). Starts playing a beep.")
        self.speakerpin(0)
        
    def stop(self):
        if(self.ISDEBUG):print("Speaker->stop(). Stops any sound that is playing.")
        self.speakerpin(1)
    
    def set_volume(self,volume=50):
        if(self.ISDEBUG):print("Speaker->set_volume(volume=",volume,"). Sets the speaker volume. old volume: ",str(self.volume))
        self.volume = volume
    
    def get_volume(self):
        if(self.ISDEBUG):print("Speaker->get_volume(). Retrieves the value of the speaker volume. Actual volume:", self.volume)
        return self.volume