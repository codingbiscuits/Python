import turtle as t

screen = t.Screen()
screen.bgpic("nemesis.gif")
screen.textinput(title="Nemesis Board Game",
                 prompt="It is the Action Phase. It is the First players turn. Please select an Action.")

screen.exitonclick()
