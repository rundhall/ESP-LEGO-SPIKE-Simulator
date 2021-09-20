import machine,time,random

class Left_button:
    ISDEBUG = True
    #If BUTTONSIMULATE is true it waits for a button to be pressed via the console, if false it monitors the state of the BUTTONPIN
    BUTTONSIMULATE = True
    #The PIN for Button D3 = GPIO0
    BUTTONPIN = 0
    #Define the type of the Button simulator. Values:
    #Circulartime: it changes the value every second * BUTTONPRESSTIME 
    #Random: it returns pressed with a probability stated in BUTTON PROBABILITY value
    #Consol: it asks for a value from the console.
    #BUTTONTYPE = "Circulartime"
    BUTTONTYPE = "Random"
    #BUTTONTYPE = "Consol"
    BUTTONPRESSTIME = 3
    BUTTONPROBABILITY = 80

    def __init__(self):
         self.buttonlast = 0
         self.buttonpin = machine.Pin(self.BUTTONPIN, machine.Pin.IN, machine.Pin.PULL_UP)
         if(self.ISDEBUG):print("Button is initialised in debug mode. Simulation:",self.BUTTONSIMULATE, " Button type:",self.BUTTONTYPE ," change at spike.left_button.py ")
         self.time = time.ticks_ms()
         
    def remap(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
    def wait_until_pressed(self):
        if(self.ISDEBUG):print("wait_until_pressed: Waits until the button is pressed.")
        if(self.BUTTONSIMULATE):
            if(self.BUTTONTYPE == "Random"):
                randnum =0
                while randnum < self.BUTTONPROBABILITY:
                    randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
                    if(self.ISDEBUG):print("press button simulated random number:", str(randnum), " probability:", self.BUTTONPROBABILITY)
                    time.sleep_ms(500)
            elif(self.BUTTONTYPE == "Circulartime"):
                self.time = time.ticks_ms()
                while time.ticks_ms() - self.time < 1000 * self.BUTTONPRESSTIME:
                    if(self.ISDEBUG):print("Time remaining until simulated button press :", str(1000 * self.BUTTONPRESSTIME - (time.ticks_ms() - self.time)))
            elif(self.BUTTONTYPE == "Consol"):
                while input("press 'p' to simulate a button press :") != "p":
                    pass
        else:
            while self.buttonpin.value()==1:
                if(self.ISDEBUG):print("push the button")
        if(self.ISDEBUG):print("button is pressed")
    
    def wait_until_released(self):
        if(self.ISDEBUG):print("wait_until_released: Waits until the button is released.")
        if(self.BUTTONSIMULATE):
            if(self.BUTTONTYPE == "Random"):
                randnum =0
                while randnum < self.BUTTONPROBABILITY:
                    randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
                    if(self.ISDEBUG):print("releas button simulated random number:", str(randnum), " probability:", self.BUTTONPROBABILITY)
                    time.sleep_ms(500)
            elif(self.BUTTONTYPE == "Circulartime"):
                self.time = time.ticks_ms()
                while time.ticks_ms() - self.time < 1000 * self.BUTTONPRESSTIME:
                    if(self.ISDEBUG):print("Time remaining until simulated button released :", str(1000 * self.BUTTONPRESSTIME - (time.ticks_ms() - self.time)))
            elif(self.BUTTONTYPE == "Consol"):
                while input("press 'r' to simulate a button release: ") != "r":
                    pass
        else:
            while self.buttonpin.value()==0:
                if(self.ISDEBUG):print("release the button")
        if(self.ISDEBUG):print("button is released")
        
    def was_pressed(self):
        if(self.ISDEBUG):print("Tests to see whether the button has been pressed since the last time this method called.")
        if(self.BUTTONSIMULATE):
            if(self.BUTTONTYPE == "Random"):
                randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
                if(self.ISDEBUG):print("Simulated button was pressed if random number:", str(randnum), " is higher then probability:", self.BUTTONPROBABILITY)
                if randnum < self.BUTTONPROBABILITY:
                    if(self.ISDEBUG):print("Simulated button was not pressed")
                    return False
                else:
                    if(self.ISDEBUG):print("Simulated button was pressed")
                    return True
            elif(self.BUTTONTYPE == "Circulartime"):
                if time.ticks_ms() - self.time > 1000 * self.BUTTONPRESSTIME:
                    if(self.ISDEBUG):print("Time is up and the simulated button is pressed time ago:", str((time.ticks_ms() - self.time)-1000 * self.BUTTONPRESSTIME))
                    self.time = time.ticks_ms()
                    return True
                else:
                    if(self.ISDEBUG):print("Simulated button press will come in :", str(1000 * self.BUTTONPRESSTIME- (time.ticks_ms() - self.time)), " msec")
                    return False
                    
            elif(self.BUTTONTYPE == "Consol"):
                readcharacter = input("press 'y' to simulate that the button was pressed 'n' if it was not (y/n): ")
                if(readcharacter =="y"):
                    return True
                if(readcharacter =="n"):
                    return False
            
        else:
            if self.buttonpin.value()==0:
                if self.buttonlast == 1:
                    if(self.ISDEBUG):print("button has been pressed since the last time")
                    self.buttonlast = 0
                    return True
                else:
                    return False
            else:
                self.buttonlast = 1
                return False
    
    def is_pressed(self):
        if(self.ISDEBUG):print("Tests whether the button is pressed.")
        if(self.BUTTONSIMULATE):
            if(self.BUTTONTYPE == "Random"):
                randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
                if(self.ISDEBUG):print("Simulated button is pressed if random number:", str(randnum), " higher then probability:", self.BUTTONPROBABILITY)
                if randnum < self.BUTTONPROBABILITY:
                    if(self.ISDEBUG):print("Simulated button is not pressed")
                    return False
                else:
                    if(self.ISDEBUG):print("Simulated button is pressed")
                    return True
            elif(self.BUTTONTYPE == "Circulartime"):
                if time.ticks_ms() - self.time > 1000 * self.BUTTONPRESSTIME:
                    if(self.ISDEBUG):print("Time is up and the simulated button is pressed time ago:", str((time.ticks_ms() - self.time)-1000 * self.BUTTONPRESSTIME))
                    self.time = time.ticks_ms()
                    return True
                else:
                    if(self.ISDEBUG):print("Simulated button press will come in :", str(1000 * self.BUTTONPRESSTIME- (time.ticks_ms() - self.time)), " msec")
                    return False
                    
            elif(self.BUTTONTYPE == "Consol"):
                readcharacter = input("press 'y' to simulate that the button is pressed 'n' if it is not (y/n): ")
                if(readcharacter =="y"):
                    return True
                if(readcharacter =="n"):
                    return False
        else:
            if self.buttonpin.value()==0:
                if(self.ISDEBUG):print("button is pressed")
                return True
            else:
                return False