COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1,2)
        new_car.color(random.choice(COLORS))
        new_car.goto(x=300,y=random.randint(-280, 280))
        new_car.setheading(180)
        self.all_cars.append(new_car)
        
    def move(self):
        for i in self.all_cars:
            i.forward(STARTING_MOVE_DISTANCE)    
    def speed_up(self):
        global STARTING_MOVE_DISTANCE, MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

        