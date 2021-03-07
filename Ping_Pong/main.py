from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgpic("BG.png")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
ball = Ball()
scoreboard = ScoreBoard()
# Right Paddle Movements
# UP
screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeyrelease(key='Up', fun=r_paddle.up)
# DOWN
screen.onkeypress(key='Down', fun=r_paddle.down)
screen.onkeyrelease(key='Down', fun=r_paddle.down)
# Left Paddle Movements
# W ( UP )
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeyrelease(key='w', fun=l_paddle.up)
# S ( DOWN )
screen.onkeypress(key='s', fun=l_paddle.down)
screen.onkeyrelease(key='s', fun=l_paddle.down)

game_is_on = True
while game_is_on:
    ball.move()
    ball.wall_collision()
    ball.paddle_collision(r_paddle)
    ball.paddle_collision(l_paddle)
    if ball.xcor() > 390:
        ball.reset_game()
        scoreboard.l_point()
    if ball.xcor() < - 390:
        ball.reset_game()
        scoreboard.r_point()

    time.sleep(ball.increase_ball_speed)
    screen.update()

screen.exitonclick()
