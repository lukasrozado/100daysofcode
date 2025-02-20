from data import resources, MENU

# TODO - 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

user_choice = str(input("What would you like? (espresso/latte/cappuccino):"))

water_machine = resources["water"]
milk_machine = resources["milk"]
coffe_machine = resources["coffee"]
money_machine = resources["money"]

# Espresso
espresso = MENU["espresso"]
espresso_ingredients = espresso["ingredients"]
espresso_water = espresso_ingredients["water"]
espresso_coffe = espresso_ingredients["coffee"]
espresso_cost = espresso["cost"]


# Latte
latte = MENU["latte"]
latte_ingredients = latte["ingredients"]
latte_water = latte_ingredients["water"]
latte_milk = latte_ingredients["milk"]
latte_coffe = latte_ingredients["coffee"]
latte_cost = latte["cost"]

# Cappuccino

cappuccino = MENU["cappuccino"]
cappuccino_ingredients = cappuccino["ingredients"]
cappuccino_water = cappuccino_ingredients["water"]
cappuccino_milk = cappuccino_ingredients["milk"]
cappuccino_coffe = cappuccino_ingredients["coffee"]
cappuccino_cost = cappuccino["cost"]

# TODO - 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
machine_status = True
while machine_status:
    if user_choice == "off":
        machine_status = False
# TODO - 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
    if user_choice == "report":
        print(f"Water: {water_machine}ml")
        print(f"Milk: {milk_machine}ml")
        print(f"Coffe: {coffe_machine}g")
        print(f"Money: ${money_machine}")
        break

# TODO - 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
    if user_choice == "espresso":
        if espresso_water >= water_machine and espresso_coffe >= coffe_machine:
            print("Doing your espresso")
            print("The Request of espresso is finished")
    if user_choice == "latte":
        if latte_milk >= milk_machine and latte_coffe >= coffe_machine and latte_water >= water_machine:
            print("Doing your latte")
            print("The Request of latte is finished")
    if user_choice == "cappuccino":
        if cappuccino_milk >= milk_machine and cappuccino_coffe >= coffe_machine and cappuccino_water >= water_machine:
            print("Doing your cappuccino")
            print("The Request of cappuccino is finished")

# TODO - 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

    count_quarters = 0
    count_dimes = 0
    count_nickles = 0
    count_pennies = 0
    quarters = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01

# TODO - 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# TODO - 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink
    user_choice = str(input("What would you like? (espresso/latte/cappuccino):"))

