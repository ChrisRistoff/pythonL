import random
from random import shuffle
import string

letters = string.ascii_letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []


for i in range(0, nr_letters) : 
    password += random.choice(letters)
for o in range(0, nr_numbers) :
    password += random.choice(numbers)
for p in range(0, nr_symbols) :
    password += random.choice(symbols)
    
print(''.join(password))
x = random.sample(password, len(password))

print(''.join(x))