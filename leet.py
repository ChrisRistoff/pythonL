numbers = int(input("numbers\n"))
newNumbers = str(numbers)
g = [""]
gg = False
for number in newNumbers:
    if number in g:
        gg = True
    if number not in g:
        g += number
print(gg)
