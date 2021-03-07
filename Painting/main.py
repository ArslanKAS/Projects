from turtle import Screen
from turtle import Turtle
import colorgram as cg
import random
import turtle as t

t.colormode(255)
sid = Turtle()
sid.shape('turtle')
image_colors = cg.extract("hirst_spot_painting.jpg", 12)
print(image_colors[0].rgb.r)

colors_list = []
for color in image_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors = (r, g, b)
    colors_list.append(colors)


sid.hideturtle()
sid.penup()
sid.setheading(225)
sid.forward(400)
sid.setheading(0)


def draw_ten():
    for _ in range(9):
        sid.dot(30, random.choice(colors_list))
        sid.forward(60)
        sid.dot(30, random.choice(colors_list))


def turn_left():
    sid.setheading(90)
    sid.forward(60)
    sid.setheading(180)


def turn_right():
    sid.setheading(90)
    sid.forward(60)
    sid.setheading(0)


def draw_loop():
    for draw in range(5):
        draw_ten()
        turn_left()
        draw_ten()
        turn_right()


draw_loop()
sid.speed(1)
screen = Screen()
screen.exitonclick()
