from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

def helixMaker(x,y,z,t,state):
    "Makes given state of helix around player"
    if state == 0:
        mc.setBlock(x  ,y+5,z  ,35,t)
        mc.setBlock(x  ,y-3,z  ,35,t)
    elif state == 1:
        mc.setBlock(x+1,y+5,z  ,35,t)
        mc.setBlock(x-1,y-3,z  ,35,t)
    elif state == 2:
        mc.setBlock(x+2,y+5,z  ,35,t)
        mc.setBlock(x-2,y-3,z  ,35,t)
    elif state == 3:
        mc.setBlock(x+3,y+4,z  ,35,t)
        mc.setBlock(x-3,y-2,z  ,35,t)
    elif state == 4:
        mc.setBlock(x+4,y+3,z  ,35,t)
        mc.setBlock(x-4,y-1,z  ,35,t)
    elif state == 5:
        mc.setBlock(x+4,y+2,z  ,35,t)
        mc.setBlock(x-4,y  ,z  ,35,t)
    elif state == 6:
        mc.setBlock(x+4,y+1,z  ,35,t)
        mc.setBlock(x-4,y+1,z  ,35,t)
    elif state == 7:
        mc.setBlock(x+4,y  ,z  ,35,t)
        mc.setBlock(x-4,y+2,z  ,35,t)
    elif state == 8:
        mc.setBlock(x+4,y-1,z  ,35,t)
        mc.setBlock(x-4,y+3,z  ,35,t)
    elif state == 9:
        mc.setBlock(x+3,y-2,z  ,35,t)
        mc.setBlock(x-3,y+4,z  ,35,t)
    elif state == 10:
        mc.setBlock(x+2,y-3,z  ,35,t)
        mc.setBlock(x-2,y+5,z  ,35,t)
    elif state == 11:
        mc.setBlock(x+1,y-3,z  ,35,t)
        mc.setBlock(x-1,y+5,z  ,35,t)
    


while True:
    state = 0
    t = 0
    while state < 12:
        x,y,z = mc.player.getPos()
        helixMaker(x,y,z,t,state)
        #time.sleep(.001)
        t += 1
        state += 1
    
