from turtle import Turtle, Screen

soo = Turtle()
soo.shape("turtle")



for i in range(10):
    soo.forward(10)
    soo.penup()
    soo.forward(10)
    soo.pendown()


screen = Screen()
screen.exitonclick()