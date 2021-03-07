from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ("Futura Hv BT", 25, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=250)
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("black")
        self.write(f'GAME OVER', move=False, align="center", font=FONT)

    def scores(self):
        self.score += 1
        self.clear()
        self.update_score()
    #
    # def big_food_score(self):
    #     big_food = Food()
    #     if self.score % 5 == 0:
    #         big_food.big_food()
    #         self.score += 5
