import RPi.GPIO as GPIO
import time

buttonPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)

try:
        while True:
            if GPIO.input(buttonPin):
                print "Button is pressed!"
                time.sleep(.1)
            else:
                time.sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
