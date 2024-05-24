import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.instructions = tk.Label(self.root, text="I have selected a random number between 1 and 100.")
        self.instructions.pack(pady=10)

        self.prompt = tk.Label(self.root, text="Enter your guess:")
        self.prompt.pack(pady=5)

        self.user_input = tk.Entry(self.root)
        self.user_input.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.feedback = tk.Label(self.root, text="")
        self.feedback.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.user_input.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                self.feedback.config(text="Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.feedback.config(text="Too high! Try again.")
            else:
                self.feedback.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")
                self.user_input.config(state='disabled')
                self.submit_button.config(state='disabled')
                messagebox.showinfo("Game Over",
                                    f"Congratulations! You guessed the number in {self.attempts} attempts.")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
