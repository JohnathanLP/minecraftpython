f = raw_input ("What do you want to do? ")
while f != "exit" and f != "Exit":
    a = input ("First Number: ")
    b = input ("Second Number: ")

    if f == "add" or f == "Add":
        print "The answer is", (a+b)

    if f == "subtract" or f == "Subtract":
        print "The answer is", (a-b)

    if f == "multiply" or f == "Multiply":
        print "The answer is", (a*b)

    if f == "divide" or f == "Divide":
        print "The answer is", (a/b)

    f = raw_input ("What do you want to do? ")

print "Goodbye!"

