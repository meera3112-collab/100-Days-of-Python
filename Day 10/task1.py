'''

TASK 1:

We've seen functions with only an execution body, functions with inputs that allow 
for variation in execution of the function body and now we'll see the final 
form of functions. Functions that can have outputs.

PAUSE 1
Create a function called format_name() that takes two inputs: f_name and `l_name'.'''

def format_name(f_name, l_name):
    pass

'''PAUSE 2
Use the title() function to modify the f_name and l_name parameters into Title Case.'''

def format_name(f_name, l_name):
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

print(format_name("MEERA", "VENKATAKRISHNAN"))
    

'''Syntax
You can create a function with a body, input and output like this:

def function_name(input_parameter):
    <body of function that uses input_argument>
    return output

Print vs. Output
Return vs. Display: The return statement is used to give back a value from a function, 
which can be used later, while print is used to display a value to the console only for the programmer to see.'''