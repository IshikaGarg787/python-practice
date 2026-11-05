import random

# List of words to choose from
words = ["PYTHON", "JAVA", "KOTLIN", "JAVASCRIPT"]

# Function to display the current state of the game
def display_game(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to play the game
def play_hangman():
    word = random.choice(words)
    guessed_letters = []
    tries = 6

    while tries > 0:
        print(display_game(word, guessed_letters))
        guess = input("Guess a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            guessed_letters.append(guess)
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")
    
    if tries == 0:
        print(f"Sorry, you ran out of tries. The word was {word}.")

if __name__ == "_main_":
    play_hangman()