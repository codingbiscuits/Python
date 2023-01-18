import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-40, 280)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.write(f"Score: {self.score}", font=("Courier", 20, "bold"))

    def update_score(self):
        self.undo()
        self.write(f"Score: {self.score}", font=("Courier", 20, "bold"))
