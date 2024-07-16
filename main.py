import tkinter as tk
import random

class Minesweeper:
    def __init__(self, master, rows=10, cols=10, mines=10):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.flags = 0
        self.buttons = []
        self.board = []

        # Añadir una etiqueta para mostrar el número de bombas restantes
        self.mine_counter_label = tk.Label(self.master, text=f"Bombas restantes: {self.mines - self.flags}")
        self.mine_counter_label.grid(row=0, column=0, columnspan=self.cols)

        # Crear el tablero de juego
        self.create_widgets()
        self.create_board()
        self.place_mines()
        self.update_counts()

    def create_widgets(self):
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                button = tk.Button(self.master, width=2, height=1, command=lambda r=r, c=c: self.on_click(r, c))
                button.bind('<Button-3>', lambda e, r=r, c=c: self.on_right_click(r, c))
                button.grid(row=r+1, column=c)  # Ajustar el índice de la fila
                row.append(button)
            self.buttons.append(row)

    def create_board(self):
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def place_mines(self):
        placed_mines = 0
        while placed_mines < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] != -1:
                self.board[r][c] = -1
                placed_mines += 1

    def update_counts(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                mine_count = 0
                for i in range(max(0, r-1), min(self.rows, r+2)):
                    for j in range(max(0, c-1), min(self.cols, c+2)):
                        if self.board[i][j] == -1:
                            mine_count += 1
                self.board[r][c] = mine_count

    def on_click(self, r, c):
        if self.buttons[r][c]['state'] == 'disabled' or self.buttons[r][c]['text'] == 'F':
            return
        if self.board[r][c] == -1:
            self.buttons[r][c].config(text='*', bg='red')
            self.game_over(False)
        else:
            self.reveal(r, c)
            if self.check_win():
                self.game_over(True)

    def on_right_click(self, r, c):
        if self.buttons[r][c]['state'] == 'disabled':
            return
        if self.buttons[r][c]['text'] == 'F':
            self.buttons[r][c].config(text='', bg='SystemButtonFace')
            self.flags -= 1
        else:
            if self.flags < self.mines:
                self.buttons[r][c].config(text='F', bg='yellow')
                self.flags += 1
            else:
                return
        self.update_mine_counter()

    def update_mine_counter(self):
        self.mine_counter_label.config(text=f"Bombas restantes: {self.mines - self.flags}")

    def reveal(self, r, c):
        if self.buttons[r][c]['state'] == 'disabled':
            return
        self.buttons[r][c].config(text=self.board[r][c], state='disabled', relief=tk.SUNKEN)
        if self.board[r][c] == 0:
            for i in range(max(0, r-1), min(self.rows, r+2)):
                for j in range(max(0, c-1), min(self.cols, c+2)):
                    if self.board[i][j] != -1 and self.buttons[i][j]['state'] != 'disabled':
                        self.reveal(i, j)

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != -1 and self.buttons[r][c]['state'] != 'disabled':
                    return False
        return True

    def game_over(self, won):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    self.buttons[r][c].config(text='*', bg='red')
                self.buttons[r][c].config(state='disabled')
        if won:
            print("¡Has ganado!")
        else:
            print("¡Juego terminado!")

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()