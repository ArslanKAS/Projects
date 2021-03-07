from turtle import Turtle, Screen
import random


def forward():
    for distance in participants:
        distance.forward(random.randrange(5, 10, 1))


def win():
    for turtle in participants:
        # print(participants[_].xcor() == 400)
        if turtle.xcor() > 300:
            if turtle.color == bet:
                print(f"{bet}  won. You Win !!!".upper())
            else:
                print(f"{turtle.pencolor()}  won. You Lose !!!".upper())
            global game_continue
            game_continue = False
            return game_continue


screen = Screen()
screen.setup(width=640, height=480)
bet = screen.textinput(title="Turtle Race", prompt="Select a Turtle by Entering Color: black, red, green, blue, cyan, "
                                                   "yellow, magenta")
colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
y_pos = [0, 40, 80, 120, -40, -80, -120]

participants = []
for x in range(len(y_pos)):
    sid = Turtle(shape='turtle')
    sid.color(colors[x])
    sid.penup()
    sid.goto(x=-300, y=y_pos[x])
    participants.append(sid)

game_continue = True
while game_continue:
    forward()
    win()
    # if sid.position() == 0:
    #     print("Game Over")

screen.exitonclick()
