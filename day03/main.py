print('''
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure chest")

choice1 = str(input("You are at the crossroad, where do you wan to go? Type: 'left' or 'right'")).lower().strip()
if choice1 == "left":
    choice2 = str(input("You\'ve come to a lake. There is a island in the middle of the lake. Type 'swim' to swim across or 'wait' for a boat")).lower().strip(  )
    if choice2 == "wait":
        choice3 = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Type the choice 'red' or 'blue' or 'yellow'")).lower().strip()
        if choice3 == "red": 
            print("It's a room full of fire: Game Over.")
        elif choice3 == "blue":
            print("You enter in the room full of beasts. Game Over.")
        elif choice3 ==  "yellow":
            print("You found the treasure chest. You Win!")
        else:
            print("You choose a door that doesn't exist. Game Over.")
            
    else:
        print("You got attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over")
