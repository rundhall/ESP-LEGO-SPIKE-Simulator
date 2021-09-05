#If true then all modules send debug information through console
ISDEBUG = False
#If true then the status of the motor is stored in variables and written to the console. If false the motor is controlled by MOTORPIN
MOTORSIMULATE = False
#The PIN for Motor
MOTORPIN = 4
#If true it waits for a button to be pressed via the console, if false it monitors the state of the BUTTONPIN
BUTTONSIMULATE = False
#The PIN for Button D3 = GPIO0
BUTTONPIN = 0
#If true ten it prints out the state of the speaker, if false it plays sound with changeing the SPEAKERPIN
SPEAKERSIMULATE = False
#The Pin for Speaker D4 = GPIO2
SPEAKERPIN = 2
#If true it increases the return value by 1, after reaching maximum value decreases by 1 every time it is called, if false it measures the ADC value of a potentiometer
FORCESENSORSIMULATE = True
#The PIN for Force Sensor (Potentiometer) ADC0
FORCESENSORPIN = 0
