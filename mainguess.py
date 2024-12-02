import random

x = random.randrange(1, 100)
#prints the question
print("Guess a number between 1 and 100:")
#Asks for input
n = int(input())

guesses = 0
#Counts your guesses
while guesses < 8:
    if n == x:
        print("You got it!")
        break
    elif n > x:
        print("Too high")
    elif n < x:
        print("Too low")
    guesses += 1
    print("Try again")
    n = int(input())

#after 8 guesses prints the number and ends the game
if guesses == 8:
    print("You ran out of guesses. The number was", x)

#Notes
#1. At first i had the variable type wrong so i could not do the operations
#2. At first i was trying to use loops for the grading of the guesses