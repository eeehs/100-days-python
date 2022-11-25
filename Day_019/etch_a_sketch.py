from turtle import Turtle , Screen , TurtleScreen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counterClockwise():
    tim.left(20)

def move_Clockwise():
    tim.right(20)   

def clear():
    tim.clear()


screen.listen()

screen.onkey(key="w", fun= move_forwards)
screen.onkey(key="s", fun= move_backward)
screen.onkey(key="a", fun= move_counterClockwise)
screen.onkey(key="d", fun= move_Clockwise)
screen.onkey(key="c", fun= clear)

screen.exitonclick()