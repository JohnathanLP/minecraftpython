from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

try:
    while True:
        x,y,z = mc.player.getPos()
        t = mc.getBlock(x,y-1,z)
        if t == 2:
            GPIO.output(21, GPIO.HIGH)
        else:
            GPIO.output(21, GPIO.LOW)
        time.sleep(.1)
except KeyboardInterrupt:
    GPIO.cleanup()
