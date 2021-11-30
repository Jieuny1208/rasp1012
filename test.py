import RPi.GPIO as GPIO
import I2C_driver2 as rasp1012
import I2C_driver2 as LCD
import time
import random
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
    LED = 12
    Switch1 = 11
    Switch2 = 13
    Switch3 = 15
    Switch4 = 40
    Flag1 = 0
    Flag2 = 0
    Flag3 = 0
    Flag4 = 0
    #mylcd = rasp1012.lcd()
    GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Switch4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    PWM_LED = GPIO.PWM(LED, 500)
    PWM_LED.start(0)

    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, width=8, height=8, block_orientation=0)
    print(device)
    device.contrast(100)
    virtual = viewport(device, width=8, height=8)

    #show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

    x = 0
    result = 0
    while True:
        #print("Touch", x)
        #mylcd.lcd_clear()
        if (GPIO.input(Switch1) == GPIO.HIGH and Flag1 == 0):
            mylcd.lcd_clear()
            x = random.randrange(1,4)
            for i in range(1,x):
                result = result + i
                print("Touch Switch",x)
            Flag = 1
            #GPIO.output(LED, GPIO.LOW)
            if result < 10:
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(result), fill="white", font=proportional(CP437_FONT))

            else :
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(0), fill="white", font=proportional(CP437_FONT))
                    mylcd.lcd_display_string("Touch Sensor",1)
                while 1:
                    for duty in range(100):
                        PWM_LED.ChangeDutyCycle(duty)
                        time.sleep(0.1)

        elif (GPIO.input(Switch2) == GPIO.HIGH and Flag2 == 0):
            mylcd.lcd_clear()
            x = random.randrange(1,4)
            for i in range(1,x):
                result = result + i
                print("Flame Switch",x)
            #for i in range(10):
                #GPIO.output(LED, GPIO.HIGH)
                #time.sleep(0.1)
                #GPIO.output(LED, GPIO.LOW)
                #time.sleep(0.1)
            Flag = 1
            if result < 10:
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(result), fill="white", font=proportional(CP437_FONT))

            else :
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(0), fill="white", font=proportional(CP437_FONT))
                    mylcd.lcd_display_string("Flame Switch ON",1)
                    while 1:
                        for duty in range(100):
                            PWM_LED.ChangeDutyCycle(duty)
                            time.sleep(0.1)

        elif (GPIO.input(Switch4) == GPIO.HIGH and Flag4 == 0):
            mylcd.lcd_clear()
            x = random.range(1,4)
            for i in range(1,x):
                result = result + i
                print("Button Switch",x)
            Flag = 1
            #GPIO.output(LED1, GPIO.HIGH)
            #sleep(1)
            #GPIO.output(LED2, GPIO.HIGH)
            if result < 10:
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(result), fill="white", font=proportional(CP437_FONT))

            else :
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(0), fill="white", font=proportional(CP437_FONT))
                    mylcd.lcd_display_string("button Switch",1)
                    while 1:
                        for duty in range(30):
                            PWM_LED.ChangeDutyCycle(duty)
                            time.sleep(0.01)

        elif (GPIO.input(Switch3) == GPIO.HIGH and Flag3 == 0):
            x = random.randrange(1,4)
            for i in range(1,x):
                result = result + i
                print("Light Switch",x)
            GPIO.output(LED, GPIO.LOW)
            Flag = 1
            if result < 10:
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(result), fill="white", font=proportional(CP437_FONT))

            else :
                with canvas(virtual) as draw:
                    text(draw, (0, 1), str(0), fill="white", font=proportional(CP437_FONT))
                    mylcd.lcd_display_string("light Switch",1)
                    while 1:
                        for duty in range(100):
                            PWM_LED.ChangeDutyCycle(duty)
                            time.sleep(0.1)

        elif 10 <= x :
            while 1:
                for duty in range(100):
                    PWM_LED.ChangeDutyCycle(duty)
                    time.sleep(0.1)
        sleep(1)

'''
        for _ in range(1):
            for intensity in range(16):
                device.contrast(intensity*16)
                sleep(0.1)
'''

if __name__ == '__main__':
    main()
