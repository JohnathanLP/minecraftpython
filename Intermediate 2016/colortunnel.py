import math
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()
while True:
    a = 0
    while a < 10:
        s = 0
        t = 0
        u = 0
        while t < 150:
            t += .1
            mc.setBlocks(x+4,y-t-1,z+4, x-4,y-t-1,z-4,0)
            mc.setBlock(x+(u*4),y-t,z+(s*4),35,a)
            mc.setBlock(x-(u*4),y-t,z-(s*4),35,a)
            u = math.sin(t/2)
            s = math.cos(t/2)
       
        a += 1
