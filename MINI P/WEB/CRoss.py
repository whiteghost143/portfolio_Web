import tkinter as tk
import random

class CrosswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Crossword Puzzle")

        self.grid_size = 10
        self.entries = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.words = ["PYTHON", "JAVA", "KOTLIN", "SCRIPT", "ALGORITHM"]

        self.create_widgets()
        self.place_words_randomly()

    def create_widgets(self):
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(padx=10, pady=10)

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                entry = tk.Entry(self.grid_frame, width=2, font=('Arial', 16), justify='center')
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry

    def place_words_randomly(self):
        for word in self.words:
            placed = False
            while not placed:
                direction = random.choice(['H', 'V'])
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - 1)

                if direction == 'H':
                    if col + len(word) <= self.grid_size and self.can_place_word_horizontal(word, row, col):
                        self.place_word_horizontal(word, row, col)
                        placed = True
                elif direction == 'V':
                    if row + len(word) <= self.grid_size and self.can_place_word_vertical(word, row, col):
                        self.place_word_vertical(word, row, col)
                        placed = True

    def can_place_word_horizontal(self, word, row, col):
        for i, letter in enumerate(word):
            if self.entries[row][col + i].get() not in ("", letter):
                return False
        return True

    def can_place_word_vertical(self, word, row, col):
        for i, letter in enumerate(word):
            if self.entries[row + i][col].get() not in ("", letter):
                return False
        return True

    def place_word_horizontal(self, word, row, col):
        for i, letter in enumerate(word):
            self.entries[row][col + i].delete(0, tk.END)
            self.entries[row][col + i].insert(0, letter)

    def place_word_vertical(self, word, row, col):
        for i, letter in enumerate(word):
            self.entries[row + i][col].delete(0, tk.END)
            self.entries[row + i][col].insert(0, letter)

if __name__ == "__main__":
    root = tk.Tk()
    app = CrosswordApp(root)
    root.mainloop()
