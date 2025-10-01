import os
import random
from game_data import data
from art import logo, vs


def clear_screen():
    """Clears the CLI screen when called"""
    os.system("cls" if os.name == "nt" else "clear")


def get_random_account():
    """Selects a random account from the data list in game_data.py"""
    return random.choice(data)


def format_account(account):
    """Organises account data into a readable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} - {description} from {country}"


def get_follower_count(account):
    """Retrieves follower count from account data"""
    return account["follower_count"]


def get_answer(account1, account2):
    """Determines which account has the most followers"""
    if get_follower_count(account1) > get_follower_count(account2):
        return account1
    elif get_follower_count(account1) < get_follower_count(account2):
        return account2


def get_choice():
    """Prompts the user to pick 'a' or 'b' and validates the input."""
    while True:
        try:
            choice = (
                input("\nPick which account has more followers - a or b: ")
                .strip()
                .lower()
            )
        except (EOFError, KeyboardInterrupt):
            print("\nExiting round...")
            return None
        if choice in ("a", "b"):
            return choice
        print("Invalid input. Please type 'a' or 'b'.")


def play_game():
    """Runs the game"""
    print("Good luck!")

    account_a = get_random_account()
    account_b = get_random_account()
    current_score = 0
    game_over = False

    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"\na) {format_account(account_a)}")
        print(vs)
        print(f"\nb) {format_account(account_b)}")

        correct_answer = get_answer(account_a, account_b)
        player_choice = get_choice()

        if (player_choice == "a" and correct_answer == account_a) or (
            player_choice == "b" and correct_answer == account_b
        ):
            print("Correct answer.")
            current_score += 1
            print(f"Your current score is: {current_score}")
        elif player_choice is None:
            game_over = True
            print("\nYou've quit the round.")
            break
        else:
            game_over = True
            print("\nIncorrect answer. You lose...")
            print(f"The answer was {correct_answer['name']}")
            print(f"\nYour final score was: {current_score}")


print(logo)
print("Welcome to the Higher Lower Game!")
print(
    "The aim of the game is to get through as many rounds as possible by answering correctly."
)
print(
    "Each round requires you to identify which individual has the higher Instagram follower count."
)
while (
    input(
        "\nDo you want to play the Higher Lower Game? Type 'y' for yes or 'n' for no: "
    ).lower()
    == "y"
):
    clear_screen()
    print(logo)
    play_game()
