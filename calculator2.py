def add(n1, n2) :
    return n1 + n2
def multiply(n1, n2) :
   return n1 * n2
def divide(n1 ,n2) :
    return n1 / n2
def minus(n1 ,n2) :
    return n1 - n2

operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide
}

number_one = int(input("Choose a number\n"))
for key in operations:
    print(key)
operation_symbol = input("Pick an operation\n")
number_two = int(input("Choose a number\n"))

answer = operations[operation_symbol](number_one, number_two)

print(f"{number_one} {operation_symbol} {number_two} = {answer}")