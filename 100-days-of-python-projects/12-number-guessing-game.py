import random
import os

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5


def clear_screen():
    """Clears the CLI screen when called"""
    os.system("cls" if os.name == "nt" else "clear")


def difficulty():
    """Prompts the user to select a difficulty"""
    while True:
        difficulty = input("\nChoose a difficulty - easy or hard: ").lower()

        if difficulty == "easy":
            return EASY_DIFFICULTY
        elif difficulty == "hard":
            return HARD_DIFFICULTY
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")


def get_guess():
    """Prompts the user to enter a guess"""
    while True:
        try:
            return int(input("\nGuess a number: "))
        except ValueError:
            print("Invalid input. Please guess a number: ")


def play_game():
    """Runs the game"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guess_num = random.randint(1, 100)
    game_over = False
    guesses = difficulty()

    while not game_over:
        if guesses > 0:
            print(f"You have {guesses} guesses left.")
            current_guess = get_guess()
            guesses -= 1
            if current_guess > guess_num:
                print("Too high")
            elif current_guess < guess_num:
                print("Too low")
            else:
                game_over = True
                print("YOU WIN!")
        else:
            game_over = True
            print("\nYou've run out of guesses. You lose...")
            print(f"The number was {guess_num}")


while (
    input(
        "Do you want to play a game of Guess the Number? Type 'y' for yes or 'n' for no: "
    ).lower()
    == "y"
):
    clear_screen()
    play_game()
