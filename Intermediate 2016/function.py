import time

def scaryMathThing(a):
    "This is the scary math function"
    print "Hold on a second, I will do the math"
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."
    return (((a+4)/5)+19%(8+a))

def anotherScaryMathThing(a,b,c):
    "This is another scary math thing"
    print "Hold on a second, I will do the math"
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."
    time.sleep(1)
    print "."
    return (((((a+6)/5)+(b+4)%7)+c/3 -a*5)-6+c)

x = input("Type in the first number: ")
print "The answer is ", scaryMathThing(x)
y = input("Type in the second number: ")
print "The answer is ", scaryMathThing(y)
z = input("Type in another number: ")
print "The answer is ", scaryMathThing(z)

print "The final answer is ", anotherScaryMathThing(x,y,z)
