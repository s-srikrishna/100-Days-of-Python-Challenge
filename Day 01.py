## the print function prints the given string (or) number (or) character (or) input, on the console.

# Syntax => print() || [Text inserted between quotes " " (or) ' ' are strings and parenthesis - (), indicates the beginning and end of strings.]

print("Hello World!") # here input is a string

print('Hello World!') # here input is a string

print("a") # here input is a character

print('a') # here input is a character

print(2024) # here input is a number, precisely an integer 

print(2024.2024) # here input is a number, precisely an float 

# The above code can be written with single print function as below.

print("Hello World!", 2024)

# or rewritten as below.

print("Hello World!\n2024")

# print() with modifiers

print('She said: "Hello" and then left.')

print("She said: 'Hello' and then left.")

print("She said: \"Hello\" and then left.")

# print() exercise

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# print() with "\n" - next line / new line

print("Hi\nHi\nHi\nHi")

# Comments in python - "#" is used for single-line comment and """ / ''' are used for multi-line command.

# This is single-line comment

""" This is multi-line comment """ 

''' This is also multi-line comment '''

## String Concatenation (merging set of characters) is done using "+" and can be done directly in print() itself

print("Hello" + "World" + "!") # prints all as a single word

print("Hello" + " " + "World" + "!")

## Example of errors (as errors don't make a program run, I'm giving them as multi-line comments so you understand them.)

'''
rint("Hello World") -> Throws Syntax Error
print("Hello World) -> Throws Syntax Error
print("Hello World" -> Throws Syntax Error
    print("Hello World") -> Throws Indentation Error (Indentation is really important in python.)
'''

# Debugging in Python

# Fix the code below 👇

'''
print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
'''

# corrected / debugged code

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# The input function in Python gets the input from the user on the console and uses it in prompted places.

input("Your name is : ") # typical input statement

# integrating print() and input()

print("Hello! " + input("How are you?\n"))

# using specific data type for input functions

num1 = int(input("Enter the first number: ")) # num1 and num2 are containers the values of a variable assigned to them.
num2 = int(input("Enter the second number: ")) 
print("Result is: ", num1*num2) # "*" is the multiplication operator | operators will be covered later.

# additional features in python: feature 01 - len() returns the length of given (or) taken string.

numofletters = len("Sri Krishna")

# dynamic working of len() for any input 👇🏻

length=len(input())
print(length)

# additional features in python: feature 02 - f-string is used to print and run the prompt / function in one single line, wrapped in { }.

print(f"The total number of characters in given input is: {numofletters}")

# Variables

'''
Variables are the containers that store the values of assigned entitites. 
They are of many types. 
Some of the most commonly used are: int, float, str, char etc...
Python is Case-Sensitive, means that, "Var" and "var" are not same.
'''

name=input()
print(name)

# Python uses the recently store value in a variable.

num_x = 3
num_x = 5 
print(num_x)

# while running this code snippet, python uses the value of 'num_x' to be "5" and print() will print "5"

## Swapping variables and their values using temp :

# There are two variables, a and b from input
a = input()
b = input()

# introducting the temp variable

temp=a
a=b
b=temp

print("a: " + a)
print("b: " + b)

# Note : for an assignment statement, x=y -> The value of "y" is stored in "x"

''' 
variable naming standards -
    1) Use proper names for variables -> use "number" instead of "n".
    2) Keyworkd like print, input, lambda, if, elif, else etc..
    3) Only alphabets, numericals and underscores are allowed in Python -> "number1", "num1", "number_1" and note a variable name cannot start with number while there is no such restriction for aplhabet and underscore.

When a typo happens while calling a specific variable, it returns a "Name Error" stating that the specific variable name is 'not define'!!!
'''