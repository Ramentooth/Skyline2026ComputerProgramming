import random


print ("Guess a number between 1 and 100:")
numGuessed = int(input())
attempts = 1
correctNum = random.randint(1, 100)
while numGuessed != correctNum:
    attempts += 1
    if numGuessed < correctNum:
        print (str(numGuessed)+"? a little higher my guy... go again")
        numGuessed = int(input())
    elif numGuessed > correctNum:
        print (str(numGuessed)+"? a little lower my guy... go again")
        numGuessed = int(input())
if numGuessed == correctNum:
    print ("Nice, it was " + str(numGuessed) + "! You got it in "+ str(attempts) + " attempts! \n"
    "Try to get it in even less attempts the next time ;)")


