import random

list_of_months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
]

paired_months = []

for i in range(0, len(list_of_months)):
    j = random.randint(0, len(list_of_months) - 1)

    temp = list_of_months[i]
    list_of_months[i] = list_of_months[j]
    list_of_months[j] = temp


print(list_of_months)
