import RPi.GPIO as GPIO
import time

ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try:
    while True:
        print "on"
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(.01)
        
        print "off"
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(.01)

except KeyboardInterrupt:
    print "Cleaning up!"
    GPIO.cleanup()
