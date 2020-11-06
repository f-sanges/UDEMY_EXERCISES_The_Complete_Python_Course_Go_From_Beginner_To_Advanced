''' Simple project to guess a number '''
import random

number_to_guess = random.randint(1, 10)
print("DEBUG: Number to guess: " + str(number_to_guess))
guess = 0

while guess != number_to_guess:
    guess = int(input("Guess the number: \n"))
    if guess < number_to_guess:
        print("The number to guess is higher:\n")
    elif guess > number_to_guess:
        print("The number to guess is lower:\n")
print("You guessed the number")

