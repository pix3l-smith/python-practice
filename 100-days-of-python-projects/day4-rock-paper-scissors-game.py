import random

# Incorporate multi-round system to enable 'best of x rounds wins' game option

# multi_round = input("Would you like to play multiple rounds to determine an overall winner? Type yes or no: ").lower()

# if multi_round == "yes":
#     round_number = int(input("How many rounds would you like to play? "))

# elif multi_round == "no":
#     print("One round it is!")

# else:
#     print("Invalid input")

user_choice = input("Pick rock, paper or scissors. Type in your choice: ").lower()
computer_choice = random.randint(1, 3)

# Converting random number to equivalent word so that computer is 'choosing' a word instead
if computer_choice == 1:
    computer_choice = "rock"

elif computer_choice == 2:
    computer_choice = "paper"

else:
    computer_choice = "scissors"

# Gameplay
if computer_choice == user_choice:
    print(f"The computer chose {computer_choice}...\nIt's a draw!")

elif computer_choice == "rock" and user_choice == "paper":
    print(f"The computer chose {computer_choice}...\nYou win!")

elif computer_choice == "rock" and user_choice == "scissors":
    print(f"The computer chose {computer_choice}...\nYou lose!")

elif computer_choice == "paper" and user_choice == "rock":
    print(f"The computer chose {computer_choice}...\nYou lose!")

elif computer_choice == "paper" and user_choice == "scissors":
    print(f"The computer chose {computer_choice}...\nYou win!")

elif computer_choice == "scissors" and user_choice == "rock":
    print(f"The computer chose {computer_choice}...\nYou win!")

elif computer_choice == "scissors" and user_choice == "paper":
    print(f"The computer chose {computer_choice}...\nYou lose!")

else:
    print("Invalid input. You lose!")
