from random import randint, choice

size = int(input("What's the size of the password? "))
password = ""

while len(password) < size:
    random_number = str(randint(1, 10))
    random_character = choice("abcdefghijklmnopqrstuvwxyz")
    random_character2 = random_character.upper()
    random_symbol = choice("!@#$%&")

    random_order = choice([random_number, random_character, random_symbol,random_character2, random_character, random_character2])

    if random_order not in password:
        password += random_order

print(password)