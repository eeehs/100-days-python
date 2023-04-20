import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player
player = Player()

# move
screen.listen()
screen.onkey(player.move, "Up")

# cars
carmanager = CarManager()
count = 0

# Scoreboard
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    # 차 생성
    count += 1
    if count == 6:
        carmanager.create_cars()
        count = 0
    carmanager.move()
    # 차 충돌 
    for i in carmanager.all_cars:
        if player.distance(i) < 25:
            game_is_on = False
    # 게임 통과
    if player.ycor() > 280:
        player.start()
        carmanager.speed_up()
        scoreboard.level_up()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
