from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(4, 1)
        self.goto(x, y)
        self.shapetransform()
        self.speed('fastest')

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
