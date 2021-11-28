from spike import MotorPair
# Initialize the motor pair
motor_pair = MotorPair('B', 'A')
# Initialize default speed
motor_pair.set_default_speed(100)
# Move in one direction for 2 seconds
motor_pair.move(2, 'seconds')

# Move in the other direction for 2 seconds
motor_pair.set_default_speed(-100)
motor_pair.move(2, 'seconds')


# Turn in one direction for 2 seconds
motor_pair.move_tank(10, 'cm', left_speed=100, right_speed=100)

# Move in the other direction for 2 seconds
motor_pair.move_tank(1, 'rotations', left_speed=-100, right_speed=-100)
