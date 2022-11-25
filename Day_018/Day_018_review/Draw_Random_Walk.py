from turtle import Turtle , Screen
import random
tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.shape("turtle")


# 선을 두껍게
tim.pensize(10)

# 빠르게 그릴 수 있게
tim.speed(10)

while True:
    tim.color(random.choice(colors))
    tim.forward(random.choice([-50,50]))
    tim.right(random.choice([-90,90]))


screen = Screen()
screen.screensize(5000,3500)
screen.exitonclick()