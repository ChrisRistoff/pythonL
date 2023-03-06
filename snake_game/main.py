from turtle import *
import random

pts = 0
level = 0
sped = 20
lev = 1
start_pos = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]
snake_body = []

snake = Turtle("square")
snake.color("white")
snake.penup()
snake.goto(start_pos[0])

for position in start_pos:
    snake_bod = Turtle("square")
    snake_bod.color("white")
    snake_bod.penup()
    snake_bod.goto(position)
    snake_body.append(snake_bod)


food = Turtle()
food.shape("circle")
food.color("black")
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))


def move_up():
    snake.setheading(90)


def move_down():
    snake.setheading(270)


def move_left():
    snake.setheading(180)


def move_right():
    snake.setheading(0)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("red")

screen.onkey(fun=move_up, key="Up")
screen.onkey(fun=move_down, key="Down")
screen.onkey(fun=move_left, key="Left")
screen.onkey(fun=move_right, key="Right")
screen.listen()

while True:
    snake.speed(0)
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].goto(snake_body[i - 1].pos())
    snake_body[0].goto(snake.pos())
    snake.forward(20)

    if snake.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        snake_bod = Turtle("square")
        snake_bod.color("white")
        snake_bod.penup()
        snake_body.append(snake_bod)
        pts += 1
        level += 1
        if level == 5:
            lev += 1
            level = 0
        clear()
        write(f"Score: {pts} Level: {lev}", align="left", font=("Arial", 24, "normal"))
    for i in snake_body:
        if snake.distance(i) < 10:
            write(f"Game Over", align="center", font=("Arial", 24, "normal"))
            screen.exitonclick()
