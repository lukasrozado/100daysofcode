from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")
def add_new_bidder(name, bid):
  bidders.append({"name": name, "bid": bid})
bidders = []
more_bidders = ""
# First bidder input
name = str(input("What is your name? "))
bid = float(input("What is your bid? "))
add_new_bidder(name, bid)
more_bidders = str(input("Are there any more bidders? Type 'yes' or 'no' ")).lower()
# Loop for additional bidders
while more_bidders == "yes":
    clear()
    name = str(input("What is your name? "))
    bid = float(input("What is your bid? "))
    add_new_bidder(name, bid)
    more_bidders = str(input("Are there any more bidders? Type 'yes' or 'no' ")).lower()
# If the user enters something other than 'yes' or 'no', prompt again
while more_bidders != "yes" and more_bidders != "no":
    print("Invalid input. Please type 'yes' or 'no'.")
    more_bidders = str(input("Are there any more bidders? Type 'yes' or 'no' ")).lower()
# Find the highest bidder
highest_bidder = max(bidders, key=lambda x: x['bid'])
name_winner = highest_bidder["name"]
bid_winner = highest_bidder["bid"]
# Display the winner
print(f"The winner is {name_winner} with a bid of ${bid_winner}")
