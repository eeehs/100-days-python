from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.snakes[0].distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -280 or snake.snakes[0].ycor() > 280 or snake.snakes[0].ycor() < -280:
        game_is_on = False 
        scoreboard.game_over()
        
    # Detect collision with tail
    for q in snake.snakes[1:]:
        if snake.snakes[0].distance(q) <10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()