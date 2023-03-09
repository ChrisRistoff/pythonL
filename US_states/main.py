import pandas
from turtle import Turtle, Screen
from get_coor import *

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
Turtle().shape(image)

guessed_states = []


while True:
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?"
    ).title()
    if answer_state == "Exit":
        missed_states = pandas.DataFrame(states)
        missed_states.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        print("Correct")
        mark_state(answer_state)
        guessed_states = states.pop(states.index(answer_state))

print(states)
