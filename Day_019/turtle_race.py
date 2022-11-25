from turtle import Turtle , Screen , TurtleScreen
import random


screen = Screen()

in_race_on = True
screen.setup(500, 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100,-70,-40,-10,20,50]
print(user_bet)
all_turtle = []

for turtle_index in range(0, 6):
    A = Turtle(shape= "turtle")
    A.color(colors[turtle_index])
    A.penup()
    A.goto(x = -230, y = y_position[turtle_index] )
    all_turtle.append(A)

while in_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            in_race_on =  False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# A = Turtle()
# B = Turtle()
# C = Turtle()
# A.penup()
# A.goto(x= -230 , y = -100)


screen.exitonclick()