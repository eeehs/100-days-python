import turtle
import random
tim = turtle.Turtle()

tim.shape("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tim.pencolor(r,g,b)

# 선을 두껍게
tim.pensize(10)

# 빠르게 그릴 수 있게
tim.speed(10)

while True:
    random_color()
    tim.forward(random.choice([-50,50]))
    tim.right(random.choice([-90,90]))


screen = Screen()
screen.screensize(5000,3500)
screen.exitonclick()