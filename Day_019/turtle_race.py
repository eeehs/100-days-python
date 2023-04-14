from turtle import Turtle,Screen
import random




# Screen setting
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Create turtle

colors = ["red","orange","yellow","green","blue","purple"]
turtles =[]
color = 0
lo_x = -230
lo_y = -100
for i in colors:
    i = Turtle(shape="turtle")
    i.color(colors[color])
    i.penup()
    i.goto(x=lo_x,y=lo_y)
    turtles.append(i)    
    lo_y += 50
    color +=1

# Race Setting
is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won! The {winning_color} turtle is the winner")
            else:
                print(f"you've lost! The {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()