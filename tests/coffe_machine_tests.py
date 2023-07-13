import unittest
from coffee_machine_Objects import CoffeeMachine


class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        self.coffee_machine = CoffeeMachine()

    def test_initial_resources(self):
        self.assertEqual(self.coffee_machine.resources['water'], 300)
        self.assertEqual(self.coffee_machine.resources['milk'], 150)
        self.assertEqual(self.coffee_machine.resources['coffee'], 100)
        self.assertEqual(self.coffee_machine.resources['money'], 100)

    def test_add_water(self):
        self.coffee_machine.add_resources('water', 50)
        self.assertEqual(self.coffee_machine.resources['water'], 350)

    def test_add_milk(self):
        self.coffee_machine.add_resources('milk', 20)
        self.assertEqual(self.coffee_machine.resources['milk'], 170)

    def test_add_coffee(self):
        self.coffee_machine.add_resources('coffee', 30)
        self.assertEqual(self.coffee_machine.resources['coffee'], 130)

    def test_add_money(self):
        self.coffee_machine.add_resources('money', 5)
        self.assertEqual(self.coffee_machine.resources['money'], 105)

    def test_choice_prompt_exit(self):
        self.assertEqual(self.coffee_machine.choice_prompt(), 'exit')

    def test_choice_prompt_report(self):
        self.assertEqual(self.coffee_machine.choice_prompt(), 'report')

    def test_choice_prompt_espresso(self):
        self.assertEqual(self.coffee_machine.choice_prompt(), 'espresso')

    def test_choice_prompt_latte(self):
        self.assertEqual(self.coffee_machine.choice_prompt(), 'latte')

    def test_choice_prompt_cappuccino(self):
        self.assertEqual(self.coffee_machine.choice_prompt(), 'cappuccino')

    def test_insert_coin_prompt(self):
        self.coffee_machine.insert_coin_prompt('espresso', 1, 1, 1, 1)
        self.assertEqual(self.coffee_machine.resources['money'], 101.5)

    def test_update_resources_espresso(self):
        self.coffee_machine.update_resources('espresso')
        self.assertEqual(self.coffee_machine.resources['water'], 250)
        self.assertEqual(self.coffee_machine.resources['milk'], 150)
        self.assertEqual(self.coffee_machine.resources['coffee'], 82)
        self.assertEqual(self.coffee_machine.resources['money'], 101.5)

    def test_update_resources_latte(self):
        self.coffee_machine.update_resources('latte')
        self.assertEqual(self.coffee_machine.resources['water'], 100)
        self.assertEqual(self.coffee_machine.resources['milk'], 0)
        self.assertEqual(self.coffee_machine.resources['coffee'], 76)
        self.assertEqual(self.coffee_machine.resources['money'], 104)

    def test_update_resources_cappuccino(self):
        self.coffee_machine.update_resources('cappuccino')
        self.assertEqual(self.coffee_machine.resources['water'], 50)
        self.assertEqual(self.coffee_machine.resources['milk'], 50)
        self.assertEqual(self.coffee_machine.resources['coffee'], 76)
        self.assertEqual(self.coffee_machine.resources['money'], 107)


if __name__ == '__main__':
    unittest.main()
