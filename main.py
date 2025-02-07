import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = ["_" for _ in range(len(chosen_word))]

while not game_over:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            correct_letters[i] = guess
    print("".join(correct_letters))

    if "_" not in correct_letters:
        game_over = True
        print("You win!")