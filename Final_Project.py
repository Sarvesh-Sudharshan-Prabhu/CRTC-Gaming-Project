import os
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
import subprocess  # Added import for subprocess

def run_game(game_path):
    os.system(game_path)

def open_link(link):
    webbrowser.open(link)

def resize_image(image_path, width, height):
    img = Image.open(image_path)
    img = img.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def create_button(frame, text, bg, fg, column, row, action, link=None, icon_path=None, column_span=1):
    def perform_action():
        print(f"Action: {action}, Link: {link}")
        if action == "game":
            try:
                subprocess.Popen(["python", link], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            except Exception as e:
                print(f"Error running the game: {e}")
        elif action == "web":
            open_link(link)

    button = tk.Button(
        frame,
        text=text,
        bg=bg,
        fg=fg,
        font=("Arial", 12),
        padx=15,
        pady=10,
        relief=tk.GROOVE,
        command=perform_action
    )

    if action != "web" and icon_path is not None:
        icon_size = (40, 40)
        icon = resize_image(icon_path, *icon_size)
        button.config(image=icon, compound=tk.LEFT)
        button.icon = icon

    button.grid(column=column, row=row, padx=10, pady=10, sticky='nsew', columnspan=column_span)

window = tk.Tk()
window.title("MiniGames")
window.geometry('550x175')
window.configure(bg="Navy Blue")

# Create the first frame for game buttons
game_frame = tk.Frame(window, bg="Navy Blue")
game_frame.grid(row=0, column=0, sticky="nsew")

games_info = [
    {"name": "Snake", "action": "game", "link": r'C:\SNAKE.py', "icon_path": r'C:\Snake.png'},
    {"name": "Hangman", "action": "game", "link": r'C:\Hangman.py', "icon_path": r'C:\Hangman.png'},
    {"name": "TicTacToe", "action": "game", "link": r'C:\TICTACTOE.py', "icon_path": r'C:\TicTacToe.png'},
]

max_button_width = max(len(game["name"]) for game in games_info)

for i, game in enumerate(games_info):
    create_button(
        game_frame,
        game["name"],
        "#4285F4",
        "white",
        i * 2,
        0,
        game["action"],
        game["link"],
        game.get("icon_path"),
        column_span=2
    )
    game_frame.grid_columnconfigure(i * 2, minsize=max_button_width)

# Create the second frame for non-game buttons
non_game_frame = tk.Frame(window, bg="Navy Blue")
non_game_frame.grid(row=1, column=0, sticky="nsew")

# Add non-game buttons to the second frame
create_button(
    non_game_frame,
    "Project Info",
    "#FF0000",
    "white",
    0,
    0,
    "web",
    "https://docs.google.com/presentation/d/e/2PACX-1vQ9McX5a04EsSsuh9y0XqgbFrn8dyrswtrXCmqQAr0W1qMOZJCkNzWQdwQ8A5isfJfnhsxq3_xG62ST/pub?start=true&loop=true&delayms=30000",
    column_span=2
)

# Set the row and column weights for both frames
for i in range(len(games_info) * 2):
    game_frame.grid_rowconfigure(i, weight=1)
    game_frame.grid_columnconfigure(i, weight=1)

for i in range(2):
    non_game_frame.grid_rowconfigure(i, weight=1)
    non_game_frame.grid_columnconfigure(i, weight=1)

window.mainloop()
