import time

class wait_for_seconds:
    ISDEBUG = False
    
    def __init__(self,second):
        time.sleep_ms(1000*second)
        print ('várás vége')