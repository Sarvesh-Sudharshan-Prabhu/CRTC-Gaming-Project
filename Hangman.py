import random
import tkinter as tk
from tkinter import messagebox, simpledialog

words = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli fruit', 'vanilla', 'watermelon', 'xylocarp', 'yuzu', 'zucchini', 'almond', 'blueberry', 'cantaloupe', 'date', 'elderflower', 'feijoa', 'guava', 'huckleberry', 'jackfruit', 'kiwifruit', 'lychee', 'mulberry', 'nectar', 'olive', 'passion fruit', 'quandong', 'rhubarb', 'soursop', 'tamarind', 'umami', 'vitality', 'whortleberry', 'xigua', 'yam', 'zinfandel grape', 'apricot', 'blackberry', 'cucumber', 'dewberry', 'endive', 'fennel', 'grapefruit', 'hibiscus', 'icaco', 'jambul', 'kumquat', 'leek', 'mangosteen', 'navajo', 'oregano', 'pomelo', 'quinoa', 'rutabaga', 'saffron', 'tangelo', 'uva', 'verjuice', 'wampee', 'ximenia', 'yellow passion fruit', 'zander', 'acai berry', 'boysenberry', 'carrot', 'dill', 'eggplant', 'feijoa', 'grapefruit', 'hazelnut', 'imbe', 'jujube', 'kohlrabi', 'longan', 'manzano', 'nance', 'olallieberry', 'pawpaw', 'quince', 'rambutan', 'soursop', 'thimbleberry', 'umeboshi', 'velvet apple', 'wasabi', 'xocoatl', 'yam', 'zinfandel grape']


def choose_word(words):
    word = random.choice(words)
    return word

def play_game(word):
    blanks = ['_'] * len(word)
    word_list = list(word)
    guesses_left = 6

    while '_' in blanks and guesses_left > 0:
        guess = simpledialog.askstring('Guess', ' '.join(blanks) + '\nGuess a letter:')
        if guess in word_list:
            for i in range(len(word)):
                if word_list[i] == guess:
                    blanks[i] = guess
        else:
            guesses_left -= 1
            messagebox.showinfo('Incorrect', 'Incorrect! You have ' + str(guesses_left) + ' guesses left.')

    if '_' not in blanks:
        messagebox.showinfo('Congratulations', 'Congratulations, you guessed the word!')
    else:
        messagebox.showinfo('Game Over', 'Sorry, you ran out of guesses. The word was ' + word)

def main():
    messagebox.showinfo('Welcome', 'Welcome to Hangman!')
    word = choose_word(words)
    play_game(word)

window = tk.Tk()
window.withdraw()  # Hide the main window
main()
window.mainloop()
