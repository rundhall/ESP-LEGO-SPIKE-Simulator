import machine,random,time

class ForceSensor:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #If FORCESENSORSIMULATE is true , if false it measures the ADC value of a potentiometer
    FORCESENSORSIMULATE = True
    #The PIN for Force Sensor (Potentiometer) ADC0
    FORCESENSORPIN = 0
    #Define the type of the Force Sensor simulator. Values:
    #Circularcall: it increases the return value by FORCESENSORCHANGE, after reaching maximum value decreases by FORCESENSORCHANGE every time it is called
    #Random: it returns with a random number 
    #Consol: it asks for a value from the console.
    #FORCESENSORTYPE = "Circularcall"
    FORCESENSORTYPE = "Random"
    #FORCESENSORTYPE = "Consol"
    #The return value of the Force Sensor will change by this number
    FORCESENSORCHANGE = 10
    #If the measured, simulated Force percentage value is lower than FORCESENSORSWITCH value then the Force Sensor is pressed
    FORCESENSORSWITCH=80
    
    def __init__(self,port):
        self.port = port
        self.adc = machine.ADC(self.FORCESENSORPIN)
        self.newton = 0
        self.newtondirection = True
        self.percentage = 0
        self.percentagedirection = True
    def remap(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def get_force_newton(self):
        if(self.ISDEBUG):print("Retrieves the measured force, in newtons.")
        if(self.FORCESENSORSIMULATE):
            if(self.FORCESENSORTYPE == "Random"):
                self.newton = self.remap(random.getrandbits(8), 0, 255, 0, 10)
                if(self.ISDEBUG):print("Simulated random force sensor newton value:", self.newton)
            elif(self.FORCESENSORTYPE == "Circularcall"):
                if(self.newtondirection):
                    self.newton += self.FORCESENSORCHANGE
                    if(self.newton > 9):
                        self.newtondirection = False
                else:
                    self.newton -= self.FORCESENSORCHANGE
                    if(self.newton < 2):
                        self.newtondirection = True
                if(self.ISDEBUG):print("Simulated Circularcall force sensor newton value:", self.newton)
            elif(self.FORCESENSORTYPE == "Consol"):
                self.newton = int(input("new Force Sensor reading in newton (0..10): "))
                if self.newton>10 :
                    self.newton = 10
                if self.newton<0 :
                    self.newton = 0
                if(self.ISDEBUG):print("Simulated force sensor newton value from console:", self.newton)
            return int(self.newton)
        else:
            adcread = self.adc.read()
            if(self.ISDEBUG):print("ADC newtons value:"+str(adcread))
            adcread = self.remap(adcread, 0, 1024, 0, 10)
            return int(adcread)
    
    def get_force_percentage(self):
        if(self.ISDEBUG):print("Retrieves the measured force as a percentage of the maximum force.")
        if(self.FORCESENSORSIMULATE):
            if(self.FORCESENSORTYPE == "Random"):
                self.percentage = self.remap(random.getrandbits(8), 0, 255, 0, 100)
                if(self.ISDEBUG):print("Simulated random force sensor percentage value:", self.percentage)
            elif(self.FORCESENSORTYPE == "Circularcall"):
                if(self.percentagedirection):
                    self.percentage += self.FORCESENSORCHANGE
                    if(self.percentage > 99):
                        self.percentagedirection = False
                else:
                    self.percentage -= self.FORCESENSORCHANGE
                    if(self.percentage < 2):
                        self.percentagedirection = True
                if(self.ISDEBUG):print("Simulated Circularcall force sensor percentage value:", self.percentage)
            elif(self.FORCESENSORTYPE == "Consol"):
                self.percentage = int(input("new Force Sensor reading in percentage (0..100): "))
                if self.percentage>100 :
                    self.percentage = 100
                if self.percentage<0 :
                    self.percentage = 0
                if(self.ISDEBUG):print("Simulated force sensor percentage value from console:", self.percentage)
            return int(self.percentage)
        else:
            adcread = self.adc.read()
            if(self.ISDEBUG):print("ADC percentage value:"+str(adcread))
            adcread = self.remap(adcread, 0, 1024, 0, 100)
            return int(adcread)
        
    def is_pressed(self):
        if(self.ISDEBUG):print("Tests whether the button on the sensor is pressed.")
        if(self.FORCESENSORSIMULATE):
            if(self.FORCESENSORTYPE == "Random"):
                self.percentage = self.remap(random.getrandbits(8), 0, 255, 0, 100)  
            elif(self.FORCESENSORTYPE == "Circularcall"):
                if(self.percentagedirection):
                    self.percentage += self.FORCESENSORCHANGE
                    if(self.percentage > 99):
                        self.percentagedirection = False
                else:
                    self.percentage -= self.FORCESENSORCHANGE
                    if(self.percentage < 2):
                        self.percentagedirection = True
            elif(self.FORCESENSORTYPE == "Consol"):
                readcharacter = input("press 'y' to simulate that the force sensor is pressed 'n' if it is not (y/n): ")
                if(readcharacter =="y"):
                    return True
                if(readcharacter =="n"):
                    return False
            if(self.ISDEBUG):print("Force sensor simulated actual value: "+str(int(self.percentage))+" Switch value:" +str(self.FORCESENSORSWITCH))
            if self.percentage < self.FORCESENSORSWITCH :
                if(self.ISDEBUG):print("force sensor button is pressed")
                return True
            else:
                return False 
        else:
            if(self.ISDEBUG):print("Retrieves the measured force as a percentage of the maximum force.")
            adcread = self.adc.read()
            adcread = self.remap(adcread, 0, 1024, 0, 100)
            if adcread<self.FORCESENSORSWITCH :
                if(self.ISDEBUG):print("force sensor button is pressed")
                return True
            else:
                return False

    def wait_until_pressed(self):
        if(self.ISDEBUG):print("Waits until the Force Sensor is pressed.")
        if(self.FORCESENSORSIMULATE):
            if(self.FORCESENSORTYPE == "Random"):
                randnum =0
                while randnum < self.FORCESENSORSWITCH:
                    randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
                    if(self.ISDEBUG):print("force sensor simulated random number:", str(randnum), " probability:", self.FORCESENSORSWITCH)
                    time.sleep_ms(500)
            elif(self.FORCESENSORTYPE == "Circularcall"):
                self.time = time.ticks_ms()
                while time.ticks_ms() - self.time < 1000 * self.FORCESENSORCHANGE:
                    if(self.ISDEBUG):print("Time remaining until simulated force sensor pressed :", str(1000 * self.FORCESENSORCHANGE - (time.ticks_ms() - self.time)))
            elif(self.FORCESENSORTYPE == "Consol"):
                while input("press 'p' to simulate a Force Sensor press :") != "p":
                    pass
        else:
            while self.remap(adcread, 0, 1024, 0, 100) > self.FORCESENSORSWITCH:
                if(self.ISDEBUG):print("push the Force Sensor")
        if(self.ISDEBUG):print("Force Sensor is pressed")
    
    def wait_until_released(self):
        if(self.ISDEBUG):print("Waits until the Force Sensor is released.")
        if(self.FORCESENSORSIMULATE):
            if(self.FORCESENSORTYPE == "Random"):
                randnum =0
                while randnum < self.FORCESENSORSWITCH:
                    randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
                    if(self.ISDEBUG):print("force sensor simulated random number:", str(randnum), " probability:", self.FORCESENSORSWITCH)
                    time.sleep_ms(500)
            elif(self.FORCESENSORTYPE == "Circularcall"):
                self.time = time.ticks_ms()
                while time.ticks_ms() - self.time < 1000 * self.FORCESENSORCHANGE:
                    if(self.ISDEBUG):print("Time remaining until simulated force sensor released :", str(1000 * self.FORCESENSORCHANGE - (time.ticks_ms() - self.time)))
            elif(self.FORCESENSORTYPE == "Consol"):
                while input("press 'r' to simulate a Force Sensor release: ") != "r":
                    pass
        else:
            while self.remap(adcread, 0, 1024, 0, 100) < self.FORCESENSORSWITCH:
                if(self.ISDEBUG):print("release the Force Sensor")
        if(self.ISDEBUG):print("Force Sensor is released")