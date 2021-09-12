'''
Example program for checking ESP LEGO SPIKE simulator
Source: LEGO Education SPIKE 2.0.0 
Controlling the Light Matrix
Create your first program using Python.

Copy the code shown below by clicking or tapping the copy icon  in the box.
Paste the code to the Programming Canvas, where you’ll write your code.

The green lines are simply comments. They won’t influence your program's actions. The other lines are your program. Can you figure out what this first program will do?

Play the program.'''

'''# Import the PrimeHub class
from spike import PrimeHub
from spike.control import wait_for_seconds
# Initialize the Hub
your_hub = PrimeHub()
# Light up a smiley face
your_hub.light_matrix.show_image('HAPPY')
wait_for_seconds(5)
your_hub.light_matrix.off()
'''
'''Change the image that’s displayed on the Light Matrix.
Change the parameter "HAPPY" to "HEART" in the code you already have. This will light up the heart instead of the happy face on the Hub.
Or, copy the code from the box below and paste it after the last line of your program. This will light up the happy face for 5 seconds and then light up a heart for 5 seconds.'''
'''
# Add another image
your_hub.light_matrix.show_image('HEART')
wait_for_seconds(5)
your_hub.light_matrix.off()
'''

'''
Playing Short Beeps and Time
Let’s make the Hub play some beeps.

If there's already a program on your Programming Canvas, it’s a good idea to delete it or start a new project before continuing.
Copy the code shown below to the Programming Canvas.
Make sure that you only have one line of code that starts with: from spike import.
Play the program!'''
# Import the PrimeHub class
from spike import PrimeHub
from spike.control import wait_for_seconds
# Initialize the Hub
hub = PrimeHub()
# beep beep beep!
hub.speaker.beep(60, 1)

'''Change the beat and tone. This is one way of doing it.'''
# Here’s a new song
hub.speaker.beep(44, 0.5)
hub.speaker.beep(123, 1.0)
wait_for_seconds(0.5)
hub.speaker.beep(20, 0.5)
hub.speaker.beep(40, 0.5)
hub.speaker.beep(67, 1.0)
wait_for_seconds(0.5)
hub.speaker.beep(40, 0.5)
'''Playing Sounds
You can also add sounds to be played from your device.

Copy the code shown below to the Programming Canvas. Play the program!'''

# Import the PrimeHub class
from spike import App
# Initialize the app
app = App()
app.play_sound('Cat Meow 1')

'''Pick another sound to play, or use this program.'''
app.play_sound('Triumph')

