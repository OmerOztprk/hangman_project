import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
lives = 6
correct_letters = ["_" for _ in range(len(chosen_word))]

while not game_over:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            correct_letters[i] = guess

    if guess not in chosen_word:
        lives -= 1

    print("".join(correct_letters))
    print(stages[lives])

    if "_" not in correct_letters:
        game_over = True
        print("You win!")
    elif lives == 0:
        game_over = True
        print("You lose!")