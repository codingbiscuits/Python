import time
import turtle as t
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

irby = Player()

screen = t.Screen()
screen.setup(width=600, height=600)

screen.listen()
screen.tracer(0)
screen.onkeypress(irby.move, "Up")

cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars.all_cars:
        if irby.distance(car) < 20:
            game_is_on = False
            scoreboard.write_game_over()

    if irby.ycor() > irby.finish_line:
        scoreboard.level += 1
        irby.refresh()
        scoreboard.update_level()
        cars.update_car_level()
        if scoreboard.level > 10:
            game_is_on = False
            scoreboard.write_you_win()

    if len(cars.all_cars) < cars.total_cars:
        cars.create_cars()

    cars.move_cars()
    cars.update_cars()

screen.exitonclick()
