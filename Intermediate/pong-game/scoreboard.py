from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.write(arg=f"{self.score}",
                   font=("Courier", 20), align="center")

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score}",
                       font=("Courier", 20), align="center")
