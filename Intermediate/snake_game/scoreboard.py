import turtle as t


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.speed("fastest")
        self.write(f"Score: {self.score} High Score: {self.highscore}", font=(
            "Courier", 20), align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", font=(
            "Courier", 30), align="center")

    def update_score(self):
        # self.undo() this also works instead of self.clear()
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", font=(
            "Courier", 20), align="center")

    def get_highscore(self):
        with open("highscore.txt") as f:
            highscore = int(f.read())
        self.highscore += highscore

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore.txt", "w+") as wf:
            wf.write(str(self.highscore))
