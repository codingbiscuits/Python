import pandas
import turtle as t

IMAGE = "blank_states_img.gif"

screen = t.Screen()
screen.title("U.S. States Quiz")
screen.addshape(IMAGE)
t.shape(IMAGE)

correct_states = 0
correct_answers = []
dataframe = pandas.read_csv("50_states.csv")
states = dataframe.state.to_list()

game_is_on = True
while game_is_on:

    if correct_states == 0:
        answer_prompt = screen.textinput(
            title="Guess the State", prompt="What is the name of a U.S. State?").title()
    else:
        answer_prompt = screen.textinput(
            title=f"{correct_states}/50 States Correct", prompt="What is the name of another U.S. State?").title()

    if answer_prompt in states and answer_prompt not in correct_answers:
        correct_states += 1
        state_x = int(dataframe[dataframe.state == answer_prompt].x)
        state_y = int(dataframe[dataframe.state == answer_prompt].y)

        answer = t.Turtle()
        answer.penup()
        answer.hideturtle()
        answer.goto(state_x, state_y)
        answer.write(arg=answer_prompt, font=("Courier", 15), align="center")

        correct_answers.append(answer_prompt)

    if correct_states >= 50:
        answer_prompt = int(screen.textinput(
            title="Winner Winner Chicken Dinner!", prompt="You Guessed All 50 States! Enter 'exit' Exit the Game."))
        game_is_on = False


t.mainloop()
