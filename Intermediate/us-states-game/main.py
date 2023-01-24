import pandas
import turtle as t

IMAGE = "blank_states_img.gif"

screen = t.Screen()
screen.addshape(IMAGE)
screen.title("U.S. States Quiz")

bg_image = t.Turtle(IMAGE)

screen.exitonclick()
