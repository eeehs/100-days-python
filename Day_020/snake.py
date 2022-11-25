from turtle import Turtle

class Snake:   
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            i = Turtle(shape="square")
            i.color("white")
            i.penup()
            i.goto(x,y)
            x -=20
            self.snakes.append(i)
    def move(self):
        for m in range(1,len(self.snakes)):
            tur_toward = self.snakes[m-1].pos()
            self.snakes[m].goto(tur_toward)
        self.snakes[0].forward(20) 
    def up(self):
        if self.snakes[0].heading() != 270.0:
            self.snakes[0].setheading(90)
    def down(self):
        if self.snakes[0].heading() != 90.0:
            self.snakes[0].setheading(270)
    def right(self):
        if self.snakes[0].heading() != 180.0:
            self.snakes[0].setheading(0)
    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)