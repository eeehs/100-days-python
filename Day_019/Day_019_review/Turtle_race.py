from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
turtles = ["a","b","c","d","e","f"]
turtle_color = random.choice(colors)

x = -200
y = -100

for i in range(6):
    turtles[i] = Turtle(shape="turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x,y)
    y = y + 40

race = True
while race:
    for turtle in turtles:
        move_x = random.randint(0, 10)
        turtle.forward(move_x)
        if turtle.xcor() > 210:
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"you win!! winner: {winner}")
            else:
                print(f"you lose winner: {winner}")
            
            
    




screen.exitonclick()