import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Python GUI")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        self.player = "X"
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Player X's Turn", font=('Helvetica', 16))
        self.label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame, text="", font=('Helvetica', 24), width=5, height=2,
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        self.reset_btn = tk.Button(self.root, text="Restart Game", font=('Helvetica', 12), command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def on_click(self, row, col):
        btn = self.buttons[row][col]
        if btn["text"] == "":
            btn["text"] = self.player
            btn.config(state="disabled")

            if self.check_winner(self.player):
                self.label.config(text=f"Player {self.player} Wins!")
                self.highlight_winner()
                self.disable_all_buttons()
            elif self.is_draw():
                self.label.config(text="It's a Draw!")
                messagebox.showinfo("Draw", "Game ended in a draw.")
            else:
                self.player = "O" if self.player == "X" else "X"
                self.label.config(text=f"Player {self.player}'s Turn")

    def check_winner(self, player):
        for i in range(3):
            if all(self.buttons[i][j]["text"] == player for j in range(3)) or \
               all(self.buttons[j][i]["text"] == player for j in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == player for i in range(3)) or \
           all(self.buttons[i][2-i]["text"] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

    def highlight_winner(self):
        player = self.player
        for i in range(3):
            if all(self.buttons[i][j]["text"] == player for j in range(3)):
                for j in range(3):
                    self.buttons[i][j].config(bg="lightgreen")
                return
            if all(self.buttons[j][i]["text"] == player for j in range(3)):
                for j in range(3):
                    self.buttons[j][i].config(bg="lightgreen")
                return
        if all(self.buttons[i][i]["text"] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][i].config(bg="lightgreen")
            return
        if all(self.buttons[i][2-i]["text"] == player for i in range(3)):
            for i in range(3):
                self.buttons[i][2-i].config(bg="lightgreen")
            return

    def reset_game(self):
        self.player = "X"
        self.label.config(text="Player X's Turn")
        for i in range(3):
            for j in range(3):
                btn = self.buttons[i][j]
                btn.config(text="", state="normal", bg="SystemButtonFace")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
