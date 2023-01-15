import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

head = t.Turtle()
head.shape("square")
head.color("white")

body = t.Turtle()
body.shape("square")
body.color("white")
body.setposition(-20, 0)

tail = t.Turtle()
tail.shape("square")
tail.color("white")
tail.setposition(-40, 0)

screen.exitonclick()
