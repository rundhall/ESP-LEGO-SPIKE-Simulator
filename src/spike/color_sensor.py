from spike import tcs34725,simulator,machine
import time
from neopixel import NeoPixel
# or from spike.tcs34725 import TCS34725



class ColorSensor:
     #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #The PIN for Sensor I2C sda
    I2CSDAPIN = 21
    #The PIN for Sensor I2C scl
    I2CSCLPIN = 22
    
    #The PIN for LED 
    LEDPIN_PORTA = 0
    LEDPIN_PORTB = 0
    LEDPIN_PORTC = 0
    LEDPIN_PORTD = 0
    LEDPIN_PORTE = 0
    LEDPIN_PORTF = 0
    #max LED number
    MAXLEDNUMBER = 8
    #actual LED ID for light_1
    LEDIDLIGHT1 = 5
    #actual LED ID for light_2
    LEDIDLIGHT2 = 6
    #actual LED ID for light_3
    LEDIDLIGHT3 = 7
    
    def __init__(self,port):
        self.port = port
        self.colors_array = [None,'black','violet','blue','cyan','green','yellow','red','white']
        self.color_index = 0
        
        self.ambient_light = 0 #0..100
        self.reflected_light = 0 #0..100
        self.rgb_intensity = 0 #0..1024
        self.red = 0 #0..1024
        self.green = 0 #0..1024
        self.blue = 0 #0..1024
        self.simulator = simulator.Simulator()
        usedLEDpin = self.LEDPIN_PORTA
        if port == 'A': usedLEDpin = self.LEDPIN_PORTA 
        if port == 'B': usedLEDpin = self.LEDPIN_PORTB 
        if port == 'C': usedLEDpin = self.LEDPIN_PORTC 
        if port == 'D': usedLEDpin = self.LEDPIN_PORTD
        if port == 'E': usedLEDpin = self.LEDPIN_PORTE 
        if port == 'F': usedLEDpin = self.LEDPIN_PORTF 
        pin = machine.Pin(usedLEDpin, machine.Pin.OUT)   # set output to drive NeoPixels
        self.np = NeoPixel(pin, self.MAXLEDNUMBER)   # create NeoPixel driver 
        try:
            self.sensor = tcs34725.TCS34725(machine.SoftI2C(sda=machine.Pin(self.I2CSDAPIN), scl=machine.Pin(self.I2CSCLPIN)))
            self.sensor.active(True)
        except OSError:
            print("tcs34725 sensor is not working or not connected. Connect the tcs34725 sensor or change this file: spike.color_sensor.py")
            machine.soft_reset()
        if(self.ISDEBUG):print("ColorSensor->__init__(port=",port,"). Color Sensor is initialised in debug mode. Color sensor i2c data PIN is:",self.I2CSDAPIN,", i2c clock PIN is:",self.I2CSCLPIN,". LED PIN is: ",usedLEDpin,". Change at spike.color_sensor.py ")
    
        
    def get_ambient_light(self):
       if(self.ISDEBUG):print("ColorSensor->get_ambient_light() Retrieves the intensity of the ambient light.")
       self.ambient_light = self.simulator.get_new_value(
                                                                             isdebug=self.ISDEBUG,
                                                                             newreading= self.sensor.read()[1],
                                                                             minvalue= 0,
                                                                             maxvalue= 100,
                                                                             minreading=0,
                                                                             maxreading=100)
       return self.ambient_light

    def get_blue(self):
        if(self.ISDEBUG):print("ColorSensor->get_blue() Retrieves the color intensity of blue.")
        self.blue = self.simulator.get_new_value( 
                                                             isdebug=self.ISDEBUG,
                                                             newreading= int(self.sensor.read(True)[2]),
                                                             minvalue= 0,
                                                             maxvalue= 1024,
                                                             minreading=0,
                                                             maxreading=50)
        return self.blue
    
    def get_green(self):
        if(self.ISDEBUG):print("ColorSensor->get_green() Retrieves the color intensity of green.")
        self.green = self.simulator.get_new_value(
                                                                 isdebug=self.ISDEBUG,
                                                                 newreading= int(self.sensor.read(True)[1]),
                                                                 minvalue= 0,
                                                                 maxvalue= 1024,
                                                                 minreading=0,
                                                                 maxreading=50)
        return self.green
    
    def get_red(self):
        if(self.ISDEBUG):print("ColorSensor->get_red() Retrieves the color intensity of red.")
        self.red = self.simulator.get_new_value(   
                                                             isdebug=self.ISDEBUG,
                                                             newreading= self.sensor.read(True)[0],
                                                             minvalue= 0,
                                                             maxvalue= 1024,
                                                             minreading=0,
                                                             maxreading=50)
        return self.red
    
    def get_color(self):
        if(self.ISDEBUG):print("ColorSensor->get_color() Retrieves the detected color of a surface.")
        self.color_index = self.simulator.get_new_value(
                                                                             isdebug=self.ISDEBUG,
                                                                             newreading= self.sensor.get_color_index(self.sensor.read(True)),
                                                                             minvalue= 0,
                                                                             maxvalue= 8,
                                                                             minreading=0,
                                                                             maxreading=8)
        return self.colors_array[self.color_index]
        
    def get_reflected_light(self):
        if(self.ISDEBUG):print("ColorSensor->get_reflected_light() Retrieves the intensity of the reflected light.")
        #self.reflected_light = 0 #0..100
        self.reflected_light = self.simulator.get_new_value(
                                                                                     isdebug=self.ISDEBUG,
                                                                                     newreading= self.sensor.read(True)[3],
                                                                                     minvalue= 0,
                                                                                     maxvalue= 100,
                                                                                     minreading=0,
                                                                                     maxreading=50)
        return self.reflected_light
    
    def get_rgb_intensity(self):
        #self.rgb_intensity = 0 #0..1024
        if(self.ISDEBUG):print("ColorSensor->get_rgb_intensity() Retrieves the overall color intensity, and intensity of rgb_intensity, green, and blue.")
        self.rgb_intensity = self.simulator.get_new_value(
                                                                                 isdebug=self.ISDEBUG,
                                                                                 newreading= self.sensor.read()[0],
                                                                                 minvalue= 0,
                                                                                 maxvalue= 1024,
                                                                                 minreading=0,
                                                                                 maxreading=50)
        return self.rgb_intensity
    
    def light_up(self,light_1, light_2, light_3):
        if(self.ISDEBUG):print("ColorSensor->light_up(light_1=",str(light_1),", light_2=",str(light_2),", light_3=",str(light_3),") Sets the brightness of the individual lights on the Color Sensor. ")
        self.np[self.LEDIDLIGHT1] = (light_1, light_1, light_1) # set the pixel 
        self.np[self.LEDIDLIGHT2] = (light_2, light_2, light_2) # set the pixel
        self.np[self.LEDIDLIGHT3] = (light_3, light_3, light_3) # set the pixel
        self.np.write() 
        
    def light_up_all(self,brightness=100):
        if(self.ISDEBUG):print("ColorSensor->light_up_all(brightness=",str(brightness),"). Lights up all of the lights on the Color Sensor at the specified brightness. ")
        self.np[self.LEDIDLIGHT1] = (brightness, brightness, brightness) # set the pixel 
        self.np[self.LEDIDLIGHT2] = (brightness, brightness, brightness) # set the pixel
        self.np[self.LEDIDLIGHT3] = (brightness, brightness, brightness) # set the pixel
        self.np.write()
            
    def wait_for_new_color(self):
        self.color_index = self.sensor.get_color_index(self.sensor.read(True))
        if(self.ISDEBUG):print("ColorSensor->wait_for_new_color() Waits until the Color Sensor detects a new color. Color at start:",self.colors_array[self.color_index])
        runwhile = True
        while runwhile:
            old_color_index = self.color_index
            self.color_index = self.simulator.get_new_value(
                                                             isdebug=self.ISDEBUG,
                                                             newreading= self.sensor.get_color_index(self.sensor.read(True)),
                                                             minvalue= 0,
                                                             maxvalue= 8,
                                                             minreading=0,
                                                             maxreading=8)
            if(self.ISDEBUG):print("Do changes at color sensor new reading:", str(self.color_index), " to exit it should be lower then:", self.color_index , " or it should be higher then:", self.color_index )
            if self.color_index > old_color_index or self.color_index < old_color_index:
                runwhile = False
            else:
                time.sleep_ms(500)
            old_color_index = self.color_index
        return self.colors_array[self.color_index]
    
    def wait_until_color(self,color):
        if color == 'black':
            old_color_index = 0
        if color=='violet':
            old_color_index = 1
        if color == 'blue':
            old_color_index = 2
        if color=='violet':
            old_color_index = 3
        if color == 'cyan':
            old_color_index = 4
        if color=='green':
            old_color_index = 5
        if color == 'yellow':
            old_color_index = 6
        if color=='red':
            old_color_index = 7
        if color=='white':
            old_color_index = 8    
        if(self.ISDEBUG):print("ColorSensor->wait_until_color(color=",color,") Waits until the Color Sensor detects the specified color.")
        runwhile = True
        while runwhile:
            self.color_index = self.simulator.get_new_value(   
                                                             isdebug=self.ISDEBUG,
                                                             newreading= self.sensor.get_color_index(self.sensor.read(True)),
                                                             minvalue= 0,
                                                             maxvalue= 8,
                                                             minreading=0,
                                                             maxreading=8)
            if(self.ISDEBUG):print("Do changes at color sensor new reading:", str(self.color_index), " to exit it should be higher or equal then:", old_color_index , " or it should be lower or equal then:", old_color_index )
            if self.color_index == old_color_index: 
                runwhile = False
            else:
                time.sleep_ms(500)
        return 
        
