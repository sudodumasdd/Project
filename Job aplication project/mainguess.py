import random

# This program implements a simple guessing game where the user tries to guess a random number between 1 and 100.
# The program generates a random number, then prompts the user for guesses.
# It provides feedback on whether the guess is too high or too low.
# The user has 8 guesses to get the number right.
# If the user runs out of guesses, the program reveals the correct number.

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