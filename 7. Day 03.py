## conditionals primarily come from the if-else combination

'''
The syntax for if-else statement is given as:

if condition:
    print statement; -> statement to be executed when the condition gets satisfied.
else:
    print statement; -> statement to be executed when the condition doesn't gets satisfied.
'''


## a simple example for working of if-else block :

age = int (input("Enter your age: "))

if (age>=18):
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

'''
Some common operations include : 
    >       (Greater than) 
    >=      (Greater than or Equal to)
    <       (Lesser than)
    <=      (Lesser than or Equal to)
    ==      (Equal to)
    !=      (Not Equal to)

Note : "=" is for assignment operation whereas, "==" is for checking equality.
'''

number = int (input("Enter the number: "))

if (number %2 == 0):
    print("Number is even.")
    if (number >= 10):
        print("This is more than a decade.")
    else:
        print("The number is less than a decade.")
else:
    print("Number is odd.")

## practice 2 for nested conditionals

# el-if is a comabination of else and if, used when there are >2 conditions => there can be many elif in a single block of code.

print("Welcome to roller coaster!")

height = int(input("Enter your height in centimeters: "))
age = int(input("Enter your age: "))

if (height>120):
    print("You're allowed to ride on a roller coaster.")
    if (age>18 and age<22):
        print("You have to pay $12!")
    elif (age>22 and age<40):
        print("You have to pay $20!")
    else:
        print("You have to pay $7!")
else:
    print("You're not allowed to ride on a roller coaster.")

# use of multiple elif :


marks = int(input("Enter the marks: "))

if(marks>=0 and marks<=100):
    print("You've entered a valid mark.")
    if(marks>=0 and marks<=25):
        print("The student has failed the subject.")
    elif (marks>=26 and marks<=50):
        print("The student will get a C.")
    elif (marks>=51 and marks<=60):
        print("The student will get a B.")
    elif (marks>=61 and marks<=70):
        print("The student will get a B+.")
    elif (marks>=71 and marks<=80):
        print("The student will get a A.")
    elif (marks>=81 and marks<=90):
        print("The student will get a A+.")
    else:
        print("The student will get a O.")
else:
    print("You've entered an invalid mark.")

# multiple if statements will be used in case of many conditions to be checked. For example,

age = int(input("Enter your age: "))
photo = input("Do you want a photo or not? Y for Yes and N for No - ")
if(age>18):
    print("Eligible to ride")
if(photo=="Y"):
    print("Pic Required")

# Logical condtional operators : and / or / not

age = int(input("Enter your Age: "))
if(age>=18 and age<=100):
    print("Your are an adult.")
elif(age>0 and age<18 or age>100):
    print("You're a child.")
elif(not age < 0):
    print("You're inhumane")
else:
    print("Who are you?")

# Some boolean operations on Logical condtional operators : and / or / not

'''
X | Y | X and Y | X or Y | not (X) | not (Y)

T | T |    T    |    T   |    F    |    F   
T | F |    F    |    T   |    F    |    T    
F | T |    F    |    T   |    T    |    F    
F | F |    F    |    F   |    T    |    T    
'''
