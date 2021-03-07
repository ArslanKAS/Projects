from turtle import Screen
from turtle import Turtle
import turtle as t
import random

sid = Turtle()
sid.shape('turtle')
sid.color('purple4')
walk_angles = [0, 90, 180, 270]

t.colormode(255)

for iteration in range(5,360,5):
    sid.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    sid.circle(100)
    sid.setheading(iteration)

sid.speed(1)
screen = Screen()
screen.exitonclick()