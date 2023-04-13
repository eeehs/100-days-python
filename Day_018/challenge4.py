from turtle import Turtle, Screen
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
soo = Turtle()
soo.shape("square")
degree = [90,180,270,360]
soo.speed(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random


while True:

    soo.pencolor(random.choice(colours))
    soodegree = random.choice(degree)
    soo.pensize(10)
    soo.right(soodegree)
    soo.forward(20)


screen = Screen()
screen.exitonclick()