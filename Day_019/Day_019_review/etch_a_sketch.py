from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_back():
    tim.back(10)
def Counter_Clockwise():
    tim.right(-10)
def Clockwise():
    tim.right(10)
def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=Counter_Clockwise)
screen.onkey(key="d", fun=Clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()