from turtle import Turtle
from food import Food


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:

            self.highscore = int(data.read())

        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.update()
        self.hideturtle()

        self.high_score()

    def high_score(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("data.txt", "w") as daata:
                daata.write(str(self.highscore))
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center",
                   font=("Arial", 24, "normal"))

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(f"Game Over !Score: {self.score}", align="center",
    #                font=("Arial", 24, "normal"))

    def score_count(self):
        self.score += 1
        self.clear()
        self.update()
