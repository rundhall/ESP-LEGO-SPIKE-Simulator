from spike import ForceSensor, Motor
# Initialize the Force Sensor, a motor, and a variable
force_sensor = ForceSensor('B')
motor = Motor('C')
count = 0
# You can press the Force Sensor 5 times 
motor.set_default_speed(100)
while count < 5:
	force_sensor.wait_until_pressed()
	motor.start()
	force_sensor.wait_until_released()
	motor.stop()
	count = count + 1

