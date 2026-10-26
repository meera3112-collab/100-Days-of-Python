import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
placeholder_list = list(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
# TODO-2: Change the for loop so that you keep the previous correct letters in display.

game_over = False

while not game_over:
    guess = input("Guess an letter: ")
    for i in range(0,len(chosen_word)):
        if guess == chosen_word[i]:
            placeholder_list[i] = guess
    if "_" not in placeholder_list:
        game_over = True

    print("".join(placeholder_list))

print("You won")

