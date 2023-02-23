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
    "*": multiply,
    "/": divide,
    "-": minus,
}

def calculation (n1, operand,dic) :
    while operand != "*" and operand != "+" and operand != "-" and operand != "/" :
        operand = str(input("Choose an operation * + - /\n"))
    number_two = int(input("Choose a number\n"))
    return dic[operand](n1, number_two)

def go_again(a) :
    while a != "yes" :
        if a == "no" :
            break
        else :
            a = input("would you like to go again?\n")
    return a

number_one = int(input("Choose a number\n"))
again = ""
while again != "no" :
    number_one = calculation(number_one, "", operations)
    print(number_one)
    again = go_again("")
