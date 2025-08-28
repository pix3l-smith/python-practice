import random
from hangman_words import word_list
from hangman_art import heading, stages


# Select word
chosen_word = random.choice(word_list)

# Give intro
print(heading)
print("WELCOME!")
print(f"The mystery word has {len(chosen_word)} letters.")

# Create placeholders
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_ "
print(f"{placeholder}\n")

# Game variables
game_over = False
lives = 6
correct_letters = []
guessed_letters = []

# Run game
while not game_over:
    # Receive guess
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print(f"\nYou've already guessed the letter '{guess}'\n")
        print(f"{display}\n")
        continue

    guessed_letters.append(guess)


    # Check letters in selected word
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += f"{letter} "
            correct_letters.append(letter)
        
        elif letter in correct_letters:
            display += f"{letter} "
        
        else:
            display += "_ "


    # Return response for incorrect guess
    if guess not in chosen_word and lives >= 1:
        print(stages[-lives])
        print("\nIncorrect\n")
        lives -= 1
        print(f"You have {lives} guess(es) remaining.\n")
    

    # Return response based on game state
    if "_" not in display:
        game_over = True
        print("\nYOU WIN!")
        print(f"The word was '{chosen_word}'.\n")
    
    elif lives == 0:
        game_over = True
        print("\nGAME OVER!")
        print(f"The word was '{chosen_word}'.\n")
    
    else:
        print(f"\n{display}\n")
