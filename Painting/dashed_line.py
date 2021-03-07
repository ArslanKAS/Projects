from turtle import Screen
from turtle import Turtle

sid = Turtle()
sid.shape('turtle')
sid.color('purple4')

for x in range(4):

    for _ in range(20):
        sid.forward(5)
        sid.penup()
        sid.forward(5)
        sid.pendown()

    sid.right(90)


screen = Screen()
screen.exitonclick()
