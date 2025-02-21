from data import resources, MENU

quarters = 0.25
dimes = 0.1
nickles = 0.05
pennies = 0.01
water_machine = resources["water"]
milk_machine = resources["milk"]
coffe_machine = resources["coffee"]
money_machine = resources["money"]


def process_coins():
    count_quarters = int(input("Insert the quantity of quarters: "))
    count_dimes = int(input("Insert the quantity of dimes: "))
    count_nickles = int(input("Insert the quantity of nickels: "))
    count_pennies = int(input("Insert the quantity of pennies: "))
    total = (count_quarters * quarters) + (count_dimes * dimes) + (count_nickles * nickles) + (count_pennies * pennies)
    return total


def check_resources(drink):
    ingredients = drink["ingredients"]
    water_needed = ingredients["water"]
    milk_needed = ingredients.get("milk", 0)
    coffee_needed = ingredients["coffee"]

    if water_needed > water_machine:
        print("Sorry, there is not enough water.")
        return False
    if milk_needed > milk_machine:
        print("Sorry, there is not enough milk.")
        return False
    if coffee_needed > coffe_machine:
        print("Sorry, there is not enough coffee.")
        return False
    return True


def make_coffee(drink):
    global water_machine, milk_machine, coffe_machine, money_machine
    ingredients = drink["ingredients"]
    water_needed = ingredients["water"]
    milk_needed = ingredients.get("milk", 0)
    coffee_needed = ingredients["coffee"]
    water_machine -= water_needed
    milk_machine -= milk_needed
    coffe_machine -= coffee_needed
    money_machine += drink["cost"]


# MAIN
machine_status = True
while machine_status:
    user_choice = str(input("What would you like? (espresso/latte/cappuccino):"))

    if user_choice == "off":
        machine_status = False
        print("Turning off the coffee machine.")
        break

    if user_choice == "report":
        print(f"Water: {water_machine}ml")
        print(f"Milk: {milk_machine}ml")
        print(f"Coffe: {coffe_machine}g")
        print(f"Money: ${money_machine}")
        continue

    # Choose the drink
    if user_choice in MENU:
        selected_drink = MENU[user_choice]
        if not check_resources(selected_drink):
            continue

        print(f"Price: ${selected_drink['cost']}")
        total_money = process_coins()

        if total_money < selected_drink['cost']:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            change = total_money - selected_drink['cost']
            if change > 0:
                print(f"Here is your change: ${change:.2f}")
            make_coffee(selected_drink)
            print(f"Here is your {user_choice}. Enjoy!")

    else:
        print("Invalid choice. Please select a valid drink (espresso, latte, cappuccino).")
