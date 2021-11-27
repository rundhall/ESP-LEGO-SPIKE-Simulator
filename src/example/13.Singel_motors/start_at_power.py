'''start_at_power(power)
Starts rotating the motor at a specified power level.
The motor will keep moving at this power level until you give it another motor command or when your program ends.
Parameters
power
Power of the motor.
Type:integer (a positive or negative whole number, including 0)
Values:-100% to 100%
Default:no default value
Errors
TypeError
power is not an integer.
RuntimeError
The motor has been disconnected from the Port.'''
from spike import Motor
from spike.control import wait_for_seconds

motor = Motor('A')

motor.start_at_power(100)

# wait until something
wait_for_seconds(1)
motor.stop()