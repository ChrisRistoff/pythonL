import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
question = ["_"] * len(chosen_word)
mistakes_left = 6
used_letters = [""]
print(question)
while chosen_word != ("".join(question)) and mistakes_left > 0:
    mistakes_made = 0
    question_index = 0
    guess = input("choose a letter: \n")
    if guess in used_letters:
        print("stop using that stupid")
        continue
    used_letters.extend(guess)

    for letter in chosen_word:
        if letter == guess:
            question[question_index] = guess
            question_index += 1
        elif letter != guess:
            question_index += 1
            mistakes_made += 1
        if mistakes_made == len(chosen_word):
            mistakes_left -= 1
            print(stages[mistakes_left + 1])

    print(" ".join(question))

if mistakes_left == 0:
    print(f"get rekt loser\n{stages[0]}")
else:
    print("you win")
