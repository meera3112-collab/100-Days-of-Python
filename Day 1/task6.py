'''
FINAL PROJECT : BRAND NAME GENERATOR

Create a greeting for your program.
Ask the user for the city that they grew up in and store it in a variable.
Ask the user for the name of a pet and store it in a variable.
Combine the name of their city and pet and show them their band name.
Make sure the input cursor shows on a new line:
'''

print("Hello! Welcome to the Brand name generator")

city=input("Enter the city name you grew up in: \n")
pet_name=input("Enter the name of your first pet: \n")

print("Name of your band name could be:",city + " " + pet_name)