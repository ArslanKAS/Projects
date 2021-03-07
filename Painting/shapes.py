from turtle import Screen
from turtle import Turtle
import random
from colors import colors

sid = Turtle()
sid.shape('turtle')
sid.color('purple4')

for sides in range(3,11):
    angle = 360/sides
    sid.pencolor(random.choice(colors))
    print(angle, sides)
    for shape in range(sides):
        sid.forward(100)
        sid.right(angle)
# sid.pencolor(random.choice(colors))
# for _ in range(3):
#     sid.forward(100)
#     sid.right(120)
#
# sid.pencolor(random.choice(colors))
# for _ in range(4):
#     sid.forward(100)
#     sid.right(90)
# sid.pencolor(random.choice(colors))
# for _ in range(5):
#     sid.forward(100)
#     sid.right(72)
# sid.pencolor(random.choice(colors))
# for _ in range(6):
#     sid.forward(100)
#     sid.right(60)
# sid.pencolor(random.choice(colors))
# for _ in range(7):
#     sid.forward(100)
#     sid.right(51.4)
# sid.pencolor(random.choice(colors))
# for _ in range(8):
#     sid.forward(100)
#     sid.right(45)
# sid.pencolor(random.choice(colors))
# for _ in range(9):
#     sid.forward(100)
#     sid.right(40)

screen = Screen()
screen.exitonclick()
