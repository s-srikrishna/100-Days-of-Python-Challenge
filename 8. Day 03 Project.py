''' 
This is the Day 03 project.

It is Treasure Island.

It uses functionalities like condtional statements, logical operators and scope.
'''

print(''' \n
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************\n
''')

print("Welcome to Treasure Island.")
print("You're at a cross road. Where do you want to go?")
direction = input("You're at a cross road. Where do you want to go? \n \t Type 'left' or 'right' \n")
if(direction=="right"):
    print("Fall into a hole. Game Over.\n")
elif(direction=="left"):
    next_step = input("You've come to a lake. There is an island in the middle of the lake. \n \t Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
    if(next_step=="swim"):
        print("Attacked by trout. Game Over")
    elif(next_step=="wait"):
        door = input("You arrive at the island unharmed. There is a house with 3 doors. \n \t One red, one yellow and one blue. Which colour do you choose?\n")
        if(door=="red"):
            print("Burned by fire. Game Over.\n")
        elif(door=="blue"):
            print("Eaten by beasts. Game Over.\n")
        elif(door=="yellow"):
            print("You Win!\n")
        else:
            print("Game over.\n")
else:
    print("Game is over.")