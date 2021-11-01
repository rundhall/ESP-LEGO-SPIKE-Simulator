from machine import Pin, I2C
import time, math
import spike.ssd1306
import spike.gfx

# using default address 0x3C
i2c = I2C(sda=Pin(21), scl=Pin(22))
oled_width = 128
oled_height = 64
display = spike.ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
graphics = spike.gfx.GFX(oled_width, oled_height, display.pixel)
display.fill(0)                         # fill entire screen with colour=0
display.show()
display.text('SZIASZTOK!', 20, 20, 1)    # draw some text at x=0, y=0, colour=1
display.show()
'''for v in range (69,129,1):
    display.fill_rect(52, 3, v, 14, 1)
    display.show()
    print(v,"/")
    time.sleep_ms(500)'''

'''
display.fill(0)                         # fill entire screen with colour=0
display.show()
display.rect(0, 0, 14, 14, 1)
display.show()
input('press a button')
display.rect(16, 0, 14, 14, 1)
display.show()
input('press a button')
display.rect(32, 0, 14, 14, 1)
display.show()
input('press a button')
display.rect(48, 0, 14, 14, 1)
display.show()
input('press a button')
display.rect(64, 0, 14, 14, 1)
display.show()
input('press a button')

display.rect(0, 16, 14, 14, 1)
display.show()
input('press a button')
display.rect(16, 16, 14, 14, 1)
display.show()
input('press a button')
display.rect(32, 16, 14, 14, 1)
display.show()
input('press a button')
display.rect(48, 16, 14, 14, 1)
display.show()
input('press a button')
display.rect(64, 16, 14, 14, 1)
display.show()
input('press a button')
'''

#display.fill_rect((0+x*13), 3, (13+x*13), 14, 1)
HAPPY = [[1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [1, 1, 1, 0, 1]]
for x in range (5):
    for y in range (5):
        if HAPPY[y][x]==1:
            graphics.fill_rect(x*24, y*13, 22, 11, 1)   # draw a solid rectangle 10,10 to 107,43, colour=1
            print (str(x),str(y), "/",str(x*24),"/",str(y*13))
            display.show()
        time.sleep_ms(200)
    

    
'''display.fill(1)                         # fill entire screen with colour=0
display.text('SZIASZTOK!', 20, 20, 0)    # draw some text at x=0, y=0, colour=1
display.show()
time.sleep_ms(500)
display.fill(0)                         # fill entire screen with colour=0
display.pixel(10, 10, 1)                 # set pixel at x=0, y=10 to colour=1
time.sleep_ms(500)
display.show()
display.hline(10, 10, 107, 1)               # draw horizontal line x=0, y=8, width=4, colour=1
time.sleep_ms(500)
display.show()
display.vline(10, 10, 43, 1)               # draw vertical line x=0, y=8, height=4, colour=1
time.sleep_ms(500)
display.show()
display.line(10, 10, 113, 49, 1)          # draw a line from 0,0 to 127,63
time.sleep_ms(500)
display.show()
display.line( 10, 49,113, 10, 1)          # draw a line from 0,0 to 127,63
time.sleep_ms(500)
display.show()
display.rect(10, 10, 107, 43, 1)        # draw a rectangle outline 10,10 to 107,43, colour=1
time.sleep_ms(500)
display.show()
display.fill_rect(10, 10, 107, 43, 1)   # draw a solid rectangle 10,10 to 107,43, colour=1
time.sleep_ms(500)
display.show()
display.text('SZIA BLANKA', 20, 0, 1)    # draw some text at x=0, y=0, colour=1
display.text('SZIA ZSOFI', 20, 20, 0)    # draw some text at x=0, y=0, colour=1
display.text('SZIA ANYA', 20, 40, 0)    # draw some text at x=0, y=0, colour=1
time.sleep_ms(500)

'''


