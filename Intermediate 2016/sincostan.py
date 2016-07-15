import math
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


while True:
    x,y,z = mc.player.getPos()
    s = 0
    t = 0
    u = 0
    a = 0
    while t < 40:
        mc.setBlock(x+t,y+(u*4),z+(s*4),35,a)
        mc.setBlock(x+t,y-(u*4),z-(s*4),35,a+5)
        t += .1
        a += 1
        u = math.sin(t/3)
        s = math.cos(t/3)
    t = 0
    while t < 40:
        mc.setBlock(x+t,y+(u*4),z+(s*4),0)
        mc.setBlock(x+t,y-(u*4),z-(s*4),0)
        t += .1
        a += 1
        u = math.sin(t/3)
        s = math.cos(t/3)
