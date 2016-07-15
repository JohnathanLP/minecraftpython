#DiamondFinder - Written by Johnathan Powell for Cache Makers
#Program activate when a button is pressed on pin 14 (using BCM numbering)
#Searches a 3x3 collumn below the player to the bottom of the world for diamond ore, if 
#ore is found, light will illuminate and the number of blocks found will be output in chat.

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
            ytest = y
            #search down to the bottom of the world
            while ytest > -63:
                bi = mc.getBlock(x,ytest,z)
                #if block is a diamond
                if bi == 56:
                    mc.postToChat("Diamonds found!")
                    GPIO.output(ledPin, True)
                    found = (found + 1) 
                ytest = (ytest - 1)
            #if no diamonds are found
            if found == 0:
                mc.postToChat("No diamonds found!")
            #if diamonds are found
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
