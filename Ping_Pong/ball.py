from turtle import Turtle
from random import randrange

RANDOM = [randrange(2, 3), randrange(2, 3)]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(1.5, 1.5)
        self.color("green")
        self.goto(0, 0)
        self.penup()
        self.x_speed = RANDOM[0]
        self.y_speed = RANDOM[1]
        self.increase_ball_speed = 0.01

    def move(self):
        x_new = self.xcor() + self.x_speed
        y_new = self.ycor() + self.y_speed
        self.goto(x_new, y_new)

    def wall_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.y_speed *= -1

    def paddle_collision(self, paddle):
        if self.distance(paddle) < 40 and (self.xcor() > 350 or self.xcor() < -350):
            self.increase_ball_speed += 0.000000009
            self.x_speed *= -1

    def reset_game(self):
        self.goto(0, 0)
        self.x_speed *= -1
        self.increase_ball_speed = 0.01
