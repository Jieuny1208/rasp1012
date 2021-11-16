import RPi.GPIO as GPIO
import I2C_driver2 as rasp1012
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
    LED1 = 16
    LED2 = 10
    Switch = 32
    Flag = 0
    GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)
    
    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    while True:
        if (GPIO.input(Switch) == GPIO.HIGH and Flag == 0):
            print("Push")
            Flag = 1
            GPIO.output(LED1, GPIO.HIGH)
            sleep(1)
            GPIO.output(LED2, GPIO.HIGH)
            with canvas(virtual) as draw:
                text(draw, (0, 1), '<-', fill="white", font=proportional(CP437_FONT))
            mylcd.lcd_display_string("Right",1)
            mylcd.lcd_display_string("Right!!!!",2)
            sleep(1)

        elif (GPIO.input(Switch) == GPIO.HIGH and Flag == 1):
            print("LED OFF")
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW)
            Flag = 0
            with canvas(virtual) as draw:
                text(draw, (0, 1), '', fill="white", font=proportional(CP437_FONT))
            mylcd.lcd_display_clear()
            mylcd.lcd_display_string("LED_OFF",2)
            sleep(1)

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
