import time
import turtle as t
from snake import Snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍🐍 My Snake Game 🐍🐍")
screen.tracer(0)

snek = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snek.move()


screen.exitonclick()
