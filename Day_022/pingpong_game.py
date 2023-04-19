# 양쪽 바 , 가운데 선
# 점수판
# 공 


from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pingpong Game")
screen.tracer(0)

# Paddle
R_Paddle = Paddle(350, 0)
L_Paddle = Paddle(-350, 0)

# Ball
ball = Ball()

# scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(R_Paddle.go_up, "Up")
screen.onkey(R_Paddle.go_down, "Down")
screen.onkey(L_Paddle.go_up, "w")
screen.onkey(L_Paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() >280 or ball.ycor() <- 280 :
        ball.bounce()
    
    if ball.distance(R_Paddle) <50 and ball.xcor() > 320 or ball.distance(L_Paddle) <50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.L_point()

    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.R_point()






screen.exitonclick()