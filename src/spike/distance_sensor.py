import machine,random,time
from spike import hcsr04,simulator
from neopixel import NeoPixel

class DistanceSensor:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #If ISSIMULATION is true then the distance will change according to their type.
    #If false the distance is measured by HCSR04 Sensor triggered at DISTANCESENSORTRIGERPIN echoed at DISTANCESENSORECHOPIN
    ISSIMULATION = True
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
    #Define the type of the Distance simulator. Values:
    #Circular: it increases the return value by SIMULATORCHANGE, after reaching maximum value decreases by SIMULATORCHANGE every time it is called in while function it changes the value every second * SIMULATORTIME
    #Random: it returns random distance value
    #Consol: it asks for a value from the console.
    #SIMULATORTYPE = "Circular"
    SIMULATORTYPE = "Random"
    #SIMULATORTYPE = "Consol"
    
    #In Circular mode this is the time between changes
    SIMULATORTIME = 3
    #In Circular mode this the amount the distance value will change every period.
    SIMULATORCHANGE = 10
    #If the measured, simulated value is higher than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
    SIMULATORSWITCHMAX=80
    #If the measured, simulated value is lower than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
    SIMULATORSWITCHMIN=0
    
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
        self.distance_cm_direction = True
        self.distance_inches_direction = True
        self.distance_percentage_direction = True
        self.simulator = simulator.Simulator()
        if not self.ISSIMULATION:
            if port == 'A':
                pin = machine.Pin(self.LEDPIN_PORTA, machine.Pin.OUT)   # set output to drive NeoPixels
                self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTA, echo_pin=self.DISTANCE_ECHOPIN_PORTA)
            if port == 'B':
                pin = machine.Pin(self.LEDPIN_PORTB, machine.Pin.OUT)   # set output to drive NeoPixels
                self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTB, echo_pin=self.DISTANCE_ECHOPIN_PORTB)
            if port == 'C':
                pin = machine.Pin(self.LEDPIN_PORTC, machine.Pin.OUT)   # set output to drive NeoPixels
                self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTC, echo_pin=self.DISTANCE_ECHOPIN_PORTC)
            if port == 'D':
                pin = machine.Pin(self.LEDPIN_PORTD, machine.Pin.OUT)   # set output to drive NeoPixels
                self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTD, echo_pin=self.DISTANCE_ECHOPIN_PORTD)
            if port == 'E':
                pin = machine.Pin(self.LEDPIN_PORTE, machine.Pin.OUT)   # set output to drive NeoPixels
                self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTE, echo_pin=self.DISTANCE_ECHOPIN_PORTE)
            if port == 'F':
                pin = machine.Pin(self.LEDPIN_PORTF, machine.Pin.OUT)   # set output to drive NeoPixels
                self.distancesensor = hcsr04.HCSR04(trigger_pin=self.DISTANCE_TRIGERPIN_PORTF, echo_pin=self.DISTANCE_ECHOPIN_PORTF)
            self.np = NeoPixel(pin, self.MAXLEDNUMBER)   # create NeoPixel driver
            
        if(self.ISDEBUG):print("Distance sensor is initialised in debug mode. Simulation:",self.ISSIMULATION, " Button type:",self.SIMULATORTYPE ," change at spike.distance_sensor.py ")
  
    def get_new_measured_value(self):
        if not self.ISSIMULATION:
            return int(self.distancesensor.distance_cm())
        else:
            return None

    def light_up_all(self,brightness=100):
        if(self.ISDEBUG):print("Lights up all of the lights on the Distance Sensor at the specified brightness.brightness:",str(brightness))
        if self.ISSIMULATION:
            print("Simulated distance sensor light up the sensor light with the brightness:",str(brightness))
        else:
            self.np[self.LEDIDRIGHT_TOP] = (brightness, brightness, brightness) # set the pixel to black = off
            self.np[self.LEDIDLEFT_TOP] = (brightness, brightness, brightness) # set the pixel to black = off
            self.np[self.LEDIDRIGHT_BOTTOM] = (brightness, brightness, brightness) # set the pixel to black = off
            self.np[self.LEDIDLEFT_BOTTOM] = (brightness, brightness, brightness) # set the pixel to black = off
            self.np.write() 

    def light_up(self,right_top, left_top, right_bottom, left_bottom):
        if(self.ISDEBUG):print("Sets the brightness of the individual lights on the Distance Sensor. Light up by: right_top:",right_top," left_top:",left_top," right_bottom:",right_bottom," left_bottom:", left_bottom)
        if self.ISSIMULATION:
            print("Simulated distance sensor light up by: right_top:",right_top," left_top:",left_top," right_bottom:",right_bottom," left_bottom:", left_bottom)
        else:
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
        if(self.ISDEBUG):print("Retrieves the measured distance in centimeters.")
        self.distance_cm, self.distance_cm_direction = self.simulator.get_new_value(issimulation=self.ISSIMULATION,
                                                                             simulationtype=self.SIMULATORTYPE,
                                                                             isdebug=self.ISDEBUG,
                                                                             actualvalue= self.distance_cm,
                                                                             newreading= self.get_new_measured_value(),
                                                                             minvalue= 0,
                                                                             maxvalue= 200,
                                                                             name= "distance sensor distance_cm",
                                                                             direction= self.distance_cm_direction,
                                                                             change= self.SIMULATORCHANGE,
                                                                             iswait= False,
                                                                             switch_min= self.SIMULATORSWITCHMIN,
                                                                             switch_max=self.SIMULATORSWITCHMAX,
                                                                             isextern= False,
                                                                             minreading=0,
                                                                             maxreading=200)
        return self.distance_cm
        
    def get_distance_inches(self,short_range=False):
        if(self.ISDEBUG):print("Retrieves the measured distance in inches.")
        self.distance_inches, self.distance_inches_direction = self.simulator.get_new_value(issimulation=self.ISSIMULATION,
                                                                     simulationtype=self.SIMULATORTYPE,
                                                                     isdebug=self.ISDEBUG,
                                                                     actualvalue= self.distance_inches,
                                                                     newreading= self.get_new_measured_value(),
                                                                     minvalue= 0,
                                                                     maxvalue= 79,
                                                                     name= "distance sensor distance_inches",
                                                                     direction= self.distance_inches_direction,
                                                                     change= self.SIMULATORCHANGE,
                                                                     iswait= False,
                                                                     switch_min= self.SIMULATORSWITCHMIN,
                                                                     switch_max=self.SIMULATORSWITCHMAX,
                                                                     isextern= False,
                                                                     minreading=0,
                                                                     maxreading=200)
        return self.distance_inches
        
    def get_distance_percentage(self,short_range=False):
        if(self.ISDEBUG):print("Retrieves the measured distance as a percentage.")
        self.distance_percentage, self.distance_percentage_direction = self.simulator.get_new_value(issimulation=self.ISSIMULATION,
                                                                     simulationtype=self.SIMULATORTYPE,
                                                                     isdebug=self.ISDEBUG,
                                                                     actualvalue= self.distance_percentage,
                                                                     newreading= self.get_new_measured_value(),
                                                                     minvalue= 0,
                                                                     maxvalue= 100,
                                                                     name= "distance sensor distance_percentage",
                                                                     direction= self.distance_percentage_direction,
                                                                     change= self.SIMULATORCHANGE,
                                                                     iswait= False,
                                                                     switch_min= self.SIMULATORSWITCHMIN,
                                                                     switch_max=self.SIMULATORSWITCHMAX,
                                                                     isextern= False,
                                                                     minreading=0,
                                                                     maxreading=200)
        return self.distance_percentage
   
   
   
    def wait_for_distance_farther_than(self,distance=100, unit='cm', short_range=False):
        if(self.ISDEBUG):print("Waits until the measured distance is less than the specified distance.")
        maxvalue_unit = 100
        if unit == "cm":
            maxvalue_unit = 200
        if unit == "in":
            maxvalue_unit = 78
        if unit == "%":
            maxvalue_unit = 100
        runwhile = True
        while runwhile:
            self.distance_cm, self.distance_cm_direction = self.simulator.get_new_value(   issimulation=self.ISSIMULATION,
                                                                     simulationtype=self.SIMULATORTYPE,
                                                                     isdebug=self.ISDEBUG,
                                                                     actualvalue= self.distance_cm,
                                                                     newreading= self.get_new_measured_value(),
                                                                     minvalue= 0,
                                                                     maxvalue= maxvalue_unit,
                                                                     name= "distance closer than",
                                                                     direction= self.distance_cm_direction,
                                                                     change= self.SIMULATORCHANGE,
                                                                     iswait= True,
                                                                     switch_min= 0,
                                                                     switch_max=distance,
                                                                     isextern= False,
                                                                     time_period= self.SIMULATORTIME,
                                                                     minreading=0,
                                                                     maxreading=200)
            if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.distance_cm), " to exit it should be lower then:", 0, " or it should be higher then:", distance )
            if self.distance_cm < 0 or self.distance_cm > distance : 
                runwhile = False
            else:
                time.sleep_ms(500)
        return self.distance_cm
    
    def wait_for_distance_closer_than(self,distance=100, unit='cm', short_range=False):
        maxvalue_unit = 100
        if unit == "cm":
            maxvalue_unit = 200
        if unit == "in":
            maxvalue_unit = 78
        if unit == "%":
            maxvalue_unit = 100
        runwhile = True
        while runwhile:
            self.distance_cm, self.distance_cm_direction = self.simulator.get_new_value(   issimulation=self.ISSIMULATION,
                                                                     simulationtype=self.SIMULATORTYPE,
                                                                     isdebug=self.ISDEBUG,
                                                                     actualvalue= self.distance_cm,
                                                                     newreading= self.get_new_measured_value(),
                                                                     minvalue= 0,
                                                                     maxvalue= maxvalue_unit,
                                                                     name= "distance closer than",
                                                                     direction= self.distance_cm_direction,
                                                                     change= self.SIMULATORCHANGE,
                                                                     iswait= True,
                                                                     switch_min= 0,
                                                                     switch_max=distance,
                                                                     isextern= True,
                                                                     time_period= self.SIMULATORTIME,
                                                                     minreading=0,
                                                                     maxreading=200)
            if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.distance_cm), " to exit it should be lower then:", 0, " or it should be higher then:", distance )
            if self.distance_cm > 0 and self.distance_cm < distance : 
                runwhile = False
            else:
                time.sleep_ms(500)
        return self.distance_cm
