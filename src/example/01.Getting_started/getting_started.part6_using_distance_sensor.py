from spike import DistanceSensor, Motor
# Initialize the Distance Sensor and motor
distance_sensor = DistanceSensor('D')
motor = Motor('C')
# Move your hand slowly toward and then away from the Distance Sensor
count = 0
while count < 5:
	distance_sensor.wait_for_distance_farther_than(20, 'cm')
	motor.start()
	distance_sensor.wait_for_distance_closer_than(20, 'cm')
	motor.stop()
	count = count + 1
	print('counta', str(count))
