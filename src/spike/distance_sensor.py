import machine,random,time
from spike.hcsr04 import HCSR04

class DistanceSensor:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #If DISTANCESENSORSIMULATE is true then the distance will change according to their type.
    #If false the distance is measured by HCSR04 Sensor triggered at DISTANCESENSORTRIGERPIN echoed at DISTANCESENSORECHOPIN
    DISTANCESENSORSIMULATE = True
    #The PIN for HCSR04 Sensor trigger
    DISTANCESENSORTRIGERPIN = 13
    #The PIN for HCSR04 Sensor echo
    DISTANCESENSORECHOPIN = 15
    #Define the type of the Distance simulator. Values:
    #Circulartime: it changes the value every second * DISTANCESENSORTIME with the value of DISTANCESENSORCHANGE after reaching the maximum 200 it will drop similarly
    #Random: it returns random distance value
    #Consol: it asks for a value from the console.
    #DISTANCESENSORTYPE = "Circulartime"
    #DISTANCESENSORTYPE = "Random"
    DISTANCESENSORTYPE = "Consol"
    
    #In Circulartime mode this is the time between changes
    DISTANCESENSORTIME = 3
    #In Circulartime mode this the amount the distance value will change every period.
    DISTANCESENSORCHANGE = 10
    
    def __init__(self,port):
        self.port = port
        self.distance_cm =0
        self.distance_inches =0
        self.distance_cmdirection = True
        self.distance_inchesdirection = True
        if not self.DISTANCESENSORSIMULATE:
            self.distancesensor = HCSR04(trigger_pin=self.DISTANCESENSORTRIGERPIN, echo_pin=self.DISTANCESENSORECHOPIN)
        if(self.ISDEBUG):print("Distance sensor is initialised in debug mode. Simulation:",self.DISTANCESENSORSIMULATE, " Button type:",self.DISTANCESENSORTYPE ," change at spike.distance_sensor.py ")
  
    def remap(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  
  
    '''get_distance_cm: Retrieves the measured distance in centimeters.
    Parameters:    short_range
    Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
    Type    :    boolean
    Values    :    True or False
    Default    :    False
    Returns    The measured distance or "none" if the distance can't be measured.
    Type    :    float (decimal number)
    Values    :    0 to 200 cm'''
    def get_distance_cm(self,short_range=False):
        if(self.ISDEBUG):print("Retrieves the measured distance in centimeters.")
        if(self.DISTANCESENSORSIMULATE):
            if(self.DISTANCESENSORTYPE == "Random"):
                self.distance_cm = self.remap(random.getrandbits(8), 0, 255, 0, 200)
                if(self.ISDEBUG):print("Simulated random distance sensor cm value:", self.distance_cm)
            elif(self.DISTANCESENSORTYPE == "Circulartime"):
                if(self.distance_cmdirection):
                    self.distance_cm += self.DISTANCESENSORCHANGE
                    if(self.distance_cm > 200):
                        self.distance_cmdirection = False
                else:
                    self.distance_cm -= self.DISTANCESENSORCHANGE
                    if(self.distance_cm < 0):
                        self.distance_cmdirection = True
                if(self.ISDEBUG):print("Simulated Circulartime distance sensor cm value:", self.distance_cm)
            elif(self.DISTANCESENSORTYPE == "Consol"):
                self.distance_cm = int(input("new Force Sensor reading in distance_cm (0..200): "))
                if self.distance_cm>200 :
                    self.distance_cm = 200
                if self.distance_cm<0 :
                    self.distance_cm = 0
                if(self.ISDEBUG):print("Simulated force sensor distance_cm value from console:", self.distance_cm)
            return int(self.distance_cm)
        else:
            self.distance_cm = int(self.distancesensor.distance_cm())
            if(self.ISDEBUG):print("Row distance sensor value in cm: "+str(self.distance_cm))
            if self.distance_cm<0: self.distance_cm = 0
            if self.distance_cm>200: self.distance_cm = 200
            return self.distance_cm
        
    def get_distance_inches(self,short_range=False):
        if(self.ISDEBUG):print("Retrieves the measured distance in inches.")
        if(self.DISTANCESENSORSIMULATE):
            if(self.DISTANCESENSORTYPE == "Random"):
                self.distance_inches = self.remap(random.getrandbits(8), 0, 255, 0, 79)
                if(self.ISDEBUG):print("Simulated random distance sensor cm value:", self.distance_cm)
            elif(self.DISTANCESENSORTYPE == "Circulartime"):
                if(self.distance_inchesdirection):
                    self.distance_inches += self.DISTANCESENSORCHANGE
                    if(self.distance_inches > 79):
                        self.distance_inchesdirection = False
                else:
                    self.distance_inches -= self.DISTANCESENSORCHANGE
                    if(self.distance_inches < 0):
                        self.distance_inchesdirection = True
                if(self.ISDEBUG):print("Simulated Circulartime distance sensor cm value:", self.distance_inches)
            elif(self.DISTANCESENSORTYPE == "Consol"):
                self.distance_inches = int(input("new Force Sensor reading in distance_inches (0..79): "))
                if self.distance_inches>79 :
                    self.distance_inches = 79
                if self.distance_inches<0 :
                    self.distance_inches = 0
                if(self.ISDEBUG):print("Simulated force sensor distance_inches value from console:", self.distance_inches)
            return int(self.distance_inches)
        else:
            self.distance_inches = int(self.distancesensor.distance_cm()*0.3937)
            if(self.ISDEBUG):print("Row distance sensor value in inches: "+str(self.distance_inches))
            if self.distance_inches<0: self.distance_inches = 0
            if self.distance_inches>79: self.distance_inches = 79
            return self.distance_inches
        
        
        




