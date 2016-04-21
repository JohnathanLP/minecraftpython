from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import RPi.GPIO as GPIO

buttonPin = 14
ledPin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, False)

try:
    #loop until keyboard interrupt
    while True:
        #if button is pressed
        if GPIO.input(buttonPin):
            mc.postToChat("Now finding diamonds...")
            found = 0
            x,y,z = mc.player.getPos()
            test = y
            while test > -63:
                bi = mc.getBlock(x,test,z)
                if bi == 56:
                    mc.postToChat("Diamonds found!")
                    GPIO.output(ledPin, True)
                    found = (found + 1)
                test = (test - 1)

            if found == 0:
                mc.postToChat("No diamonds found!")
            else:
                string = "Number of diamonds found: "
                string += `found`
                mc.postToChat(string)
                mc.postToChat("Wait for LED to turn off before running again.")
                time.sleep(5)
                GPIO.output(ledPin, False)
            time.sleep(.1)
        else:
            time.sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
