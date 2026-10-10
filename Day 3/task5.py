'''
TASK 5:

Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill. Use the input() function to get a user's preferences 
and then add up the total for their order and tell them how much they have to pay.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Interaction
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28.
'''

print("Welcome to Python Pizza Deliveries!")
bill_amount = 0
pizza_size = input("What size pizza do you want? S, M or L: ")
if pizza_size == 'S':
    bill_amount = 15
elif pizza_size == 'M':
    bill_amount = 20
else:
    bill_amount = 25

wants_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if wants_pepperoni == 'Y':
    if pizza_size == "S":
        bill_amount += 2
    else:
        bill_amount += 3

wants_cheese = input("Do you want extra cheese? Y or N: ")
if wants_cheese == 'Y':
    bill_amount += 1

print(f"Your final bill is: ${bill_amount}.")


        
