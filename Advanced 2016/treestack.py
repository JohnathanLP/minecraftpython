from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getPos()

mc.setBlock(x+3,y-1,z,3)
mc.setBlock(x+3,y,z,6)
