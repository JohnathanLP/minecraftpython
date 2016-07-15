import random

#pick a random number
target = random.randint(0,100)
print "I've picked a random number from 0 to 100! I want you to guess it!"
guess = input("Guess a number! ")
while guess != target:
    print "\n"
    if guess < target:
        print "Try a bigger number!"
    if guess > target:
        print "Try a smaller number!"
    guess = input("Guess again!")
print "You did it!"
