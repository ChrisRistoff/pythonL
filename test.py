menu = [{
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
            },

            {
            "chicken" : 13,
            "fish" : 20,
            "prawn" : 20,
            "beef" : 30,
            "pork" : 10,
            "lamb" : 30,
            "turkey" : 15,
            "duck" : 15,
            },

            {
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
]


class Shop:
    def __init__(self,choice):
        self.menu = menu
        self.bill = 0
        self.valid_choices = ["0","1","2","3","4","5"]
        self.cart = []
        self.choice = choice

    def take_user_choice(self):

        while True:
            print("1 for vegitables\n2 for meat\n3 for fruits\n"
            + "4 for cart\n5 for checkout\n0 for exit")
            choice= input("Enter your choice:")
            if choice in self.valid_choices:
                return choice
            else:
                continue


    def display_menu(choice):
        n = 1
        if choice in valid_choices[1:4]:
            for key,value in menu[int(choice) - 1].items():
                print(f"{n} {key}: £{value}")
                n += 1
        elif choice == "4":
            for item in cart:
                print(cart)
            print(f"Total: £{bill}")
        elif choice == "5":
            checkout()
        elif choice == "0":
            exit()



    def take_menu_choice(self):
        display_menu(choice)
        while True:
            try:
                item = int(input("Enter the item number you wish to add:\n"
                                 + "or Enter 0 to go back\n"))
                if item in range(0,len(menu[int(choice) - 1])+1):
                    return item
                print("Invalid choice")
                continue
            except ValueError:
                print("Invalid choice")
                continue

    def add_to_cart(self):
        item = take_menu_choice(choice)
        if item != 0:
            return
        all = [
        [key for key in menu[0].keys()],
        [key for key in menu[1].keys()],
        [key for key in menu[2].keys()],
        ]
        self.cart.append(all[choice-1][item-1])
        return



if __name__== "__main__":
    shop = Shop()
    while True:
        choice = shop.take_user_choice()
        shop.add_to_cart(choice)
        print(cart)







