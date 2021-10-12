import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
LED = 11
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(LED, GPIO.HIGH)
time.sleep(10)
GPIO.output(LED, GPIO.LOW)
time.sleep(5)

