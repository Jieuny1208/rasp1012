import RPi.GPIO as GPIO
import I2C_driver2 as rasp1012
import I2C_driver2 as LCD
import time
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

mylcd = rasp1012.lcd()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def main():
    LED = 10
    Switch1 = 11
    Switch2 = 13
    Switch3 = 15
    Flag1 = 0
    Flag2 = 0
    Flag3 = 0
    #mylcd = rasp1012.lcd()
    GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED, GPIO.OUT)

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)

    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        #mylcd.lcd_clear()
        if (GPIO.input(Switch1) == GPIO.HIGH and Flag1 == 0):
            mylcd.lcd_clear()
            print("Touch On")
            Flag = 1
            GPIO.output(LED, GPIO.LOW)
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'T', fill="white", font=proportional(CP437_FONT))

        elif (GPIO.input(Switch2) == GPIO.HIGH and Flag2 == 0):
            mylcd.lcd_clear()
            print("Flame On")
            for i in range(10):
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(LED, GPIO.LOW)
                time.sleep(0.1)
            Flag = 1
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'F', fill="white", font=proportional(CP437_FONT))

        elif (GPIO.input(Switch3) == GPIO.HIGH and Flag3 == 0):
            print("Light On")
            GPIO.output(LED, GPIO.LOW)
            Flag = 0
            with canvas(virtual) as draw:
                text(draw, (0, 1), 'L', fill="white", font=proportional(CP437_FONT))
            mylcd.lcd_display_string("Room Light ON",1)
            mylcd.lcd_display_string("!!!!!!!!!!!!",2)
            sleep(1)

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
