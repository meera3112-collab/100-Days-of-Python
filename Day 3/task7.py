'''
TASK 7: TREASURE ISLAND PROJECT

Your goal today is to build a "Chose your own adventure game". 
Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.

Use the flow chart create the game logic.

Once you've completed the project, you can always extend the game and make it more interesting!
'''

print("Welcome to Treasure Island!!!")
choice1 = input("Do you wanna take right or left? R or L: ")
if choice1 == 'L':
    print("You fell into a pit, GAME OVER!!!")
else: 
    choice2 = int(input("You have 3 doors infront of you choose the door number wisely, 1,2 or 3: "))
    if choice2 == 2:
        print("You stepped into fire, GAME OVER!!!")
    elif choice2 == 3:
        print("You stepped onto a bomb, GAME OVER!!!")
    else:
        choice3 = int(input("Now you have 2 boxes infront of you,open one 1 or 2: "))
        if choice3 == 2:
            print("You opened a box full of snakes, GAME OVER!!!")
        else:
            print("You found the treasure, YOU WON!!!")

