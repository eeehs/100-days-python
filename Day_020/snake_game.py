## Step
# 1. create a snake body
# 2. Move the snake
# 3. create snake food
# 4. detect collision with food
# 5. create a scoreboard
# 6. detect collision with wall
# 7. detect collision with tail

# import 
from turtle import Turtle, Screen
from snake import Snake
import time
# Screen Setting

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()


screen.listen()

screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key= "Down")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")


# main
game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

        









screen.exitonclick()