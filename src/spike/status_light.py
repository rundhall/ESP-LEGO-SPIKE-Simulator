import machine
from neopixel import NeoPixel

class Status_light:
    ISDEBUG = True
    #The PIN for LED 
    LEDPIN = 0
    #max LED number
    MAXLEDNUMBER = 8
    #actual LED ID
    LEDID = 0
    

    def __init__(self):
        if(self.ISDEBUG):print("Status_light->__init__(). Status light is initialised in debug mode.  LED PIN:",self.LEDPIN,", Maximum LED:",self.MAXLEDNUMBER ," LED ID:",self.LEDID," change at spike.status_light.py ")
        pin = machine.Pin(self.LEDPIN, machine.Pin.OUT)   # set GPIO0 to output to drive NeoPixels
        self.np = NeoPixel(pin, self.MAXLEDNUMBER)   # create NeoPixel driver 

    def on(self,color='white'):
        if(self.ISDEBUG):print("Status_light->on(color=",color,"). Sets the color of the light to: ",color)
        #"azure","black","blue","cyan","green","orange","pink","red","violet","yellow","white"
        if color=="azure":
            self.np[self.LEDID] = (0, 122, 255) # set the pixel
        if color=="black":
            self.np[self.LEDID] = (0, 0, 0) # set the pixel
        if color=="blue":
            self.np[self.LEDID] = (0, 0, 255) # set the pixel
        if color=="cyan":
            self.np[self.LEDID] = (0, 255, 255) # set the pixel
        if color=="green":
            self.np[self.LEDID] = (0, 255, 0) # set the pixel
        if color=="orange":
            self.np[self.LEDID] = (255, 122, 0) # set the pixel
        if color=="pink":
            self.np[self.LEDID] = (255, 0, 122) # set the pixel
        if color=="red":
            self.np[self.LEDID] = (255, 0, 0) # set the pixel
        if color=="violet":
            self.np[self.LEDID] = (122, 0, 255) # set the pixel
        if color=="yellow":
            self.np[self.LEDID] = (255, 255, 0) # set the pixel
        if color=="white":
            self.np[self.LEDID] = (255, 255, 255) # set the pixel
        self.np.write()     


    def off(self):
        if(self.ISDEBUG):print("Status_light->off(). Turns off the light.")
        self.np[self.LEDID] = (0, 0, 0) # set the pixel to black = off
        self.np.write() 
