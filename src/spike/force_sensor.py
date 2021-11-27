from spike import simulator
import machine,time

class ForceSensor:
    #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #The PIN for Force Sensor (Potentiometer) ADC0
    FORCE_PIN_PORTA = 36
    FORCE_PIN_PORTB = 36
    FORCE_PIN_PORTC = 36
    FORCE_PIN_PORTD = 36
    FORCE_PIN_PORTE = 36
    FORCE_PIN_PORTF = 36
    #If the measured value is higher than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
    SIMULATORSWITCHMAX=80
    #If the measured value is lower than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
    SIMULATORSWITCHMIN=0
    
    
    def __init__(self,port):
        self.port = port
        forceLEDpin = self.FORCE_PIN_PORTA
        if port == 'A': forceLEDpin = self.FORCE_PIN_PORTA
        if port == 'B': forceLEDpin = self.FORCE_PIN_PORTB
        if port == 'C': forceLEDpin = self.FORCE_PIN_PORTC
        if port == 'D': forceLEDpin = self.FORCE_PIN_PORTD
        if port == 'E': forceLEDpin = self.FORCE_PIN_PORTE
        if port == 'F': forceLEDpin = self.FORCE_PIN_PORTF
        self.adc = machine.ADC(machine.Pin(forceLEDpin))
        self.FORCE_PIN_PORTA
        self.adc.atten(machine.ADC.ATTN_11DB)       #Full range: 3.3v
        self.newton = 0
        self.percentage = 0
        self.simulator = simulator.Simulator()
        if(self.ISDEBUG):print("ForceSensor->__init__(port=",port,"). Force sensor is initialised in debug mode. Force sensor PIN:",forceLEDpin,", Switching threshold: ",self.SIMULATORSWITCHMAX,"  Change at spike.force_sensor.py ")

    def get_force_newton(self):
        if(self.ISDEBUG):print("ForceSensor->get_force_newton(). Retrieves the measured force, in newtons.")
        self.newton = self.simulator.get_new_value(
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= self.adc.read(),
                                                                     minvalue= 0,
                                                                     maxvalue= 10,
                                                                     minreading=0,
                                                                     maxreading=4095)
        return self.newton
    
    def get_force_percentage(self):
        if(self.ISDEBUG):print("ForceSensor->get_force_percentage(). Retrieves the measured force, in percentages.")
        self.percentage = self.simulator.get_new_value(
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= self.adc.read(),
                                                                     minvalue= 0,
                                                                     maxvalue= 100,
                                                                     minreading=0,
                                                                     maxreading=4095)
        return self.percentage
        
    def is_pressed(self):
        if(self.ISDEBUG):print("ForceSensor->is_pressed(). Tests whether the button on the force sensor is pressed.")
        self.percentage = self.simulator.get_new_value(
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= self.adc.read(),
                                                                     minvalue= 0,
                                                                     maxvalue= 100,
                                                                     minreading=0,
                                                                     maxreading=4095)
        if self.percentage < self.SIMULATORSWITCHMAX :
            if(self.ISDEBUG):
                print("force sensor button is pressed")
                return True
            else:
                return False

    def wait_until_pressed(self):
        if(self.ISDEBUG):print("ForceSensor->wait_until_pressed(). Waits until the Force Sensor is pressed.")
        runwhile = True
        while runwhile:
            self.percentage = self.simulator.get_new_value(
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= self.adc.read(),
                                                                     minvalue= 0,
                                                                     maxvalue= 100,
                                                                     minreading=0,
                                                                     maxreading=4095)
            if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.percentage), " to exit it should be lower then:", self.SIMULATORSWITCHMIN , " or it should be higher then:", self.SIMULATORSWITCHMAX )
            if self.percentage < self.SIMULATORSWITCHMIN or self.percentage > self.SIMULATORSWITCHMAX : 
                runwhile = False
            else:
                time.sleep_ms(500)
    
    def wait_until_released(self):
        if(self.ISDEBUG):print("ForceSensor->wait_until_released(). Waits until the Force Sensor is released.")
        runwhile = True
        while runwhile:
            self.percentage = self.simulator.get_new_value(   
                                                                     isdebug=self.ISDEBUG,
                                                                     newreading= self.adc.read(),
                                                                     minvalue= 0,
                                                                     maxvalue= 100,
                                                                     minreading=0,
                                                                     maxreading=4095)
            if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.percentage), " to exit it should be higher or equal then:", self.SIMULATORSWITCHMIN , " or it should be lower or equal then:", self.SIMULATORSWITCHMAX )
            if self.percentage >= self.SIMULATORSWITCHMIN and self.percentage <= self.SIMULATORSWITCHMAX : 
                runwhile = False
            else:
                time.sleep_ms(500)