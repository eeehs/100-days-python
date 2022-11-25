from turtle import Turtle
snake_position = [(0,0),(-20,0),(-40,0)]

class Snake:   
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for i in snake_position:
            new = Turtle("square")
            new.color("white")
            new.penup()
            new.goto(i)
            self.snakes.append(new)

    def extend(self):
        new_pos = self.snakes[-1].position()
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(new_pos)
        self.snakes.append(new_snake)    

    def move(self):
        for m in range(len(self.snakes)-1,0,-1):
            tur_toward_x = self.snakes[m-1].xcor()
            tur_toward_y = self.snakes[m-1].ycor()
            self.snakes[m].goto(tur_toward_x,tur_toward_y)
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

        
        
        
        
        