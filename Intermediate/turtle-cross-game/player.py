from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 300
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.finish_line = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)
