import machine,random,time

class ForceSensor:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #If MOTORSIMULATE is true then the status of the motor is stored in variables and written to the console. If false the motor is controlled by MOTORPIN
    MOTORSIMULATE = False
    #The PIN for Motor
    MOTORPIN = 4
    
    def __init__(self,port):
        self.port = port