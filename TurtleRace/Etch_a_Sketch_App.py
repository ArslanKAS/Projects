import random
import turtle

sid = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
toggle_n = 0


def colors():
    random_colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return random_colors


def forward():
    sid.forward(20)


def turn_left():
    sid.left(10)


def turn_right():
    sid.right(10)


def dot():
    sid.dot(20, colors())


def backwards():
    sid.backward(20)


def clear():
    sid.clear()


def reset():
    screen.reset()


def toggle():
    global toggle_n
    if toggle_n % 2 == 0:
        sid.penup()
    else:
        sid.pendown()
    toggle_n += 1


def circle():
    sid.circle(80)


screen.listen()
screen.onkey(key="Up", fun=forward)
screen.onkey(key="Down", fun=backwards)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="d", fun=dot)
screen.onkey(key="c", fun=clear)
screen.onkey(key="r", fun=reset)
screen.onkey(key="space", fun=toggle)
screen.onkey(key="q", fun=circle)
sid.speed("fastest")
screen.exitonclick()
