from spike import mpu6050,simulator,machine
import time



class Motion_sensor:
     #If ISDEBUG is true. then all modules send debug information through console
    ISDEBUG = True
    #The PIN for Sensor I2C sda
    I2CSDAPIN = 21
    #The PIN for Sensor I2C scl
    I2CSCLPIN = 22
    
    def __init__(self):
        self.gesture_array = [None,'shaken','tapped','doubletapped','falling']
        self.gesture_index = 0
        
        self.orientation_array = [None,'front','back','up','down','leftside','rightside']
        self.orientation_index = 0
        
        self.pitch_angle = 0
        
        self.roll_angle = 0
        
        self.yaw_angle = 0
        
        self.yaw = 0.0
        self.pitch = 0.0
        self.roll = 0.0
        self.timeStep = 0.01
                
        self.simulator = simulator.Simulator()
        try:
            self.sensor = mpu6050.accel(machine.SoftI2C(sda=machine.Pin(self.I2CSDAPIN), scl=machine.Pin(self.I2CSCLPIN)))
        except OSError:
            print("mpu6050 motion sensor is not working or not connected. Connect it or change this file: spike.motion_sensor.py")
            machine.soft_reset()
       
        if(self.ISDEBUG):print("Motion_sensor->__init__(). Motion sensor is initialised in debug mode. Motion sensor i2c data PIN is:",self.I2CSDAPIN,", i2c clock PIN is:",self.I2CSCLPIN,". Change at spike.motion_sensor.py ")
    
        
    def get_yaw_angle(self):
       if(self.ISDEBUG):print("Motion_sensor->get_yaw_angle(). Retrieves the Hub’s yaw angle.")
       self.yaw = self.yaw + self.sensor.get_values()['GyZ'] * self.timeStep
       self.yaw_angle = self.simulator.get_new_value(
                                                                             isdebug=self.ISDEBUG,
                                                                             newreading= self.yaw,
                                                                             minvalue= -180,
                                                                             maxvalue= 180,
                                                                             minreading=-180,
                                                                             maxreading=180)
       return self.yaw_angle
    
    def get_roll_angle(self):
       if(self.ISDEBUG):print("Motion_sensor->get_roll_angle(). Retrieves the Hub’s roll angle.")
       self.roll = self.roll + self.sensor.get_values()['GyX'] * self.timeStep
       self.roll_angle = self.simulator.get_new_value(
                                                                                isdebug=self.ISDEBUG,
                                                                                newreading= self.roll,
                                                                                minvalue= -180,
                                                                                maxvalue= 180,
                                                                                minreading=-180,
                                                                                maxreading=180)
       return self.roll_angle
    
    def get_pitch_angle(self):
       if(self.ISDEBUG):print("Motion_sensor->get_pitch_angle(). Retrieves the Hub’s pitch angle.")
       self.pitch = self.pitch + self.sensor.get_values()['GyX'] * self.timeStep
       self.pitch_angle = self.simulator.get_new_value(                                                                                isdebug=self.ISDEBUG,
                                                                                newreading= self.pitch,
                                                                                minvalue= -180,
                                                                                maxvalue= 180,
                                                                                minreading=-180,
                                                                                maxreading=180)
       return self.pitch_angle
    
    def get_gesture(self):
        if(self.ISDEBUG):print("Motion_sensor->get_gesture(). Retrieves the most recently-detected gesture. Not implemented correctly it changes by pitch value")
        self.pitch = self.pitch + self.sensor.get_values()['GyX'] * self.timeStep
        self.gesture_index = self.simulator.get_new_value(  
                                                                             isdebug=self.ISDEBUG,
                                                                             newreading= self.pitch,
                                                                             minvalue= 0,
                                                                             maxvalue= 4,
                                                                             minreading=-180,
                                                                             maxreading=180)
        return self.gesture_array[self.gesture_index]
        
    def get_orientation(self):
        if(self.ISDEBUG):print("Motion_sensor->get_orientation(). Retrieves the Hub's current orientation. Not implemented correctly it changes by pitch value")
        self.pitch = self.pitch + self.sensor.get_values()['GyX'] * self.timeStep
        self.orientation_index = self.simulator.get_new_value(   isdebug=self.ISDEBUG,
                                                                             newreading= self.pitch,
                                                                             minvalue= 0,
                                                                             maxvalue= 6,
                                                                             minreading=-180,
                                                                             maxreading=180)
        return self.orientation_array[self.orientation_index]
    
   
    
    def reset_yaw_angle(self):
        if(self.ISDEBUG):print("Motion_sensor->reset_yaw_angle(). Sets the yaw angle to 0.")
        self.yaw_angle = 0
        self.yaw = 0

    def wait_for_new_orientation(self):
        #next line is not correct implementation it should be changed later
        self.orientation_index = int(self.remap(self.pitch, -180, 180, 0, 6))
        if(self.ISDEBUG):print("Motion_sensor->wait_for_new_orientation(). Waits until the Hub’s orientation changes. Orientation at start:",self.orientation_array[self.orientation_index],". Not implemented correctly it changes by pitch value")
        runwhile = True
        while runwhile:
            old_orientation_index = self.orientation_index
            self.pitch = self.pitch + self.sensor.get_values()['GyX'] * self.timeStep
            self.orientation_index = self.simulator.get_new_value(
                                                                            isdebug=self.ISDEBUG,
                                                                             newreading= self.pitch,
                                                                             minvalue= 0,
                                                                             maxvalue= 6,
                                                                             minreading=-180,
                                                                             maxreading=180)
            if self.orientation_index > old_orientation_index or self.orientation_index < old_orientation_index:
                runwhile = False
            else:
                time.sleep_ms(500)
            old_orientation_index = self.orientation_index
        return self.orientation_array[self.orientation_index]
    
    def wait_for_new_gesture(self):
        #next line is not correct implementation it should be changed later
        self.gesture_index = int(self.remap(self.pitch, -180, 180, 0, 4))
        if(self.ISDEBUG):print("Motion_sensor->wait_for_new_gesture(). Waits until the Hub’s gesture changes. Gesture at start:",self.gesture_array[self.gesture_index],". Not implemented correctly it changes by pitch value")
        runwhile = True
        
        while runwhile:
            old_gesture_index = self.gesture_index
            self.pitch = self.pitch + self.sensor.get_values()['GyX'] * self.timeStep
            self.gesture_index = self.simulator.get_new_value(
                                                                            isdebug=self.ISDEBUG,
                                                                             newreading= self.pitch,
                                                                             minvalue= 0,
                                                                             maxvalue= 6,
                                                                             minreading=-180,
                                                                             maxreading=180)
            
            if self.gesture_index > old_gesture_index or self.gesture_index < old_gesture_index:
                runwhile = False
            else:
                time.sleep_ms(500)
            old_gesture_index = self.gesture_index
        return self.gesture_array[self.gesture_index]
    
    def remap(self,x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def was_gesture(self,gesture):
        if(self.ISDEBUG):print("Motion_sensor->was_gesture(gesture=",gesture,"). Tests whether a gesture has occurred since the last time was_gesture() was used, or since the beginning of the program (for the first use). Not implemented correctly it changes by pitch value")
        self.pitch = self.pitch + self.sensor.get_values()['GyX'] * self.timeStep
        self.gesture_index = self.simulator.get_new_value(                   isdebug=self.ISDEBUG,
                                                                             newreading= self.pitch,
                                                                             minvalue= 0,
                                                                             maxvalue= 6,
                                                                             minreading=-180,
                                                                             maxreading=180)
        if gesture == self.gesture_array[self.gesture_index]: 
            return True
        else:
            return False

