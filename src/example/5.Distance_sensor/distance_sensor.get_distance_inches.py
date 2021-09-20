get_distance_inches(short_range=False)
Gets the measured distance in inches.
Parameters
short_range
Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
Type
:
boolean
Values
:
True or False
Default
:
False
Returns
The measured distance or "none" if the distance can't be measured.
Type
:
float (decimal number)
Values
:
any value between 0 and 79
Errors
TypeError
short_range is not a boolean.
RuntimeError
The sensor has been disconnected from the Port.
Events
