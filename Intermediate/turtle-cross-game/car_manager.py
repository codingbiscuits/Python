import random
from turtle import Turtle

MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.total_cars = 15

    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)
        random_x = random.randint(300, 900)
        random_y = random.randint(-250, 250)
        new_car.goto(random_x, random_y)
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def update_cars(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                self.all_cars.remove(car)
