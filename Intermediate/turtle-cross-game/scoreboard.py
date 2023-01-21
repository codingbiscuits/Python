from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 270)
        self.write(arg=f"Level: {self.level}",
                   font=("Courier", 20), align="center")

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}",
                   font=("Courier", 20), align="center")

    def write_you_win(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Congrats! You win!",
                   font=("Courier", 40), align="center")

    def write_game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.",
                   font=("Courier", 40), align="center")
