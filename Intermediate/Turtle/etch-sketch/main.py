import turtle as t

t.register_shape('deku.gif')

bri = t.Turtle()
screen = t.Screen()


def move_forward():
    bri.forward(10)


def move_backward():
    bri.back(10)


def turn_right():
    bri.right(15)


def turn_left():
    bri.left(15)


def clear_screen():
    bri.clear()
    bri.penup()
    bri.home()
    bri.pendown()
    bri.left(90)


bri.shape('deku.gif')
bri.left(90)
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
