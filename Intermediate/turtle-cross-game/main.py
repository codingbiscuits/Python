import time
import turtle as t
from player import Player
from car_manager import CarManager

irby = Player()

screen = t.Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.onkeypress(irby.move, "Up")

cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if len(cars.all_cars) < cars.total_cars:
        cars.create_cars()
    cars.move_cars()
    cars.update_cars()

    if irby.ycor() > irby.finish_line:
        print("You win!")

screen.exitonclick()
