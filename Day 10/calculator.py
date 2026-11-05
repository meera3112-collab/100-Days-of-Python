def add(num1, num2):
    """This function takes two numbers as inputs num1 and num2. 
    Add these two numbers and return their sum as output"""
    return num1 + num2

def sub(num1, num2):
    """This function takes two numbers as inputs num1 and num2. 
        subtract these two numbers and return their difference as output"""
    return num1 - num2

def mul(num1, num2):
    """This function takes two numbers as inputs num1 and num2. 
        multiply these two numbers and return their product as output"""
    return num1 * num2

def div(num1, num2):
    """This function takes two numbers as inputs num1 and num2. 
        Divide num1 by num2 and return it as output"""
    if num2 != 0:
        return num1/num2
    else: 
        return "Zero division error"

def calculator(input1, input2, operand):
    """This function takes 3 inputs and perform the desired 
    operation based on the operand on those inputs and return the answer"""
    if operand == '+':
        return add(input1, input2)
    elif operand == '-':
        return sub(input1, input2)
    elif operand == '*':
        return mul(input1, input2)
    elif operand == '/':
        return div(input1, input2)
    else:
        return "Invalid operand"