import turtle
import pandas

screen = turtle.Screen()
screen.title('USA State Guesser Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()


guessed_states = []

def states_to_learn():
    not_guessed_states = []
    for state in all_states:
        if state not in guessed_states:
            not_guessed_states.append(state)
    df = pandas.DataFrame({"Not guessed" : not_guessed_states})
    df.to_csv('Not_guessed.csv')


while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?: ").title()

    if answer_state == "Exit":
        states_to_learn()
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
            guessed_states.append(answer_state)


