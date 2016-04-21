import time
import RPi.GPIO as GPIO

ledPin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

while True:
    print "Blink!"
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(3)
    print "Off!"
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(3)

GPIO.cleanup()
