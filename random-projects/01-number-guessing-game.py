import random

print("Welcome to the Number Guessing Game!\nYou have 7 chances to guess the correct number between 1 and 100.")

num = random.randint(1, 100)
chances = 7
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"\nCORRECT! The number is {num}. It took you {guess_counter} guesses.")
        break

    elif guess_counter >= chances and guess != num:
        print(f"\nOH, NO! The number was {num}. Better luck next time.")

    elif guess > num:
        print(f"\nTOO HIGH! Try a lower number.\n{7 - guess_counter} guesses remaining...\n")

    elif guess < num:
        print(f"\nTOO LOW! Try a higher number.\n{7 - guess_counter} guesses remaining...\n")
