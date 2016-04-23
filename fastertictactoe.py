import RPi.GPIO as GPIO 			#import GPIO libraries
import time					#import time library, useful for sleep
from mcpi.minecraft import Minecraft		#import Minecraft API	
mc = Minecraft.create()

GPIO.setmode(GPIO.BCM)				#sets GPIO to use Broadcom-defined numbering

#pin declarations/setup here!

def checkSquare(x,y,z,b):
	"This checks a single block at the given coords x,y,z for blocktype b"
	t=mc.getBlock(x,y,z)

	if t==b:
                mc.setBlock(x,y,z,0)
                return True
        else:
                return False

def makeX(x,y,z):
	mc.setBlock(x,   y-1, z,   35, 0)   
	mc.setBlock(x-1, y-1, z-1, 35, 0)
	mc.setBlock(x-1, y-1, z+1, 35, 0)
	mc.setBlock(x+1, y-1, z+1, 35, 0)
	mc.setBlock(x+1, y-1, z-1, 35, 0)

def make0(x,y,z):
	mc.setBlocks(x-1, y-1, z-1, x+1, y-1, z-1, 35, 0)
	mc.setBlocks(x-1, y-1, z+1, x+1, y-1, z+1, 35, 0)	
	mc.setBlock(x-1, y-1, z, 35, 0)
	mc.setBlock(x+1, y-1, z, 35, 0)
	mc.setBlock(x,   y-1,  z,35, 7)

print("Now running script... Press CTRL+C to exit")
try:
	#Main code here!
	cX,cY,cZ = mc.player.getPos()
	mc.setBlocks(cX+10, cY-1, cZ+10, cX-10, cY-1,  cZ-10, 35, 7)
	mc.setBlocks(cX+10, cY,    cZ+10, cX-10, cY+10, cZ-10, 0)
	mc.setBlocks(cX+3,  cY-1,  cZ+8,  cX+3,  cY-1,  cZ-8,  35, 0)
	mc.setBlocks(cX-3,  cY-1,  cZ+8,  cX-3,  cY-1,  cZ-8,  35, 0)
	mc.setBlocks(cX+8,  cY-1,  cZ+3,  cX-8,  cY-1,  cZ+3,  35, 0)
	mc.setBlocks(cX+8,  cY-1,  cZ-3,  cX-8,  cY-1,  cZ-3,  35, 0)
	mc.setBlock(cX-6, cY-1, cZ-6, 35, 1)
	mc.setBlock(cX-6, cY-1, cZ,   35, 1)
	mc.setBlock(cX-6, cY-1, cZ+6, 35, 1)
	mc.setBlock(cX  , cY-1, cZ-6, 35, 1)
	mc.setBlock(cX  , cY-1, cZ,   35, 1)
	mc.setBlock(cX  , cY-1, cZ+6, 35, 1)
	mc.setBlock(cX+6, cY-1, cZ-6, 35, 1)
	mc.setBlock(cX+6, cY-1, cZ,   35, 1)
	mc.setBlock(cX+6, cY-1, cZ+6, 35, 1)	
	
	mc.postToChat("Welcome to Tic-Tac-Toe!")
	mc.postToChat("Player One, use stone, Player Two, use dirt")
	mc.postToChat("Place blocks on the colored dots to make X's and O's")

        taken = [0,0,0, 0,0,0, 0,0,0,] 

	#Check blocks for stone or dirt        
	while True:
                if taken[0]==0:
                        if checkSquare(cX-6,cY,cZ-6,3):
                                makeX(cX-6,cY,cZ-6)
                                taken[0]=1
                        elif checkSquare(cX-6,cY,cZ-6, 1):
                                make0(cX-6,cY,cZ-6)
                                taken[0]=2
                if taken[1]==0:
                        if checkSquare(cX-6,cY,cZ,3):
                                makeX(cX-6,cY,cZ)
                                taken[1]=1
                        elif checkSquare(cX-6,cY,cZ, 1):
                                make0(cX-6,cY,cZ)
                                taken[1]=2
                if taken[2]==0:
                        if checkSquare(cX-6,cY,cZ+6,3):
                                makeX(cX-6,cY,cZ+6)
                                taken[2]=1
                        elif checkSquare(cX-6,cY,cZ+6, 1):
                                make0(cX-6,cY,cZ+6)
                                taken[2]=2
                                
                if taken[3]==0:
                        if checkSquare(cX,cY,cZ-6,3):
                                makeX(cX,cY,cZ-6)
                                taken[3]=1
                        elif checkSquare(cX,cY,cZ-6, 1):
                                make0(cX,cY,cZ-6)
                                taken[3]=2
                if taken[4]==0:
                        if checkSquare(cX,cY,cZ,3):
                                makeX(cX,cY,cZ)
                                taken[4]=1
                        elif checkSquare(cX,cY,cZ, 1):
                                make0(cX,cY,cZ)
                                taken[4]=2
                if taken[5]==0:
                        if checkSquare(cX,cY,cZ+6,3):
                                makeX(cX,cY,cZ+6)
                                taken[5]=1
                        elif checkSquare(cX,cY,cZ+6, 1):
                                make0(cX,cY,cZ+6)
                                taken[5]=2

                if taken[6]==0:
                        if checkSquare(cX+6,cY,cZ-6,3):
                                makeX(cX+6,cY,cZ-6)
                                taken[6]=1
                        elif checkSquare(cX+6,cY,cZ-6, 1):
                                make0(cX+6,cY,cZ-6)
                                taken[6]=2
                if taken[7]==0:
                        if checkSquare(cX+6,cY,cZ,3):
                                makeX(cX+6,cY,cZ)
                                taken[7]=1
                        elif checkSquare(cX+6,cY,cZ, 1):
                                make0(cX+6,cY,cZ)
                                taken[7]=2
                if taken[8]==0:
                        if checkSquare(cX+6,cY,cZ+6,3):
                                makeX(cX+6,cY,cZ+6)
                                taken[8]=1
                        elif checkSquare(cX+6,cY,cZ+6, 1):
                                make0(cX+6,cY,cZ+6)
                                taken[8]=2
	
except KeyboardInterrupt:
	GPIO.cleanup()
