from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-200,200)
        self.write(f"level = {self.level}", align="center" , font = FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        
        self.write("Game Over", align="center" , font = FONT)

