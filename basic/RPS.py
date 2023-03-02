import random

rock = "rock"
paper = "paper"
scissors = "scissors"

listo = [rock, paper, scissors]

x = int(input("Choose 1 for rock, 2 for pape, 3 for scissors\n"))
y = random.randint(1, 3)

if x >= 4 and x < 0:
    print("Invalid choice")
else:
    print(f"You chose\n {listo[x - 1]}\n Computer chose\n {listo[y - 1]}")

if (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
    print("YOU WIN")
elif x == y:
    print("DRAW")
else:
    print("YOU LOSE")
