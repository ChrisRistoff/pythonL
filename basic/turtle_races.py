from turtle import *
import random

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
screen = Screen()
screen.setup(width=500, height=400)

for index in range(0, 6):
    new_tirtle = Turtle(shape="turtle")
    new_tirtle.color(colors[index])
    new_tirtle.penup()
    new_tirtle.goto(-230, y_positions[index])
    all_turtles.append(new_tirtle)

user_bet = False
while user_bet not in colors:
    user_bet = screen.textinput(
        title="make your bet", prompt=f"enter a color {colors}: "
    )

while user_bet:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.color()
            if winning_color[0] == user_bet:
                print(f"You won! The {winning_color[0]} turtle is the winner!")
            else:
                print(
                    f"{user_bet.title()} lost! The {winning_color[0]} turtle is the winner!"
                )
            user_bet = False

screen.exitonclick()
