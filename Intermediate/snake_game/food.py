import random
import turtle as t

t.register_shape('grape.gif')


class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("grape.gif")
        self.penup()
        self.color("purple")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(new_x, new_y)
