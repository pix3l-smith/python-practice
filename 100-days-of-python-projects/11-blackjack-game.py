import random
import os


def clear_screen():
    """Clears the CLI screen when called"""
    os.system("cls" if os.name == "nt" else "clear")


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards."""

    if sum(cards) == 21:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        if sum(cards) == 21:
            return 0

    return sum(cards)


def compare(score1, score2):
    """Compares the user's score with the dealer's score"""
    if score1 == 0 and score2 == 0:
        return "\nIt's a draw"
    elif score2 == 0:
        return "\nYou lose... Your opponent has Blackjack"
    elif score1 == 0:
        return "\nYOU WIN!"
    elif score1 > 21:
        return "\nYour score is too high. You lose..."
    elif score2 > 21:
        return "\nYour opponent's score is too high. YOU WIN!"
    elif score1 == score2:
        return "\nIt's a draw"
    elif score1 > score2:
        return "\nYour score is the highest. YOU WIN!"
    else:
        return "You lose..."


def play_game():
    """Runs the game"""
    # Empty lists to represent the user's hand of cards and the dealer's hand of cards
    user_cards = []
    user_score = -1
    dealer_cards = []
    dealer_score = -1
    game_over = False

    # Deals 2 cards to user and dealer
    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"\nYour cards are: {user_cards}")
        if user_score == 0:
            print("BLACKJACK!")
        else:
            print(f"Your current score is {user_score}")
        print(f"The dealer's first card is: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input(
                "Would you like another card? 'y' for yes or 'n' to end the game: "
            ).lower()
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score > 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print("\nThe game is over")
    print(f"The dealer's hand was: {dealer_cards}")
    if dealer_score == 0:
        print("The dealer has Blackjack!")
    else:
        print(f"The dealer's score was: {dealer_score}")
    print(compare(user_score, dealer_score))


while (
    input(
        "Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: "
    ).lower()
    == "y"
):
    clear_screen()
    play_game()
