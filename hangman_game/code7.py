import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Hangman Game with First Letter")

        # Word Categories and Choices
        self.word_pool = {
            "Animals": ["TIGER", "ELEPHANT", "GIRAFFE", "RABBIT", "PANDA"],
            "Countries": ["INDIA", "BRAZIL", "CANADA", "FRANCE", "JAPAN"],
            "Fruits": ["BANANA", "APPLE", "ORANGE", "MANGO", "PINEAPPLE"]
        }
        self.category = random.choice(list(self.word_pool.keys()))
        self.word = random.choice(self.word_pool[self.category]).upper()

        # Setup game variables
        self.guessed_word = [self.word[0]] + ["_"] * (len(self.word) - 1)  # Reveal first letter
        self.remaining_attempts = 6
        self.guessed_letters = set(self.word[0])  # Include first letter in guessed letters

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        # Heading: Category
        self.category_label = tk.Label(self.root, text=f"Category: {self.category}", font=("Arial", 18))
        self.category_label.pack(pady=10)

        # Display Word
        self.word_label = tk.Label(self.root, text=" ".join(self.guessed_word), font=("Arial", 24))
        self.word_label.pack(pady=20)

        # Input Field
        self.guess_entry = tk.Entry(self.root, font=("Arial", 16), width=5, justify='center')
        self.guess_entry.pack(pady=10)

        # Guess Button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, font=("Arial", 14), bg="#3498db", fg="white")
        self.guess_button.pack(pady=5)

        # Remaining Attempts Label
        self.attempts_label = tk.Label(self.root, text=f"Remaining Attempts: {self.remaining_attempts}", font=("Arial", 14))
        self.attempts_label.pack(pady=10)

        # Guessed Letters Display
        self.guessed_letters_label = tk.Label(self.root, text=f"Guessed Letters: {self.word[0]}", font=("Arial", 12))
        self.guessed_letters_label.pack(pady=10)

    def make_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter!")
            return
        if guess in self.guessed_letters:
            messagebox.showwarning("Duplicate Guess", "You already guessed that letter!")
            return

        # Process guess
        self.guessed_letters.add(guess)
        self.guessed_letters_label.config(text=f"Guessed Letters: {', '.join(self.guessed_letters)}")

        if guess in self.word:
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[idx] = guess
            self.word_label.config(text=" ".join(self.guessed_word))
        else:
            self.remaining_attempts -= 1
            self.attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")

        # Check game state
        if "_" not in self.guessed_word:
            messagebox.showinfo("Game Over", "Congratulations! You guessed the word!")
            self.reset_game()
        elif self.remaining_attempts == 0:
            messagebox.showerror("Game Over", f"You lost! The word was: {self.word}")
            self.reset_game()

    def reset_game(self):
        self.category = random.choice(list(self.word_pool.keys()))
        self.word = random.choice(self.word_pool[self.category]).upper()
        self.guessed_word = [self.word[0]] + ["_"] * (len(self.word) - 1)  # Reveal first letter
        self.remaining_attempts = 6
        self.guessed_letters = set(self.word[0])  # Include first letter in guessed letters

        # Update UI
        self.category_label.config(text=f"Category: {self.category}")
        self.word_label.config(text=" ".join(self.guessed_word))
        self.attempts_label.config(text=f"Remaining Attempts: {self.remaining_attempts}")
        self.guessed_letters_label.config(text=f"Guessed Letters: {self.word[0]}")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()