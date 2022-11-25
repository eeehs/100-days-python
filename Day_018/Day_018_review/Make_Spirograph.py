from turtle import Turtle , Screen
import random
tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.shape("turtle")
tim.speed("fastest")

n = 5
while n < 360:
    tim.setheading(n)
    tim.color(random.choice(colors))
    tim.circle(150)
    n += 5

screen = Screen()
screen.exitonclick()