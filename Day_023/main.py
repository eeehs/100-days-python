import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.onkey(turtle.up, "w")


game_is_on = True
i = 0
while game_is_on:
    screen.update()
    # 게임 시작
    car.car_move()
    # 자동차 일정 시간 뒤 생성
    i +=1
    if i == 6:
        i = 0
        car.new_car()
    # 자동차 충돌 감지
    for dis in car.car:
        if dis.distance(turtle) <20:
            game_is_on =False
            scoreboard.game_over()
    # 거북이가 도착지에 닿았을 때
    if turtle.ycor() == 300:
        turtle.goto(0, -280)
        scoreboard.level_up()
        car.car_fast()



screen.exitonclick()