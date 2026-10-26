'''
TASK 4: Final Hangman game
'''

import random 
from hangman_words import word_list
from hangman_art import logo, stages

choosen_word = random.choice(word_list)
print(logo)

lives = 6
placeholder = ""
for i in range(len(choosen_word)):
    placeholder+="_"

print(f"Word to guess: {placeholder}")
placeholder_list = list(placeholder)

game_over = False

guessed_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed ",guess)

    else:
        guessed_letters.append(guess)

        if guess not in choosen_word:
            print(f"You guessed {guess}, that's not in the word you loose a life")
            lives-=1
            print(stages[lives])
            print(f"********************************** {lives}/6 left **********************************")
            

        else:
            for i in range(len(choosen_word)):
                if guess == choosen_word[i]:
                    placeholder_list[i]= guess

    print("".join(placeholder_list))
    if "_" not in placeholder_list :
        print("You won!!!")
        game_over = True    
    if lives == 0:
        game_over = True
        print("You lost")
        print(f"The word was {choosen_word}")

