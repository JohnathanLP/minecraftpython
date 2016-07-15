from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()
while True:
    mc.setBlock(x,y-1,z, 1)
    x+=1
    y+=1
    z+=1
