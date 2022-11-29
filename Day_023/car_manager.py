from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:
    def __init__(self):
        self.car = []
        self.new_car()
        self.STARTING_MOVE_DISTANCE = 5
        self.MOVE_INCREMENT = 10
    def new_car(self):
        color = random.choice(COLORS)
        x_cor = 300
        y_cor = random.choice(range(-250,280))
        new = Turtle("square")
        new.turtlesize(stretch_wid=1,stretch_len=2)
        new.color(color)
        new.penup()
        new.setheading(180)
        new.goto(x_cor,y_cor)
        self.car.append(new)
    def car_move(self):
        for i in self.car:
            i.forward(self.STARTING_MOVE_DISTANCE)
        time.sleep(0.1)
    def car_fast(self):
        self.STARTING_MOVE_DISTANCE+=self.MOVE_INCREMENT

            