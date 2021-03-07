from turtle import Screen
from turtle import Turtle
import turtle as t
import random

sid = Turtle()
sid.shape('turtle')
sid.color('purple4')
walk_angles = [0, 90, 180, 270]

t.colormode(255)


def random_walks(loop, size):
    sid.pensize(size)
    for _ in range(loop):
        sid.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        sid.forward(30)
        sid.setheading(random.choice(walk_angles))


sid.speed('fastest')
random_walks(500, 8)
screen = Screen()
screen.exitonclick()