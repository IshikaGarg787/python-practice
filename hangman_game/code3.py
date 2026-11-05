import random

class Hangman:
    def _init_(self, words):
        self.words = words
        self.word = random.choice(self.words).upper()
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.guessed_words = []  # Initialize guessed_words
        self.guessed = False     # Initialize guessed
        self.tries = 6

    def display_hangman(self):
        stages = [
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        return stages[self.tries]

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print(f"You already guessed the letter {letter}.")
        elif letter not in self.word:
            print(f"The letter {letter} is not in the word.")
            self.tries -= 1
            self.guessed_letters.append(letter)
        else:
            print(f"Good guess! The letter {letter} is in the word.")
            self.guessed_letters.append(letter)
            word_as_list = list(self.word_completion)
            indices = [i for i, l in enumerate(self.word) if l == letter]
            for index in indices:
                word_as_list[index] = letter
            self.word_completion = "".join(word_as_list)
            if "_" not in self.word_completion:
                self.guessed = True

    def guess_word(self, word):
        if word in self.guessed_words:
            print(f"You already guessed the word {word}.")
        elif word != self.word:
            print(f"The word {word} is not correct.")
            self.tries -= 1
            self.guessed_words.append(word)
        else:
            self.guessed = True
            self.word_completion = self.word

    def play(self):
        print("Let's play Hangman!")
        while not self.guessed and self.tries > 0:
            print(self.display_hangman())
            print(self.word_completion)
            guess = input("Please guess a letter or word: ").upper()
            if len(guess) == 1 and guess.isalpha():
                self.guess_letter(guess)
            elif len(guess) == len(self.word) and guess.isalpha():
                self.guess_word(guess)
            else:
                print("Invalid guess.")
            print("\n")
        if self.guessed:
            print("Congratulations! You guessed the word!")
        else:
            print(f"Sorry, you ran out of tries. The word was {self.word}. Better luck next time!")

if __name__ == "_main_":
    words = ["PYTHON", "JAVA", "KOTLIN", "JAVASCRIPT"]
    game = Hangman(words)
    game.play()