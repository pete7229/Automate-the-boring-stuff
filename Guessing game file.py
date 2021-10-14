#random number generator game

import random
print ('Hello, what is your name?')
name = str(input())

secretNumber = random.randint (1,10)
print ('Well, ' + name + ' Im thinking of a number between 1 and 10, try and guess what it is!')


for guessestaken in range (1,4):
    print ('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print ('Too low')
    elif guess > secretNumber:
        print ('Too high')
    else:
        break # this condition is for the correct guess!

if guess == secretNumber:
    print ('Ding Ding Ding, we have a winner')
    print ('You took ' + str(guessestaken) + ' guesses to get the number')

else:
    print ('You lost, I was thinking of the number ' + str(secretNumber))
    
