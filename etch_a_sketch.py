from turtle import *

turtle = Turtle()
screen = Screen()
turtle.shape("turtle")


def move_forward():
    turtle.forward(20)


def move_backwards():
    turtle.backward(20)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def reset():
    turtle.reset()


screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backwards, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(reset, "c")

screen.listen()
screen.exitonclick()
