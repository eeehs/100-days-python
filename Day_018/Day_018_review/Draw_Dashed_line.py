from turtle import Turtle , Screen



tt = Turtle()

tt.shape("turtle")

tt.color("blue")

for _ in range(10):
    tt.forward(10)
    tt.penup()
    tt.forward(10)
    tt.pendown()

screen = Screen()
screen.exitonclick()









