from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

tlast = 0;

while True:
    x,y,z = mc.player.getPos()
    t = mc.getBlock(x,y-1,z)
    if t != tlast:
        if t==0:
            mc.postToChat("You're flying!")
        elif t==1:
            mc.postToChat("Stone")
        elif t==2:
            mc.postToChat("Grass")
        elif t==3:
            mc.postToChat("Dirt")
        elif t==12:
            mc.postToChat("Sand")
        else:
            mc.postToChat("I'm not sure...")
    tlast = t
    time.sleep(.1)
