from spike import ForceSensor, Motor
# Initialize the Force Sensor and a motor
force_sensor = ForceSensor('B')
motor = Motor('A')
# Press the button slowly, it will only work once # Play the program again to give it another go
motor.set_default_speed(100)
force_sensor.wait_until_pressed()
motor.start()
force_sensor.wait_until_released()
motor.stop()

motor.set_default_speed(100)
force_sensor.wait_until_pressed()
force_sensor.wait_until_released()
motor.start()
force_sensor.wait_until_pressed()
force_sensor.wait_until_released()
motor.stop()
