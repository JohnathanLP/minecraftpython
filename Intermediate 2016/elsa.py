from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getPos()
    t = mc.getBlock(x,y-1,z)
    if t == 79 or t == 9:
        mc.setBlocks(x+1,y-1,z+1, x-1,y-1,z-1, 79)
