from art import logo, vs
from game_data import data
from random import randint

print(logo)

score = 0
while True:
    index = randint(0, len(data)-1)
    random_data = data[index]
    random_name = random_data["name"]
    random_follower = random_data["follower_count"]
    random_description = random_data["description"]
    random_country = random_data["country"]
    print(f"{random_name}, a {random_description} from {random_country}")

    print(vs)

    index2 = randint(0, len(data)-1)
    random_data2 = data[index2]
    random_name2 = random_data2["name"]
    random_follower2 = random_data2["follower_count"]
    random_description2 = random_data2["description"]
    random_country2 = random_data2["country"]
    print(f"{random_name2}, a {random_description2} from {random_country2}")

    choice = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if choice == "A":
        if random_follower > random_follower2:
            score += 1
            print(f"You're right!, Current score: {score}")
            data.pop(index)
        else:
            print(f"You're wrong! Current score: {score}")
            break
    elif choice == "B":
        if random_follower2 > random_follower:
            score += 1
            print(f"You're right!, Current score: {score}")
            data.pop(index2)
        else:
            print(f"You're wrong! Current score: {score}")
            break
    else:
        print("Invalid input! Please type 'A' or 'B'.")

print(f"Total Score: {score}")
