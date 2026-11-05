import random
import tkinter as tk
from tkinter import messagebox

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        master.title("Hangman Game")
        
        # Game words with hints
        self.words_with_hints = {
            "PYTHON": "A popular programming language",
            "JAVA": "Object-oriented language used for Android apps",
            "KOTLIN": "Modern language that runs on JVM",
            "JAVASCRIPT": "The language of the web",
            "CSHARP": "Microsoft's object-oriented language",
            "SQL": "Language for database management"
        }
        
        # Initialize game
        self.word = random.choice(list(self.words_with_hints.keys()))
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed = False
        self.tries = 6
        
        # Create GUI elements
        self.create_widgets()
        self.update_display()
    
    def create_widgets(self):
        # Hangman drawing canvas
        self.canvas = tk.Canvas(self.master, width=300, height=300, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        # Word display
        self.word_label = tk.Label(self.master, text="", font=('Arial', 24))
        self.word_label.grid(row=1, column=0, columnspan=3, pady=10)
        
        # Hint display
        self.hint_label = tk.Label(self.master, text="", font=('Arial', 12), wraplength=400)
        self.hint_label.grid(row=2, column=0, columnspan=3, pady=5)
        
        # Attempts left
        self.attempts_label = tk.Label(self.master, text="", font=('Arial', 12))
        self.attempts_label.grid(row=3, column=0, columnspan=3, pady=5)
        
        # Guessed letters
        self.guessed_label = tk.Label(self.master, text="", font=('Arial', 12))
        self.guessed_label.grid(row=4, column=0, columnspan=3, pady=5)
        
        # Input frame
        input_frame = tk.Frame(self.master)
        input_frame.grid(row=5, column=0, columnspan=3, pady=10)
        
        self.guess_entry = tk.Entry(input_frame, font=('Arial', 14), width=15)
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        
        self.guess_button = tk.Button(input_frame, text="Guess", command=self.process_guess)
        self.guess_button.pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to guess button
        self.master.bind('<Return>', lambda event: self.process_guess())
    
    def draw_hangman(self):
        self.canvas.delete("all")
        
        # Draw gallows
        self.canvas.create_line(50, 250, 150, 250, width=3)  # Base
        self.canvas.create_line(100, 250, 100, 50, width=3)  # Pole
        self.canvas.create_line(100, 50, 200, 50, width=3)    # Top
        self.canvas.create_line(200, 50, 200, 80, width=3)    # Rope
        
        if self.tries < 6:  # Head
            self.canvas.create_oval(180, 80, 220, 120, width=3)
        
        if self.tries < 5:  # Body
            self.canvas.create_line(200, 120, 200, 180, width=3)
        
        if self.tries < 4:  # Left arm
            self.canvas.create_line(200, 130, 170, 150, width=3)
        
        if self.tries < 3:  # Right arm
            self.canvas.create_line(200, 130, 230, 150, width=3)
        
        if self.tries < 2:  # Left leg
            self.canvas.create_line(200, 180, 170, 220, width=3)
        
        if self.tries < 1:  # Right leg
            self.canvas.create_line(200, 180, 230, 220, width=3)
    
    def update_display(self):
        # Update word display with spaces between letters
        displayed_word = " ".join(list(self.word_completion))
        self.word_label.config(text=displayed_word)
        
        # Update hint
        self.hint_label.config(text=f"Hint: {self.words_with_hints[self.word]}")
        
        # Update attempts
        self.attempts_label.config(text=f"Attempts left: {self.tries}")
        
        # Update guessed letters
        guessed_text = "Guessed letters: " + ", ".join(sorted(self.guessed_letters)) if self.guessed_letters else ""
        self.guessed_label.config(text=guessed_text)
        
        # Update hangman drawing
        self.draw_hangman()
    
    def process_guess(self):
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)
        
        if not guess:
            return
        
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                messagebox.showinfo("Already Guessed", f"You already guessed the letter {guess}")
            elif guess not in self.word:
                messagebox.showinfo("Incorrect", f"The letter {guess} is not in the word.")
                self.tries -= 1
                self.guessed_letters.append(guess)
            else:
                messagebox.showinfo("Correct", f"Good guess! The letter {guess} is in the word.")
                self.guessed_letters.append(guess)
                word_as_list = list(self.word_completion)
                indices = [i for i, letter in enumerate(self.word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                self.word_completion = "".join(word_as_list)
                if "_" not in self.word_completion:
                    self.guessed = True
        elif len(guess) == len(self.word) and guess.isalpha():
            if guess in self.guessed_words:
                messagebox.showinfo("Already Guessed", f"You already guessed the word {guess}")
            elif guess != self.word:
                messagebox.showinfo("Incorrect", f"The word {guess} is not correct.")
                self.tries -= 1
                self.guessed_words.append(guess)
            else:
                self.guessed = True
                self.word_completion = self.word
        else:
            messagebox.showinfo("Invalid Input", "Please enter a single letter or a word of the correct length.")
        
        self.update_display()
        self.check_game_over()
    
    def check_game_over(self):
        if self.guessed:
            messagebox.showinfo("Congratulations!", "You guessed the word!")
            self.master.after(1000, self.reset_game)
        elif self.tries <= 0:
            messagebox.showinfo("Game Over", f"Sorry, you ran out of tries. The word was {self.word}.")
            self.master.after(1000, self.reset_game)
    
    def reset_game(self):
        self.word = random.choice(list(self.words_with_hints.keys()))
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.guessed_words = []
        self.guessed = False
        self.tries = 6
        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGUI(root)
    root.mainloop()