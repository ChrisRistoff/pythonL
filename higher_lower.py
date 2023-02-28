from higher_lower_data import data
import random


def ask_question(index_1):
    index_2 = random.randint(0, len(data))
    print(
        "Who has more followers?>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        + "A for "
        + data[index_2]["name"]
        + " from "
        + data[index_2]["country"]
        + "\n is a "
        + data[index_2]["description"]
        + "\n"
    )
    print("OR >>>>>>>>>>>>>>>>>>>>>")
    print(
        "B for "
        + data[index_1]["name"]
        + " from "
        + data[index_1]["country"]
        + "\n is a "
        + data[index_1]["description"]
        + "\n"
    )
    return index_2


def ask_for_answer(index_1, index_2):
    choice = ""
    while choice != "a" and choice != "b":
        choice = input("Choose A or B:\n").lower()
    if (
        choice == "A"
        and data[index_2]["follower_count"] > data[index_1]["follower_count"]
    ):
        print(
            "Correct, the answer was "
            + data[index_2]["name"]
            + " with "
            + str(data[index_2]["follower_count"])
            + " Million followers\n"
        )
        return index_2
    if (
        choice == "B"
        and data[index_1]["follower_count"] > data[index_2]["follower_count"]
    ):
        print(
            "Correct, the answer was "
            + data[index_1]["name"]
            + " with "
            + str(data[index_1]["follower_count"])
            + " Million followers\n"
        )
        return index_1
    else:
        print("Wrong, you're done\n")
        return -5


def play_again_prompt(again):
    while again != "y" and again != "n":
        again = input(
            "Would you like to play again?\ntype Y for yes or N for no\n"
        ).lower()
    if again == "y":
        return True
    else:
        return False


index_1 = random.randint(0, len(data))
counter = 0

again = True
while again:
    index_2 = ask_question(index_1)
    index_1 = ask_for_answer(index_1, index_2)

    if index_1 < 0:
        counter = 0
        again = play_again_prompt("")
    else:
        counter += 1
    print(f"You have {counter} points!")
