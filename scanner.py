#Scanner - Written by Johnathan Powell for Cache Makers
#While running, outputs to chat the block under the player's feet

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

tlast = 0;

#loop always
while True:
    x,y,z = mc.player.getPos()
    t = mc.getBlock(x,y-1,z)
    #checks if block has changed - prevents excessive posts
    if t != tlast:
        #air
        if t==0:
            mc.postToChat("You're flying!")
        #stone
        elif t==1:
            mc.postToChat("Stone")
        #grass
        elif t==2:
            mc.postToChat("Grass")
        #dirt
        elif t==3:
            mc.postToChat("Dirt")
        #sand
        elif t==12:
            mc.postToChat("Sand")
        #everything else
        else:
            mc.postToChat("I'm not sure...")
    tlast = t
    time.sleep(.1)
