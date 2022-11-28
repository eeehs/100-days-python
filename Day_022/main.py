from turtle import Turtle ,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 화면 설정 적용
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)

R_paddle = Paddle((350,0))
L_paddle = Paddle((-350,0))
ball = Ball()
screen.listen()
screen.onkey(R_paddle.go_up, "Up")
screen.onkey(R_paddle.go_down, "Down")
screen.onkey(L_paddle.go_up, "w")
screen.onkey(L_paddle.go_down, "s")
screen.onkey(ball.reset,"space")
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #  공이 위 아래 벽에 닿았을 때 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # 공에 R_paddle 에 닿았을 때  
    if ball.distance(R_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    # 공에 L_paddle 에 닿았을 때
    if ball.distance(L_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # 공이 오른쪽 바깥으로 나갔을 때 
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()
    # 공이 왼쪽 바깥으로 나갔을 때
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset()
        

screen.exitonclick()