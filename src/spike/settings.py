#If ISDEBUG is true. then all modules send debug information through console
ISDEBUG = True

#If LIGHTMATRIXSIMULATE is true then the displayed result is written to the console. If false the display is used.
LIGHTMATRIXSIMULATE = False

#If MOTORSIMULATE is true then the status of the motor is stored in variables and written to the console. If false the motor is controlled by MOTORPIN
MOTORSIMULATE = False
#The PIN for Motor
MOTORPIN = 4

#If BUTTONSIMULATE is true it waits for a button to be pressed via the console, if false it monitors the state of the BUTTONPIN
BUTTONSIMULATE = False
#The PIN for Button D3 = GPIO0
BUTTONPIN = 0

#If SPEAKERSIMULATE is true ten it prints out the state of the speaker, if false it plays sound with changeing the SPEAKERPIN
SPEAKERSIMULATE = False
#The Pin for Speaker D4 = GPIO2
SPEAKERPIN = 2

#If FORCESENSORSIMULATE is true , if false it measures the ADC value of a potentiometer
FORCESENSORSIMULATE = False
#The PIN for Force Sensor (Potentiometer) ADC0
FORCESENSORPIN = 0
#Define the type of the Force Sensor simulator. Values:
#Circular: it increases the return value by FORCESENSORCHANGE, after reaching maximum value decreases by FORCESENSORCHANGE every time it is called
#Random: it returns with a random number beetwean the FORCESENSORMIN and FORCESENSORMAX
#Consol: it asks a value from consol. 
#FORCESENSORTYPE = "Circular"
FORCESENSORTYPE = "Random"
#FORCESENSORTYPE = "Consol"
#The return value of the Force Sensor will change by this number
FORCESENSORCHANGE = 10
#If the measured, simulated Force percentage value is lower than FORCESENSORSWITCH value then the Force Sensor is pressed
FORCESENSORSWITCH=80
