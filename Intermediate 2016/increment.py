import os
import time

fout = open("timerecord.txt",'w')
fout.truncate()
try:
    limit = input("How long do you want to count? ")
    seconds = 0.00
    #take it to the limit
    while seconds <= limit:
        os.system('clear')
        print seconds
        seconds += .01
        time.sleep(.01)
        #one more time
    print "All done!"
    fout.write("Total time passed: ")
    s = str(seconds)
    fout.write(s)
    fout.close()
except KeyboardInterrupt:
    fout.write("Total time passed: ")
    s = str(seconds)
    fout.write(s)
    fout.close()
    
    
