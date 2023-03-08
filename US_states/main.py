import pandas as pd
from turtle import Turtle, Screen
from get_coor import *

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
Turtle().shape(image)

while True:
    # input
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?"
    ).title()
    if answer_state == "Exit":
        break
    if answer_state in states:
        print("Correct")
        mark_state(answer_state)
