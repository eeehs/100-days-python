from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self , position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(),self.new_y)
    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(),self.new_y)
    






