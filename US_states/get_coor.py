import pandas
from turtle import *

data = pandas.read_csv("50_states.csv")


data_dict = data.to_dict()
states = data.state.to_list()


def y_coor(state):
    index = states.index(state.title())
    return data_dict["y"][index]


def x_coor(state):
    index = states.index(state.title())
    return data_dict["x"][index]


def mark_state(state):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x_coor(state), y_coor(state))
    t.write(state)


def get_mouse_click_coor(x, y):
    print(x, y)
