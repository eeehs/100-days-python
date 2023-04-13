from turtle import Turtle, Screen

soo = Turtle()
soo.shape("turtle")


degree = 360
draw = 3 

while True:
    for i in range(draw):
        soo.forward(100)
        soo.right(degree/draw)
    draw +=1
    if draw > 10:
        break


screen = Screen()
screen.exitonclick()