from random import choice
from art import logo

# Logo
print(logo)
cards = [11, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player1_card1 = choice(cards)
player1_card2 = choice(cards)
player_initial_cards = [player1_card1, player1_card2]
total_initial_cards_player = sum(player_initial_cards)

computer_cards1 = choice(cards)
computer_cards2 = choice(cards)
computer_cards = [computer_cards1, computer_cards2]
total_initial_cards_computer = sum(computer_cards)

print(f"Player Initial Cards: {player_initial_cards}")
print(f"Total First Player: {total_initial_cards_player}")
print(f"Computer First Card: {computer_cards1}")

while total_initial_cards_player <= 21:
    choices = input("Do you want another card? Press 'Y' to get one or 'N' to stop the game: ").lower()

    if choices == "y":
        new_card = choice(cards)
        player_initial_cards.append(new_card)
        total_initial_cards_player = sum(player_initial_cards)
        print(f"New Card for Player: {new_card}")
        print(f"Total Player: {total_initial_cards_player}")
        
        if total_initial_cards_player > 21:
            print("Busted! You lose")
            break
    elif choices == "n":
        break
    else:
        print("Invalid input! Please enter 'Y' or 'N'.")

if total_initial_cards_player <= 21:
    print(f"\nComputer Cards: {computer_cards}")
    
    while total_initial_cards_computer < 17:  
        new_card = choice(cards)
        computer_cards.append(new_card)
        total_initial_cards_computer = sum(computer_cards)
        print(f"New Card for Computer: {new_card}")
        print(f"Computer Total: {total_initial_cards_computer}")

    if total_initial_cards_computer > 21:
        print("\nComputer Busted! You win!")
    elif total_initial_cards_computer > total_initial_cards_player:
        print(f"\nComputer Wins! Total: {total_initial_cards_computer}")
    elif total_initial_cards_computer < total_initial_cards_player:
        print(f"\nYou win! Total: {total_initial_cards_player}")
    else:
        print("\nIt's a tie!")
