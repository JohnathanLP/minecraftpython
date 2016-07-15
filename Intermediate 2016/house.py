from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO
import time

buttonPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setwarnings(False)

try:
    while True:
        if not GPIO.input(buttonPin):
            x,y,z = mc.player.getPos()

            mc.setBlocks(x+5,y-1,z+5, x-5,y+3,z-5, 5)
            mc.setBlocks(x+4,y  ,z+4, x-4,y+2,z-4, 0)
            mc.setBlocks(x+5,y  ,z  , x+5,y+1,z  , 0)
            mc.setBlock(x,y,z, 50)
            time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()
