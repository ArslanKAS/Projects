from turtle import Turtle
from random import randint, choice

COLORS = ['blue violet', 'purple', 'dark magenta', 'indigo']


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("turtle")
        self.penup()
        self.speed("fastest")
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.refresh()
    #
    # def big_food(self):
    #     self.shapesize(stretch_wid=1, stretch_len=1)
    #     self.color("red")

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(x=random_x, y=random_y)
        self.color(choice(COLORS))
