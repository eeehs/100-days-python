import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S, States Game")
image = "./Day_025/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./Day_025/us-states-game/50_states.csv")
all_state = data.state.to_list()
guessed_states = []


print(data[data.state == "Alabama"]["y"])


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50Guess the State", prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./Day_025/us-states-game/states_to_learn.csv")
        break
    if answer_state in all_state:
        all_state.remove(answer_state)
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


