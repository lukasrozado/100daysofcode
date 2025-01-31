from random import randint

computer_choice = randint(1, 3)

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
user_choice = int(input("Choose a option between: Type the value \n 1 - Rock \n 2 - Paper \n 3 - Scissors "))
game_images = [rock, paper, scissor]
print("The User Choice")
print(game_images[user_choice-1])
print("The Computer Choice: ")
print(game_images[computer_choice-1])

if computer_choice == user_choice:
    print("It's a draw")
elif user_choice  == 1 and computer_choice == 3:
    print("You Win!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == 3 and computer_choice == 2:
    print("You Win")
else:
    print("You Lose")