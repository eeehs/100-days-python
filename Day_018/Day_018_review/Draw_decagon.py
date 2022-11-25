from turtle import Turtle , Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")


n = 3
while n < 11:
    for i in range(n):
        tim.right(360/n)
        tim.forward(100)
    n = n + 1
    

screen = Screen()
screen.exitonclick()