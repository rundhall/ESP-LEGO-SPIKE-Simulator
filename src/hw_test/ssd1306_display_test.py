from machine import Pin, I2C
import time, math
import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)


display.fill(1)                         # fill entire screen with colour=0
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
display.show()

