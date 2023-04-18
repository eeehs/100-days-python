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
from food import Food
from scoreboard import Scoreboard
import time
# Screen Setting

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    
    # Detect clooision with food
    if snake.snake_turtle[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect clooision with wall
    if snake.snake_turtle[0].xcor() >280 or snake.snake_turtle[0].xcor() < - 280 or snake.snake_turtle[0].ycor() >280 or snake.snake_turtle[0].ycor() < -280:
        game_is_on = False
        scoreboard.gameover()
    # Detect collisioin with tail
    for segment in snake.snake_turtle[1:]:
        if snake.snake_turtle[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()
        









screen.exitonclick()