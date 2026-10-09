'''
FINAL PROJECT : TIP CALCULATOR

We're going to build a tip calculator.

If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay:

(150.00 / 5) * 1.12 = 33.6

After formatting the result to 2 decimal places = 33.60
'''

print("Welcome to the tip calculator!")

bill_amount = input("What was the total bill? : $")
tip = input("How much tip would you like to give? 10, 12 or 15? : ")
number_of_people = input("How many people to split the bill? : ")

individual_bill = (float(bill_amount)/int(number_of_people))*(1+int(tip)/100)
print(f"Each person should pay : {round(individual_bill,2)}")

