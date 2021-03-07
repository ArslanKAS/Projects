from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Futura Hv BT", 25, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,move=False, align="center", font=FONT)
        self.goto(100,200)
        self.write(self.r_score,move=False, align="center", font=FONT)

    def r_point(self):
        print('Before Right',self.r_score)
        self.r_score += 1
        print('After Right',self.r_score)
        self.update()

    def l_point(self):
        print(self.l_score)
        self.l_score += 1
        self.update()
