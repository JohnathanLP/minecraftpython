from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    t = 0
    while t < 10:
        x,y,z = mc.player.getPos()
        mc.setBlock(x,y-1,z,35,t)
        t += 1
