import random
from hangman_words import word_list
from hangman_art import stages, logo

def play_hangman():
    print(logo)

    chosen_word = random.choice(word_list)
    correct_letters = ["_" for _ in range(len(chosen_word))]
    print(" ".join(correct_letters))
    lives = 6
    guessed_letters = []

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"You guessed {guess}, that's in the word.")
            for i in range(len(chosen_word)):
                if guess == chosen_word[i]:
                    correct_letters[i] = guess
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

        print(" ".join(correct_letters))
        print(stages[lives])

        if "_" not in correct_letters:
            print("You win!")
            break

        if lives == 0:
            print(f"You lose! The word was {chosen_word}")
            break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        play_hangman()
    else:
        print("Thanks for playing!")

play_hangman()