import machine,time,random

class Left_button:
    ISDEBUG = True
    #The PIN for Button D3 = GPIO0
    BUTTONPIN = 15

    def __init__(self):
         self.buttonlast = 0
         self.buttonpin = machine.Pin(self.BUTTONPIN, machine.Pin.IN, machine.Pin.PULL_UP)
         if(self.ISDEBUG):print("Left_button->__init__(). Left button is initialised in debug mode. Left button PIN is:",self.BUTTONPIN,". Change at spike.left_button.py ")
         self.time = time.ticks_ms()
         
    def wait_until_pressed(self):
        if(self.ISDEBUG):print("Left_button->wait_until_pressed(). Waits until the left button is pressed.")
        while self.buttonpin.value()==1:
            if(self.ISDEBUG):print("push the left button")
        if(self.ISDEBUG):print("left button is pressed")
    
    def wait_until_released(self):
        if(self.ISDEBUG):print("Left_button->wait_until_released(). Waits until the left button is released.")
        while self.buttonpin.value()==0:
            if(self.ISDEBUG):print("release the left button")
        if(self.ISDEBUG):print("left button is released")
        
    def was_pressed(self):
        if(self.ISDEBUG):print("Left_button->was_pressed(). Tests to see whether the left button has been pressed since the last time this method called.")
        if self.buttonpin.value()==0:
            if self.buttonlast == 1:
                if(self.ISDEBUG):print("left button has been pressed since the last time")
                self.buttonlast = 0
                return True
            else:
                return False
        else:
            self.buttonlast = 1
            return False
    
    def is_pressed(self):
        if(self.ISDEBUG):print("Left_button->is_pressed(). Tests whether the left button is pressed.")
        if self.buttonpin.value()==0:
            if(self.ISDEBUG):print("left button is pressed")
            return True
        else:
            return False
