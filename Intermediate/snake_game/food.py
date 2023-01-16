import random
import turtle as t


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
