from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

food = Food()
snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgpic('bg.png')
screen.register_shape("head.gif")
snake.head.shape("head.gif")
screen.tracer(0)
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
scoreboard = ScoreBoard()

game_is_on = True

while game_is_on:

    snake.move()
    if snake.head.distance(food) < 20:
        # if scoreboard.score == 5 or scoreboard == 10 or scoreboard == 15 or scoreboard == 20:
        #     food.big_food()
        #     scoreboard.score += 5
        food.refresh()
        snake.extend_segment()
        scoreboard.update_score()
        scoreboard.scores()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.game_over()
            game_is_on = False

    time.sleep(0.08)
    screen.update()

screen.exitonclick()
