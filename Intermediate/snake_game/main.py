import time
import turtle as t
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍🐍 My Snake Game 🐍🐍")
screen.tracer(0)

snek = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

scoreboard.get_highscore()
scoreboard.update_score()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

    # Detect collision with food.
    if snek.head.distance(food) < 14:
        food.refresh()
        snek.extend()
        scoreboard.score += 100
        scoreboard.update_score()

    # Detect collision with wall
    if snek.head.xcor() >= 300 or snek.head.xcor() <= -300 or snek.head.ycor() >= 300 or snek.head.ycor() <= -300:
        scoreboard.game_over()
        scoreboard.update_highscore()
        game_is_on = False

    # Detect collision with tail
    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 10:
            scoreboard.game_over()
            scoreboard.update_highscore()
            game_is_on = False

screen.exitonclick()
