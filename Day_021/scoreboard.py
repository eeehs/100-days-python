from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(f"Score: {self.score}",align="center",font=('Arial', 12, 'normal'))
        self.hideturtle()
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=('Arial', 12 ,'normal'))
    
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game over",align="center",font=('Arial', 24, 'normal'))