def add(n1, n2) :
    return n1 + n2
def multiply(n1, n2) :
   return n1 * n2
def divide(n1 ,n2) :
    return n1 / n2
def minus(n1 ,n2) :
    return n1 - n2

def calculation (n1, operand) :
    while operand != "*" and operand != "+" and operand != "-" and operand != "/" :
        operand = str(input("Choose an operation * + - /\n"))
    number_two = int(input("Choose a number\n"))
    if operand == "*" :
        g = multiply(n1, number_two)
    elif operand == "-" :
        g = minus(n1, number_two)
    elif operand == "+" :
        g = add(n1, number_two)
    else :
        g = divide(n1, number_two)
    return g
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
    number_one = calculation(number_one, "")
    print(number_one)
    again = go_again("")
