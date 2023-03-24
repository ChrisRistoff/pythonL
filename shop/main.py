vegitables = {
            "potato" : 2,
            "tomato" : 3,
            "onion" : 1,
            "cabbage" : 0.20,
            "carrot" : 2,
            "brinjal" : 3,
            "cauliflower" : 2,
            "spinach" : 3,
            "capsicum" : 4,
            "cucumber" : 2,
            }

meat = {
            "chicken" : 13,
            "fish" : 20,
            "prawn" : 20,
            "beef" : 30,
            "pork" : 10,
            "lamb" : 30,
            "turkey" : 15,
            "duck" : 15,
            }

fruits = {
            "apple" : 3,
            "banana" : 1,
            "mango" : 3,
            "grapes" : 2,
            "pineapple" : 5,
            "watermelon" : 0.40,
            "papaya" : 7,
            "strawberry" : 5,
            "orange" : 2,
            "cherry" : 3,
            }


bill = 0


def take_user_choice():
    valid_choices = ["0","1","2","3","4","5"]

    while True:
        print("1 for vegitables\n2 for meat\n
        3 for fruits\n4 for checkout\n5 for exit\n")
       choice= input("Enter your choice:\n")

        if choice in valid_choices:
            return choice
        else:
            continue


def display_menu(user_choice):
    if user_choice == "1":
        print("vegitables are:\n")
        for item in vegitables:
            print(item)

    elif user_choice == "2":
        print("meat are:\n")
        for item in meat:
            print(item)

    elif user_choice == "3":
        print("fruits are:\n")
        for item in fruits:
            print(item)

    elif user_choice == "4":
        print("Checkout")

    elif user_choice == "5":
        exit()

def add_to_card()















