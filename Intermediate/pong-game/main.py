import time
import turtle as t
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = t.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("🏓 Pong Game 🏓")
screen.setup(width=800, height=600)

ball = Ball()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
right_scoreboard = Scoreboard((150, 270))
left_scoreboard = Scoreboard((-150, 270))

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when ball misses right paddle
    if ball.xcor() > 400:
        ball.reset_position()
        left_scoreboard.score += 1
        left_scoreboard.update_score()

    # Detect when ball misses left paddle
    if ball.xcor() < -400:
        ball.reset_position()
        right_scoreboard.score += 1
        right_scoreboard.update_score()

screen.exitonclick()
