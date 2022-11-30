from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.high_score_road()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_save()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def high_score_road(self):
        with open("C:\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_024\\data.txt") as f:
            self.content = f.read()
            return int(self.content)
    def high_score_save(self):
        with open("C:\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_024\\data.txt",mode="w") as f:
            self.score = str(self.score)
            f.write(self.score)