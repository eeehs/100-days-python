import turtle ,csv ,pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = ".\\us-states-game\\blank_states_img.gif"

# 미국 주 데이타 추출
data = pandas.read_csv(".\\us-states-game\\50_states.csv")
state = data["state"].to_list()

screen.addshape(image)
turtle.shape(image)

# 미국 주 위치 추출 

#글로 쓰여질 거북이 생성
write_turtle = turtle.Turtle()
write_turtle.color("black")
write_turtle.hideturtle()
correct_answer = []
while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"Guess the State {len(correct_answer)}/{len(state)}", prompt="What's another state's name?").title()
    if answer_state in state:
        w = turtle.Turtle()
        w.hideturtle()
        w.penup()
        state_data = data[data["state"] == answer_state]
        w.goto(int(state_data.x),int(state_data.y))
        w.write(answer_state)
        correct_answer.append(answer_state)
    elif answer_state == "Exit":
        break

#state to learn

for i in state:
    if i in correct_answer:
        state.remove(i)

data = pandas.DataFrame(state)

data.to_csv(".\\us-states-game\\learn_state.csv")