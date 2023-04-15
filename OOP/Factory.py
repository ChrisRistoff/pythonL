class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


class BurgerFactory():

    def create_cheeseburger(self):
        return Burger(['cheese', 'beef'])

    def create_veggieburger(self):
        return Burger(['cheese', 'tomato', 'lettuce'])

    def create_hamburger(self):
        return Burger(['beef'])


if __name__ == '__main__':
    burger_factory = BurgerFactory()
    cheeseburger = burger_factory.create_cheeseburger()
    cheeseburger.print()
    veggieburger = burger_factory.create_veggieburger()
    veggieburger.print()
    hamburger = burger_factory.create_hamburger()
    hamburger.print()


# the Factory pattern is a creational pattern that allows us to
# create objects without exposing the instantiation logic to the
# client and refer to newly created objects using a common interface
