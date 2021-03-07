from turtle import Turtle

SNAKE_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION = {'right': 0, 'up': 90, 'left': 180, 'down': 270}


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for pos in SNAKE_POS:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.speed(10)
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("olive drab")
        self.segments.append(new_segment)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION['down']:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != DIRECTION['up']:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != DIRECTION['left']:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != DIRECTION['right']:
            self.head.setheading(180)
