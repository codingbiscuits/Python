import random
import turtle as t

is_race_on = False

deku = t.Turtle()
luffy = t.Turtle()
naruto = t.Turtle()
bri = t.Turtle()
sabrina = t.Turtle()

screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which hero will win the race? (Deku, Luffy, Naruto, Bri, Sabrina)")


t.register_shape('Deku.gif')
t.register_shape('Luffy.gif')
t.register_shape('Naruto.gif')
t.register_shape('Bri.gif')
t.register_shape('Sabrina.gif')

deku.shape('Deku.gif')
deku.penup()
deku.goto(-220, 0)

luffy.shape('Luffy.gif')
luffy.penup()
luffy.goto(-220, 50)

naruto.shape('Naruto.gif')
naruto.penup()
naruto.goto(-230, 100)

bri.shape('Bri.gif')
bri.penup()
bri.goto(-230, -50)

sabrina.shape('Sabrina.gif')
sabrina.penup()
sabrina.goto(-230, -100)

heroes = []
heroes.append(deku)
heroes.append(luffy)
heroes.append(naruto)
heroes.append(bri)
heroes.append(sabrina)

if user_bet:
    is_race_on = True

while is_race_on:
    for hero in heroes:
        rand_distance = random.randint(0, 10)
        hero.forward(rand_distance)

        # if hero.shape()[:-4].lower() == "bri":
        #     hero.forward(5)

        if hero.xcor() > 230:
            print(f"Winner is: {hero.shape()[:-4]}")
            winning_hero = hero.shape()[:-4]
            is_race_on = False


if winning_hero.lower() == user_bet.lower():
    print(f"You win! You guessed {user_bet} 😏")
else:
    print(f"You lose! You guessed {user_bet} 😭")


screen.exitonclick()
