from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time

x,y,z=mc.player.getPos()
c =0


while True:
    u = mc.getBlock(x,y-1,z)
    if u==57:
        mc.postToChat ("You found a diamond")

#mc.setBlocks(x,y+2,z,x+10,y+10,z+10,46,1)

#mc.setBlocks(x-100,y+20,z-100,x+100,y-70,z+100,0)

#mc.setBlocks(x-100,y-1,z-100,x+100,y-1,z+100,57)
#mc.postToChat("Diamonds, diamonds, everywhere...")
