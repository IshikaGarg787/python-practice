import random

class Hangman:
    def __init__(self, word_list, max_attempts=6):
        self.word = random.choice(word_list).lower()
        self.max_attempts = max_attempts
        self.attempts_left = max_attempts
        self.guessed_letters = set()
        self.current_state = ["_"] * len(self.word)
        self.hangman_stages = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            ----------
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            ----------
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            ----------
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            ----------
            """,
            """
               -----
               |   |
               O   |
              /|\  |
                   |
                   |
            ----------
            """,
            """
               -----
               |   |
               O   |
              /|\  |
              /    |
                   |
            ----------
            """,
            """
               -----
               |   |
               O   |
              /|\  |
              / \  |
                   |
            ----------
            """
        ]

    def display_state(self):
        print(self.hangman_stages[self.max_attempts - self.attempts_left])
        print("Word: " + " ".join(self.current_state))
        print(f"Attempts left: {self.attempts_left}")
        print(f"Guessed letters: {', '.join(self.guessed_letters)}")

    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("You already guessed that letter!")
            return

        self.guessed_letters.add(letter)
        if letter in self.word:
            print("Good guess!")
            for i, char in enumerate(self.word):
                if char == letter:
                    self.current_state[i] = letter
        else:
            print("Wrong guess!")
            self.attempts_left -= 1

    def is_game_over(self):
        if "_" not in self.current_state:
            print("Congratulations! You've guessed the word!")
            return True
        if self.attempts_left <= 0:
            print(f"Game over! The word was '{self.word}'.")
            return True
        return False

# Initialize the game
word_list = ["python", "hangman", "programming", "challenge", "developer"]
game = Hangman(word_list)

# Game loop
while not game.is_game_over():
    game.display_state()
    guess = input("Guess a letter: ").strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    game.guess(guess)

