import random


def choose_difficulty():
    a = ""
    while a.lower() != "e" and a.lower() != "h":
        a = input(
            "Choose difficulty, easy or hard\nE for easy = 10 lives\nH for hard = 5 lives\n" 
        )
    if a == "e":
        return 10
    else:
        return 5


def play_game(lives, number):
    player_input = 0
    list_of_used_numbers = []
    while number != player_input and lives > 0:
        player_input = 101
        while player_input > 100:
            try:
                player_input = int(input("Choose a number between 1 and 100 :\n"))
            except ValueError or TypeError:
                continue

        if player_input in list_of_used_numbers:
            print("You already guessed this number.")
        elif number < player_input:
            lives -= 1
            list_of_used_numbers.append(player_input)
            print(f"Number is too high\n You have {lives} lives left")
        elif number > player_input:
            lives -= 1
            list_of_used_numbers.append(player_input)
            print(f"Number is too low\n You have {lives} lives left")
    return lives


def check_score(lives, number):
    if lives > 0:
        return f"You win! The number was {number}. You had {lives} lives left!"
    else:
        return f"You are out of lives, the number was {number}"


def play():
    number = random.randint(1, 100)
    lives = choose_difficulty()
    lives = play_game(lives, number)
    print(check_score(lives, number))


def play_again_prompt():
    a = ""
    while a != "y" and a != "n":
        a = input("Do you want to play again?\nN for no\nY for yes\n")
    if a == "y":
        return True
    else:
        return False


again = True
while again:
    play()
    again = play_again_prompt()
