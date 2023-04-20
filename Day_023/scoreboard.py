FONT = ("Courier", 24, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level =1
        self.hideturtle()
        self.penup()
        self.goto(-200,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)
    
    def level_up(self):
        self.level +=1
        self.update_scoreboard()
