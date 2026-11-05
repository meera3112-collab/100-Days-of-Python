# TASK 3: CALCULATOR

from art import logo
import calculator

continue_calculation = False
new_calculation = True
output = 0

while continue_calculation or new_calculation:
    if new_calculation:
        print(logo)
        input1 = float(input("What's the first number: "))
    else:
        input1 = output
    print("+\n-\n*\n/\n")
    operand = input("Pick an operation: ")
    input2 = float(input("What's the second number: "))
    output = calculator.calculator(input1, input2, operand)
    print(f"{input1} {operand} {input2} = {output}")
    choice = input(f"Type 'y' to continue calculating with {output} , type 'n' to start a new calculation or 'e' to exit from the code: ")
    if choice == 'y':
        continue_calculation = True
        new_calculation = False
    elif choice == 'n':
        continue_calculation = False
        new_calculation = True
    else: 
        continue_calculation = False
        new_calculation = False

