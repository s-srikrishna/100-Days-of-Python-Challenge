''' 
This is the Day 02 project.

It is a Tip Calculator.

it uses functionalities like data type integration, numbers and operations and f=strings.
'''
print("\nWelcome to tip calculator!")

bill = float(input("\nWhat was the total bill? $ "))

tip = float(input("\nHow much tip would you like to give? 10%, 12%, or 15%? "))

people = int(input("\nHow many people to split the bill? "))

tip_percent = bill * (tip/100)

final_split = ((bill + tip_percent) / people)

print(f"\nEach person should pay: ${round(final_split,2)} \n")