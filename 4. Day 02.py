## len() revision

length=len("Hello")
print(length)   # (or)

print(len("Hello"))

# but when we give numbers instead of string in len(), it returns a "type-error"

# for example, print(len(12345)) -> TypeError: object of type 'int' has no len().

'''
Data types to be learned today are:

    1) Strings
    2) Integer
    3) Float
    4) Boolean
'''

## for srings, we can extract using individual characters by using the "index values". For example,

print("Hello"[0]) # return "H" at index 0.

print("Hello"[-5]) # negative values indicate counting from reverse!

# this method of pulling out a seperate character from a string is called "subscripting".

# type () is used to retrive the type of data used / given. 

## Integer = number without decimal and are whole numbers.

print(123+345)
print(type(123+345))

# for representing lakhs / millions / billions, we use "_" instead of ","

print(100_000_000) # and not 100,000,000 which is 100 Millions (or) 10 Crores.

## Float = Floating point number with decimal places.

print(123.51)
print(type(123.51))

## Boolean = True or False. And they always begin with a "T" and "F" and not "t" and "f" respectively.

# Booleans are mostyly used in conditionals and check statements.

print(True)
print(False)

# utilising type()

print(type("hello"))
print(type(123456))
print(type(123.456))
print(type(True))

# "type conversion" (or) "type casting" allows you to convert one datatype to another by introducing a new variable and the type of data you want as a function of existing variable. For example,

age = input() # here, the age is considered as a string input as input() by default takes string as the datatype.

# to convert, age to int type from str type, the following is done :

age_new = int(age) # now the variable age_new stores the value of age in int type.

print(age_new + 100)

# but, some conversions are not allowed, like, int(abc) cannot be convereted to integer and it returns a "Value Error".

'''print("Number of letters in your name: " + len(int(input("Enter you name: ")))) -> throws value error '''

name = input("Enter your name: ")
length = len(name)
length_of_name = str(length)
print("Number of letters in your name: " + length_of_name)

# Mathematical operations in Python

print(2 + 2) # sum operator
print(2 - 2) # subtraction operator
print(2 * 2) # multiplication operator
print(2 / 2) # division operator, which by default gives float result (implicit typecasting)
print(2 % 2) # modulo, gives the remainder of a division
print(2 // 2) # double division, gives the quotient of a division
print(2 ** 2) # power of operator (exponential)

## Priority order of operators => PEMDAS = Parenthesis, Exponential, Multiplication, Division, Addition, Subtraction.

print(3 * 3 + 3 / 3 - 3) # prints 7

print(3 * (3 + 3) / 3 - 3) # prints 3 -> Parenthesis matters.

print(5/3) # gives the answer in float, i.e., 1.6666666...
print(round(5/3)) # gives the answer in rounded off format, since 1.666 rounded off is 2, it returns 2.
print(round(5/3, 2)) # rounding off to two digits
print(int(5/3)) # gives only the quotient of the division ignoring the decimals.

# assigning a new value to a variable based on it's previous value is done with the following operators : +=. -=. *=. /=

score = 0
score += 1
print(score)
score -= 1
print(score)
score *= 1
print(score)
score /= 1
print(score)