'''
TASK 3:

Figure out how to pick a random name from the list of friends.
'''

# option 1

import random
friends = ["Meera", "Sarvesh", "Suba", "Akshi", "Ana"]
print(random.choice(friends))

# option 2 

number_of_friends = len(friends)
random_number = random.randint(0,number_of_friends)
print(friends[random_number])