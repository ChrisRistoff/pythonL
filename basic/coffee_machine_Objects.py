class CoffeeMachine:
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 150,
            "coffee": 100,
            "money": 100,
        }
        self.menu = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "milk": 0,
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

    def get_resources(self):
        print("You have\n" + str(self.resources["water"]) + " ml of water")
        print(str(self.resources["milk"]) + " ml of milk")
        print(str(self.resources["coffee"]) + " grams of coffee")
        print("$" + str(self.resources["money"]) + " in the machine")

    def add_resources(self, resource_choice, resource_quan):
        """prompts the user to pick a resource to add and returns the updated resource dictionary.
        takes the resource dictionary and 2 empty strings as parameters"""
        valid_choices = ["water", "milk", "coffee", "money"]
        while resource_choice not in valid_choices:
            resource_choice = input(
                "Which resource would you like to update?\nWater, milk, coffee or money?\n"
            )
        while resource_quan == "":
            try:
                resource_quan = int(
                    input(
                        f"How much {resource_choice} would you like to add or use - if you would like to remove?\n"
                    )
                )
            except ValueError or TypeError:
                print("Please enter a valid number")
                continue
        self.resources[resource_choice] += resource_quan
        print(f"You have {self.resources[resource_choice]} {resource_choice} left")
        return self.resources

    def choice_prompt(self):
        """prompts the user to pick a drink and returns the drink choice"""
        viable_choices = ["espresso", "latte", "cappuccino", "report", "exit"]
        choice = ""
        while choice not in viable_choices:
            choice = input(
                "Type report for resources\nWhat would you like to drink?\nEspresso, latte or cappuccino?\n"
            )
        if choice == "report":
            CoffeeMachine.get_resources(self)
            choice = ""
            add_resources = input("Would you like to add resources?\n")
            while add_resources == "yes":
                CoffeeMachine.add_resources(self, "", "")
                add_resources = input("Would you like to add resources?\n")
            else:
                return self.resources
        return choice

    def insert_coin_prompt(self, choice, quarters, dimes, nickles, pennies):
        """prompts the user to insert coins and returns the change
        takes user's choice of drink and 4 empty strings as an argument"""

        while quarters == "" or dimes == "" or nickles == "" or pennies == "":
            try:
                quarters = int(input("How many quarters would you like to insert? : "))
                dimes = int(input("How many dimes would you like to insert? : "))
                nickles = int(input("How many nickles would you like to insert? : "))
                pennies = int(input("How many pennies would you like to insert? : "))
            except ValueError or TypeError:
                print("Please enter a number\n START OVER\n")
                continue

        total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if total < self.menu[choice]["cost"]:
            print(
                "Sorry, that's not enough money $"
                + self.menu[choice]["cost"]
                + " refunded."
            )
            return
        change = round(total - self.menu[choice]["cost"], 3)
        print(f"Here is your {choice} and ${change} in change")
        return

    def update_resources(self, choice):
        """updates the resources dictionary after a drink has been made"""
        if self.resources["water"] - self.menu[choice]["ingredients"]["water"] < 0:
            print("Sorry, there is not enough water")
            return False
        else:
            self.resources["water"] -= self.menu[choice]["ingredients"]["water"]
        if self.resources["milk"] - self.menu[choice]["ingredients"]["milk"] < 0:
            print("Sorry, there is not enough milk")
            return False
        else:
            self.resources["milk"] -= self.menu[choice]["ingredients"]["milk"]
        if self.resources["coffee"] - self.menu[choice]["ingredients"]["coffee"] < 0:
            print("Sorry, there is not enough coffee")
            return False
        else:
            self.resources["coffee"] -= self.menu[choice]["ingredients"]["coffee"]
        self.resources["money"] += self.menu[choice]["cost"]
        return self.resources


def main():
    object = CoffeeMachine()
    while True:
        choice = object.choice_prompt()
        while type(choice) != str:
            choice = object.choice_prompt()
        if choice == "exit":
            print("Goodbye")
            break
        res_update = object.update_resources(choice)
        if res_update == False:
            continue
        object.insert_coin_prompt(choice, "", "", "", "")


if __name__ == "__main__":
    main()
