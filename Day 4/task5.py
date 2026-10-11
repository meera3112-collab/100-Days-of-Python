'''
TASK 5: ROCK PAPER SCISSORS

You are going to build a Rock, Paper, Scissors game. 
You will need to use what you have learnt about randomisation and Lists to achieve this.
'''
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock,paper,scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: "))
print(choices[player_choice])

computer_choice = random.randint(0,2)
print("Computer Chose: ")
print(choices[computer_choice])

'''
0 - 1 - loose
1 - 2 - loose
2 - 1 - loose
'''

if(player_choice == computer_choice):
    print("Match draw")
elif((player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1)):
    print("you lose")
else:
    print("You win")


