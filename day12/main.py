from random import randint

def guess_number_game(attempts):
    number = randint(1, 101)
    
    while attempts > 0:
        guess = int(input(f"You have {attempts} attempts remaining. Enter a guess: "))
        
        if guess == number:
            print("Congratulations! You guessed the correct number.")
            return
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")
        
        attempts -= 1
    
    print(f"You ran out of attempts. The correct number was {number}.")

print("Welcome to the Number Guessing Game!")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

if difficulty == "easy":
    guess_number_game(10)
elif difficulty == "hard":
    guess_number_game(5)
else:
    print("Invalid difficulty choice!")
