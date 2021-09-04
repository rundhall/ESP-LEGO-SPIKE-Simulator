import time,spike.settings

class wait_for_seconds:
    
    def __init__(self,second):
       # if(settings.ISDEBUG):print (str(second)+' sec wait_for_seconds ended')
        time.sleep_ms(1000*second)
      #  if(settings.ISDEBUG):print (str(second)+' sec wait_for_seconds ended')