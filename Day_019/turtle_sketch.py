from turtle import Turtle,Screen

soo = Turtle()

screen = Screen()

## 함수
def forward():
    soo.forward(10)
def backward():
    soo.backward(10)
def right():
    soo.right(10)
def left():
    soo.left(10)
def clear():
    soo.reset()


screen.listen()

screen.onkey(fun= forward, key="w")
screen.onkey(fun= backward, key= "s")
screen.onkey(fun= right, key="a")
screen.onkey(fun= left, key="d")
screen.onkey(fun= clear, key="c")


screen.exitonclick()