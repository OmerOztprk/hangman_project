import tkinter as tk
from tkinter import messagebox
import random
from hangman_words import word_list
from hangman_art import stages, logo
from PIL import Image, ImageTk

def create_window():
    window = tk.Tk()
    window.title("Hangman Game")
    window_width = 500
    window_height = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_pos = int((screen_width / 2) - (window_width / 2))
    y_pos = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
    return window

def create_labels(window, canvas):
    word_label = tk.Label(canvas, text="", font=("Arial", 20), bg="white")
    word_label.pack()
    lives_label = tk.Label(canvas, text="Lives: 6", font=("Arial", 16), bg="white")
    lives_label.pack()
    message_label = tk.Label(canvas, text="Guess a letter", font=("Arial", 14), bg="white")
    message_label.pack()
    hangman_image = tk.Label(canvas, text="", font=("Courier", 18), relief="solid", width=40, height=10, bg="white")
    hangman_image.pack(pady=20)
    return word_label, lives_label, message_label, hangman_image

def create_input_area(window, word_label, lives_label, message_label, hangman_image):
    guess_entry = tk.Entry(window, font=("Arial", 14), width=5)
    guess_entry.pack(pady=20)

    def handle_guess():
        guess = guess_entry.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            message_label.config(text="Please enter a single letter.")
            return
        if guess in guessed_letters:
            message_label.config(text=f"You've already guessed {guess}.")
            return

        guessed_letters.append(guess)
        update_game_state(guess, word_label, lives_label, message_label, hangman_image)

    guess_button = tk.Button(window, text="Guess", font=("Arial", 14), command=handle_guess)
    guess_button.pack()
    return guess_entry, guess_button

def update_game_state(guess, word_label, lives_label, message_label, hangman_image):
    global lives, correct_letters, guessed_letters, chosen_word

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                correct_letters[i] = guess
        word_label.config(text=" ".join(correct_letters))
        message_label.config(text=f"You guessed {guess}, that's in the word.")
    else:
        lives -= 1
        lives_label.config(text=f"Lives: {lives}")
        message_label.config(text=f"You guessed {guess}, that's not in the word. You lose a life.")

    hangman_image.config(text=stages[lives])

    if "_" not in correct_letters:
        message_label.config(text="You win!")
        prompt_restart()
    elif lives == 0:
        message_label.config(text=f"You lose! The word was {chosen_word}")
        prompt_restart()

def prompt_restart():
    answer = messagebox.askquestion("Play again", "Do you want to play again?")
    if answer == "yes":
        restart_game()
    else:
        window.quit()

def restart_game():
    global chosen_word, correct_letters, lives, guessed_letters
    chosen_word = random.choice(word_list)
    correct_letters = ["_" for _ in range(len(chosen_word))]
    lives = 6
    guessed_letters = []
    word_label.config(text=" ".join(correct_letters))
    lives_label.config(text=f"Lives: {lives}")
    message_label.config(text="Guess a letter")
    hangman_image.config(text=stages[6])

def set_background(canvas, image_path):
    image = Image.open(image_path)
    image = image.resize((500, 600))
    background_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    canvas.image = background_image

def play_hangman():
    global word_label, lives_label, message_label, hangman_image, window
    window = create_window()

    canvas = tk.Canvas(window, width=500, height=600)
    canvas.pack()

    set_background(canvas, "background.jpg")

    word_label, lives_label, message_label, hangman_image = create_labels(window, canvas)
    create_input_area(window, word_label, lives_label, message_label, hangman_image)
    restart_game()
    window.mainloop()

play_hangman()
