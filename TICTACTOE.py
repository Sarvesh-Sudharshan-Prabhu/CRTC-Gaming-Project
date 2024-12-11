import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = 'X'

        self.buttons = [[None] * 3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text=' ', font=('Helvetica', 20), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.turn_label = tk.Label(self.window, text="Player 1's Turn", font=('Helvetica', 12))
        self.turn_label.grid(row=3, columnspan=3)

    def on_click(self, row, col):
        if self.buttons[row][col]['text'] == ' ' and not self.is_board_full():
            self.buttons[row][col]['text'] = self.current_player
            if self.is_winner():
                self.end_game(f"{self.current_player} wins!")
            elif self.is_board_full():
                self.end_game("It's a tie!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.turn_label.config(text=f"{self.current_player}'s Turn")
                if self.current_player == 'O':
                    self.computer_move()

    def is_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != ' ':
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != ' ':
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != ' ':
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != ' ':
            return True
        return False

    def is_board_full(self):
        return all(self.buttons[i][j]['text'] != ' ' for i in range(3) for j in range(3))

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.buttons[row][col]['text'] = 'O'
            self.current_player = 'X'
            self.turn_label.config(text="Player 1's Turn")
            if self.is_winner():
                self.end_game("Computer wins!")
            elif self.is_board_full():
                self.end_game("It's a tie!")

    def end_game(self, message):
        messagebox.showinfo('Game Over', message)
        self.window.destroy()

    def main(self):
        messagebox.showinfo('Welcome', 'Welcome to Tic Tac Toe!')
        self.window.mainloop()

# Play the game
if __name__ == "__main__":
    game = TicTacToe()
    game.main()
