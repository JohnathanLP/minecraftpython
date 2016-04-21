from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:
    x,y,z = mc.player.getPos()
    t = mc.getBlock(x,y-1,z)

    if t==9:
        mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,79)
    if t==79:
        mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,79)    
