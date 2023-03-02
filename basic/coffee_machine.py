menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 150,
    "coffee": 100,
    "money": 100,
}


def display_resources():
    print("You have\n" + str(resources["water"]) + " ml of water")
    print(str(resources["milk"]) + " ml of milk")
    print(str(resources["coffee"]) + " grams of coffee")
    print("$" + str(resources["money"]) + " in the machine")


def add_resources(resource_list, resource_choice, resource_quan):
    """prompts the user to pick a resource to add and returns the updated resource dictionary.
    takes the resource dictionary and 2 empty strings as parameters"""
    while (
        resource_choice != "water"
        and resource_choice != "milk"
        and resource_choice != "coffee"
        and resource_choice != "money"
    ):
        resource_choice = input(
            "Which resource would you like to update?\nWater, milk, coffee or money?"
        )
    while resource_quan == "":
        try:
            resource_quan = int(
                input(
                    f"How much {resource_choice} would you like to add or use - if you would like to remove?\n"
                )
            )
        except ValueError or TypeError:
            resource_quan = ""
            continue
    resource_list[resource_choice] += resource_quan
    return resource_list


def choice_prompt(choice, resource):
    """asks for user's choice of drink and lets you add resources
    to the coffee machine, takes two empty strings as a parameters"""
    valid_choices = ["espresso", "latte", "cappuccino", "report", "exit"]
    while choice not in valid_choices:
        choice = input(
            "Choose a drink from the list:\n Espresso,Latte, Cappuccino \n"
        ).lower()
        if choice == "report":
            print(display_resources())
            while resource != "yes" and resource != "no":
                resource = input("would you like to add resources?\n").lower()
            if resource == "no":
                choice = ""
                resource = ""
                continue
            else:
                return add_resources(resources, "", "")
    return choice


def insert_coin_prompt(choice, quarters, dimes, nickles, pennies):
    """takes coins for the drinks and returns the change
    takes 4 empty strings as parameters"""
    while quarters == "" and dimes == "" and nickles == "" and pennies == "":
        try:
            print("That will be $" + str(menu[choice]["cost"]))
            quarters = int(input("How many quarters were inserted? : \n"))
            dimes = int(input("How many dimes were inserted? : \n"))
            nickles = int(input("How many nickles were inserted? : \n"))
            pennies = int(input("How many pennies were inserted? : \n"))
        except ValueError or TypeError:
            continue
        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        change = total - menu[choice]["cost"]
    return change


def update_resources(resource_quant, choice):
    """updates the resources available to the machine after the order is complete
    takes the resources dictionary and users choice of drink as parameters"""
    resource_quant["money"] += menu[choice]["cost"]
    resource_quant["water"] -= menu[choice]["ingredients"]["water"]
    resource_quant["milk"] -= menu[choice]["ingredients"]["milk"]
    resource_quant["coffee"] -= menu[choice]["ingredients"]["coffee"]


while True:
    choice = choice_prompt("", "")
    while type(choice) != str:
        choice = choice_prompt("", "")
    if choice == "exit":
        print("Goodbye")
        break
    if (
        resources["water"] < menu[choice]["ingredients"]["water"]
        or resources["milk"] < menu[choice]["ingredients"]["milk"]
        or resources["coffee"] < menu[choice]["ingredients"]["coffee"]
    ):
        print("Sorry, there is not enough resources to make your drink")
        continue
    print("Your change is!\n$" + str(insert_coin_prompt(choice, "", "", "", "")))
    update_resources(resources, choice)
