import turtle as t
from player import Player


irby = Player()
screen = t.Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.onkeypress(irby.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
