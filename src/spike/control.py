import time

class wait_for_seconds:
    
    def __init__(self,second):
       # if(settings.ISDEBUG):print (str(second)+' sec wait_for_seconds ended')
        time.sleep_ms(int(1000*second))
      #  if(settings.ISDEBUG):print (str(second)+' sec wait_for_seconds ended')
      
class Timer:
    
    def __init__(self):
        self.start = time.ticks_ms()
    
    def now(self):
        dif = time.ticks_ms()- self.start
        print("time.now", dif) 
        return dif