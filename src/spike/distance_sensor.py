import machine,random,time
from spike import hcsr04,simulator
from neopixel import NeoPixel

class DistanceSensor:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #The PIN for HCSR04 Sensor trigger
    DISTANCE_TRIGERPIN_PORTA = 14
    #The PIN for HCSR04 Sensor echo
    DISTANCE_ECHOPIN_PORTA = 12
    DISTANCE_TRIGERPIN_PORTB = 14
    DISTANCE_ECHOPIN_PORTB = 12
    DISTANCE_TRIGERPIN_PORTC = 14
    DISTANCE_ECHOPIN_PORTC = 12
    DISTANCE_TRIGERPIN_PORTD = 14
    DISTANCE_ECHOPIN_PORTD = 12
    DISTANCE_TRIGERPIN_PORTE = 14
    DISTANCE_ECHOPIN_PORTE = 12
    DISTANCE_TRIGERPIN_PORTF = 14
    DISTANCE_ECHOPIN_PORTF = 12

    
    #The PIN for LED 
    LEDPIN_PORTA = 0
    LEDPIN_PORTB = 0
    LEDPIN_PORTC = 0
    LEDPIN_PORTD = 0
    LEDPIN_PORTE = 0
    LEDPIN_PORTF = 0
    #max LED number
    MAXLEDNUMBER = 8
    #actual LED ID for right_top
    LEDIDRIGHT_TOP = 1
    #actual LED ID for left_top
    LEDIDLEFT_TOP = 2
    #actual LED ID for right_bottom
    LEDIDRIGHT_BOTTOM = 3
    #actual LED ID for left_bottom
    LEDIDLEFT_BOTTOM = 4
    
    def __init__(self,port):
        self.port = port
        self.distance_cm =0
        self.distance_inches =0
        self.distance_percentage =0

        self.simulator = simulator.Simulator()
        if port == 'A':
            pin = machine.Pin(self.LEDPIN_PORTA, machine.Pin.OUT)   # set output to drive NeoPixels
            self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTA, echo_pin=self.DISTANCE_ECHOPIN_PORTA)
            if(self.ISDEBUG):print("DistanceSensor->__init__(port=",port,"). Distance sensor is initialised in debug mode. Distance sensor trigger PIN:",self.DISTANCE_TRIGERPIN_PORTA,", echo PIN:",self.DISTANCE_ECHOPIN_PORTA,", LED PIN:",self.LEDPIN_PORTA,". Change at spike.distance_sensor.py ")
        if port == 'B':
            pin = machine.Pin(self.LEDPIN_PORTB, machine.Pin.OUT)   # set output to drive NeoPixels
            self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTB, echo_pin=self.DISTANCE_ECHOPIN_PORTB)
            if(self.ISDEBUG):print("DistanceSensor->__init__(port=",port,"). Distance sensor is initialised in debug mode. Distance sensor trigger PIN:",self.DISTANCE_TRIGERPIN_PORTB,", echo PIN:",self.DISTANCE_ECHOPIN_PORTB,", LED PIN:",self.LEDPIN_PORTB,". Change at spike.distance_sensor.py ")
        if port == 'C':
            pin = machine.Pin(self.LEDPIN_PORTC, machine.Pin.OUT)   # set output to drive NeoPixels
            self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTC, echo_pin=self.DISTANCE_ECHOPIN_PORTC)
            if(self.ISDEBUG):print("DistanceSensor->__init__(port=",port,"). Distance sensor is initialised in debug mode. Distance sensor trigger PIN:",self.DISTANCE_TRIGERPIN_PORTC,", echo PIN:",self.DISTANCE_ECHOPIN_PORTC,", LED PIN:",self.LEDPIN_PORTC,". Change at spike.distance_sensor.py ")
        if port == 'D':
            pin = machine.Pin(self.LEDPIN_PORTD, machine.Pin.OUT)   # set output to drive NeoPixels
            self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTD, echo_pin=self.DISTANCE_ECHOPIN_PORTD)
            if(self.ISDEBUG):print("DistanceSensor->__init__(port=",port,"). Distance sensor is initialised in debug mode. Distance sensor trigger PIN:",self.DISTANCE_TRIGERPIN_PORTD,", echo PIN:",self.DISTANCE_ECHOPIN_PORTD,", LED PIN:",self.LEDPIN_PORTD,". Change at spike.distance_sensor.py ")
        if port == 'E':
            pin = machine.Pin(self.LEDPIN_PORTE, machine.Pin.OUT)   # set output to drive NeoPixels
            self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTE, echo_pin=self.DISTANCE_ECHOPIN_PORTE)
            if(self.ISDEBUG):print("DistanceSensor->__init__(port=",port,"). Distance sensor is initialised in debug mode. Distance sensor trigger PIN:",self.DISTANCE_TRIGERPIN_PORTE,", echo PIN:",self.DISTANCE_ECHOPIN_PORTE,", LED PIN:",self.LEDPIN_PORTE,". Change at spike.distance_sensor.py ")
        if port == 'F':
            pin = machine.Pin(self.LEDPIN_PORTF, machine.Pin.OUT)   # set output to drive NeoPixels
            self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTF, echo_pin=self.DISTANCE_ECHOPIN_PORTF)
            if(self.ISDEBUG):print("DistanceSensor->__init__(port=",port,"). Distance sensor is initialised in debug mode. Distance sensor trigger PIN:",self.DISTANCE_TRIGERPIN_PORTF,", echo PIN:",self.DISTANCE_ECHOPIN_PORTF,", LED PIN:",self.LEDPIN_PORTF,". Change at spike.distance_sensor.py ")

        self.np = NeoPixel(pin, self.MAXLEDNUMBER)   # create NeoPixel driver
            
        
  
    def light_up_all(self,brightness=100):
        if(self.ISDEBUG):print("DistanceSensor->light_up_all(brightness=",str(brightness),"). Lights up all of the lights on the Distance Sensor at the specified brightness.")
        self.np[self.LEDIDRIGHT_TOP] = (brightness, brightness, brightness) # set the pixel to black = off
        self.np[self.LEDIDLEFT_TOP] = (brightness, brightness, brightness) # set the pixel to black = off
        self.np[self.LEDIDRIGHT_BOTTOM] = (brightness, brightness, brightness) # set the pixel to black = off
        self.np[self.LEDIDLEFT_BOTTOM] = (brightness, brightness, brightness) # set the pixel to black = off
        self.np.write() 

    def light_up(self,right_top, left_top, right_bottom, left_bottom):
        if(self.ISDEBUG):print("DistanceSensor->light_up(right_top=",str(right_top),", left_top=",str(left_top),", right_bottom=",str(right_bottom),", left_bottom=",str(left_bottom),"). Sets the brightness of the individual lights on the Distance Sensor.")
        self.np[self.LEDIDRIGHT_TOP] = (right_top, right_top, right_top) # set the pixel to black = off
        self.np[self.LEDIDLEFT_TOP] = (left_top, left_top, left_top) # set the pixel to black = off
        self.np[self.LEDIDRIGHT_BOTTOM] = (right_bottom, right_bottom, right_bottom) # set the pixel to black = off
        self.np[self.LEDIDLEFT_BOTTOM] = (left_bottom, left_bottom, left_bottom) # set the pixel to black = off
        self.np.write() 

    '''
    get_distance_cm: Retrieves the measured distance in centimeters.
    Parameters:    short_range
    Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
    Type    :    boolean
    Values    :    True or False
    Default    :    False
    Returns    The measured distance or "none" if the distance can't be measured.
    Type    :    float (decimal number)
    Values    :    0 to 200 cm'''
    
    def get_distance_cm(self,short_range=False):
        if(self.ISDEBUG):print("DistanceSensor->get_distance_cm(short_range=",short_range,"). Retrieves the measured distance in centimeters.")
        self.distance_cm = self.simulator.get_new_value(
                                                                             isdebug=self.ISDEBUG,
                                                                             newreading= int(self.distancesensor.distance_cm()),
                                                                             minvalue= 0,
                                                                             maxvalue= 200,
                                                                             minreading=0,
                                                                             maxreading=200)
        return self.distance_cm
        
    def get_distance_inches(self,short_range=False):
        if(self.ISDEBUG):print("DistanceSensor->get_distance_inches(short_range=",short_range,"). Retrieves the measured distance in inches.")
        self.distance_inches = self.simulator.get_new_value(
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= int(self.distancesensor.distance_cm()),
                                                                     minvalue= 0,
                                                                     maxvalue= 79,
                                                                     minreading=0,
                                                                     maxreading=200)
        return self.distance_inches
        
    def get_distance_percentage(self,short_range=False):
        if(self.ISDEBUG):print("DistanceSensor->get_distance_percentage(short_range=",short_range,"). Retrieves the measured distance as a percentage.")
        self.distance_percentage = self.simulator.get_new_value(
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading=int(self.distancesensor.distance_cm()), 
                                                                     minvalue= 0,
                                                                     maxvalue= 100,
                                                                     minreading=0,
                                                                     maxreading=200)
        return self.distance_percentage
   
   
   
    def wait_for_distance_farther_than(self,distance=100, unit='cm', short_range=False):
        if(self.ISDEBUG):print("DistanceSensor->wait_for_distance_farther_than(distance=",distance,",unit=",unit,",short_range=",short_range,"). Waits until the measured distance is less than the specified distance.")
        maxvalue_unit = 100
        if unit == "cm":
            maxvalue_unit = 200
        if unit == "in":
            maxvalue_unit = 78
        if unit == "%":
            maxvalue_unit = 100
        runwhile = True
        while runwhile:
            self.distance_cm = self.simulator.get_new_value(
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= int(self.distancesensor.distance_cm()),
                                                                     minvalue= 0,
                                                                     maxvalue= maxvalue_unit,
                                                                     minreading=0,
                                                                     maxreading=200)
            if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.distance_cm), " to exit it should be lower then:", 0, " or it should be higher then:", distance )
            if self.distance_cm < 0 or self.distance_cm > distance : 
                runwhile = False
            else:
                time.sleep_ms(500)
        return self.distance_cm
    
    def wait_for_distance_closer_than(self,distance=100, unit='cm', short_range=False):
        if(self.ISDEBUG):print("DistanceSensor->wait_for_distance_closer_than(distance=",distance,",unit=",unit,",short_range=",short_range,"). Waits until the measured distance is less than the specified distance.")
        maxvalue_unit = 100
        if unit == "cm":
            maxvalue_unit = 200
        if unit == "in":
            maxvalue_unit = 78
        if unit == "%":
            maxvalue_unit = 100
        runwhile = True
        while runwhile:
            self.distance_cm = self.simulator.get_new_value(   
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= int(self.distancesensor.distance_cm()),
                                                                     minvalue= 0,
                                                                     maxvalue= maxvalue_unit,
                                                                     minreading=0,
                                                                     maxreading=200)
            if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.distance_cm), " to exit it should be lower then:", 0, " or it should be higher then:", distance )
            if self.distance_cm > 0 and self.distance_cm < distance : 
                runwhile = False
            else:
                time.sleep_ms(500)
        return self.distance_cm
