def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def subtract(n1, n2):
    return n1 - n2


operations = {
    "+": add,
    "*": multiply,
    "/": divide,
    "-": subtract,
}


def number_input():
    while True:
        try:
            a = int(input("Choose a number\n"))
            return a
        except ValueError or TypeError:
            continue


def calculate(n1, operand, number_two, dictionary):
    while operand != "*" and operand != "+" and operand != "-" and operand != "/":
        operand = str(input("Choose an operation * + - /\n"))
    number_two = number_input()

    return dictionary[operand](n1, number_two)


number_one = number_input()
again = ""
while again != "no":
    number_one = calculate(number_one, "", "", operations)
    print(number_one)
    again = ""
    while again != "yes" and again != "no":
        again = input("Would you like to go again")
