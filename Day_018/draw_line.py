from turtle import Turtle , Screen



tt = Turtle()

tt.shape("turtle")

tt.color("blue")

# 1. 점선그리기 
for _ in range(10):
    tt.forward(10)
    tt.penup()
    tt.forward(10)
    tt.pendown()



screen = Screen()
screen.exitonclick()