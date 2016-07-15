#Elsa - Written by Johnathan Powell for Cache Makers
#While this program is running, water below player's feet and in a 10 block radius will convert 
#to ice. Let it go.

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

#loop forever
while True:
    x,y,z = mc.player.getPos()
    t = mc.getBlock(x,y-1,z)
    
    #checks for ice or water, creates ice
    if t==9:
        mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,79)
    if t==79:
        mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,79)    
