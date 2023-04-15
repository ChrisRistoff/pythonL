class Burger():
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def set_buns(self, buns):
        self.buns = buns

    def set_patty(self, patty):
        self.patty = patty

    def set_cheese(self, cheese):
        self.cheese = cheese

    def __str__(self):
        return f'Burger with {self.buns}, {self.patty} and {self.cheese}'


class BurgerBuilder():
    def __init__(self):
        self.burger = Burger()

    def add_buns(self, buns):
        self.burger.set_buns(buns)
        return self

    def add_patty(self, patty):
        self.burger.set_patty(patty)
        return self

    def add_cheese(self, cheese):
        self.burger.set_cheese(cheese)
        return self

    def build_burger(self):
        return self.burger


burger = BurgerBuilder()\
    .add_buns('basic').add_patty('beef')\
    .add_cheese('mozarella').build_burger()

print(burger)


# the Builder pattern is a creational pattern that allows us to
# construct complex objects step by step
# the pattern allows you to produce different types and representations
# of an object using the same construction code
# the pattern is used to separate the construction of a complex object
# from its representation so that the same construction process can
# create different representations
