from spike import ColorSensor, Motor
from spike.control import Timer
# Initialize the Colour Sensor, 2 motors, and a Timer
color_sensor = ColorSensor('F')
motor_a = Motor('A')
motor_e = Motor('E')
timer = Timer()
# Present each colored brick to the Color Sensor and observe what happens; it will detect each color for 30 seconds
while timer.now() < 5:
	color = color_sensor.wait_for_new_color()
	if color == None:
		motor_a.run_for_rotations(1)
	elif color == 'white':
		motor_e.run_for_rotations(1)
	print ("color:",color)

print("wait_for_new_color is over") 
