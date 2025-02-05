from random import choice

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


words = [
    "apple", "banana", "computer", "ocean", "mountain", "guitar", "sunshine",
    "elephant", "breeze", "whisper", "adventure", "galaxy", "notebook",
    "puzzle", "rainbow", "journey", "fireplace", "midnight", "harmony", "lantern"
]


def generate_word():
    return choice(words)


word_to_guess = generate_word()
word_search_updated = list("-" * len(word_to_guess))
life = 6

print("Welcome to hangman")
print("The Word has", len(word_to_guess), "letters.")
print(" ".join(word_search_updated))

while "-" in word_search_updated and life > 0:
    letter = input("Choose a letter ").lower()

    if letter in word_to_guess:
        for index, char in enumerate(word_to_guess):
            if char == letter:
                word_search_updated[index] = letter
    else:
        life -= 1
        print(stages[life])
        print(f"You lost 1 life you have {life} lifes.")

    print(" ".join(word_search_updated))

if "-" not in word_search_updated:
    print("Congrats, You Won!")
else:
    print(f"You Lost! The Word was:  {word_to_guess}")