import tkinter as tk
from tkinter import messagebox, font

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg='#2c3e50')
        
        # Game variables
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.game_over = False
        
        # Colors
        self.colors = {
            "bg": "#2c3e50",
            "button_bg": "#34495e",
            "button_fg": "#ecf0f1",
            "x_color": "#e74c3c",    # Red
            "o_color": "#3498db",    # Blue
            "win_color": "#27ae60",  # Green
            "title_color": "#ecf0f1"
        }
        
        # Create fonts
        self.title_font = font.Font(family="Arial", size=20, weight="bold")
        self.button_font = font.Font(family="Arial", size=16, weight="bold")
        self.status_font = font.Font(family="Arial", size=12)
        
        self.create_widgets()
        self.update_status()
    
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.colors["bg"], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="TIC TAC TOE", 
            font=self.title_font, 
            fg=self.colors["title_color"], 
            bg=self.colors["bg"]
        )
        title_label.pack(pady=(0, 20))
        
        # Game board frame
        board_frame = tk.Frame(main_frame, bg=self.colors["bg"])
        board_frame.pack(pady=10)
        
        # Create 3x3 grid of buttons
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text=" ",
                    font=self.button_font,
                    width=4,
                    height=2,
                    bg=self.colors["button_bg"],
                    fg=self.colors["button_fg"],
                    relief=tk.RAISED,
                    bd=3,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                row.append(button)
            self.buttons.append(row)
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="",
            font=self.status_font,
            fg=self.colors["title_color"],
            bg=self.colors["bg"],
            pady=10
        )
        self.status_label.pack()
        
        # Reset button
        reset_button = tk.Button(
            main_frame,
            text="New Game",
            font=self.button_font,
            bg="#f39c12",
            fg="white",
            padx=20,
            pady=5,
            command=self.reset_game
        )
        reset_button.pack(pady=20)
    
    def make_move(self, row, col):
        # Check if the move is valid
        if self.board[row][col] == " " and not self.game_over:
            # Update board and button
            self.board[row][col] = self.current_player
            button = self.buttons[row][col]
            button.config(text=self.current_player)
            
            # Set color based on player
            if self.current_player == "X":
                button.config(fg=self.colors["x_color"])
            else:
                button.config(fg=self.colors["o_color"])
            
            # Disable the button
            button.config(state=tk.DISABLED)
            
            # Check for win or draw
            if self.check_win():
                self.highlight_winning_cells()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_status()
    
    def check_win(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        
        return False
    
    def highlight_winning_cells(self):
        # Highlight winning cells in green
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                for col in range(3):
                    self.buttons[row][col].config(bg=self.colors["win_color"])
                return
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                for row in range(3):
                    self.buttons[row][col].config(bg=self.colors["win_color"])
                return
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            for i in range(3):
                self.buttons[i][i].config(bg=self.colors["win_color"])
            return
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            for i in range(3):
                self.buttons[i][2-i].config(bg=self.colors["win_color"])
    
    def check_draw(self):
        # Check if all cells are filled
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return False
        return True
    
    def update_status(self):
        if not self.game_over:
            self.status_label.config(text=f"Player {self.current_player}'s turn")
        else:
            self.status_label.config(text="Game Over")
    
    def reset_game(self):
        # Reset game variables
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.game_over = False
        
        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text=" ",
                    state=tk.NORMAL,
                    bg=self.colors["button_bg"],
                    fg=self.colors["button_fg"]
                )
        
        self.update_status()
    
    def run(self):
        self.root.mainloop()

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    game.run()

if __name__ == "__main__":
    main()