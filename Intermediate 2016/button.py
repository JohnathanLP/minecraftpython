import RPi.GPIO as GPIO
import time

buttonPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
lastState = 0

try:
    while True:
        if GPIO.input(buttonPin) and lastState == 0:
            print"Button is Not Pressed!"
            lastState = 1
        elif not GPIO.input(buttonPin) and lastState == 1:
            print"Button is Pressed!"
            lastState = 0
        else:
            time.sleep(.1)

except KeyboardInterrupt:
    print "Cleaning Up!"
    GPIO.cleanup()
