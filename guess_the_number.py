import random

print("Welcome to the Number Guessing Game!")
number_to_guess = random.randint(1, 10)
guess = None
attempts = 0

while guess != number_to_guess:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} tries.")
    except ValueError:
         print("Please enter a valid number.")
