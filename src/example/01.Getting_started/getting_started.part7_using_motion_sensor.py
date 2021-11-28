from spike import PrimeHub, App
# Initialize the Hub and app
hub = PrimeHub()
app = App()

count = 0
while count < 10:
	orientation = hub.motion_sensor.wait_for_new_orientation()
	if orientation == 'front':
		hub.light_matrix.show_image('ASLEEP')
		app.start_sound('Snoring')
	elif orientation == 'up':
		hub.light_matrix.show_image('HAPPY')
		app.start_sound('Triumph')
	count = count + 1
	print('count_a', str(count))

