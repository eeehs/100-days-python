from turtle import Turtle

class Snake:

    def __init__(self):
        l_x = 0
        l_y = 0
        self.snake_turtle = []
        for snake in range(3):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(x= l_x ,y= l_y)
            l_x -=20
            self.snake_turtle.append(snake)
    
    def extend(self):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(self.snake_turtle[-1].position())
        self.snake_turtle.append(snake)

    def move(self):
        step = -1
        for i in range(len(self.snake_turtle)-1):
            new_x = self.snake_turtle[step-1].xcor()
            new_y = self.snake_turtle[step-1].ycor()
            self.snake_turtle[step].goto(new_x,new_y)
            step -=1
        self.snake_turtle[0].forward(20)
    
    def up(self):
        if self.snake_turtle[0].heading() != 270:
            self.snake_turtle[0].setheading(90)
    def down(self):
        if self.snake_turtle[0].heading() != 90:
            self.snake_turtle[0].setheading(270)
    def left(self):
        if self.snake_turtle[0].heading() != 0:
            self.snake_turtle[0].setheading(180)
    def right(self):
        if self.snake_turtle[0].heading() != 180:
            self.snake_turtle[0].setheading(0)