# Game Snake
from turtle import Turtle

# snake settings
ORIGIN = [(20, 0), (0, 0), (-20, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# snake class
class Snake:

    # initialize settings
    def __init__(self):

        self.segments = []
        self.create()
        self.head = self.segments[0]

        self.action = False

    # create snake
    def create(self):

        for position in ORIGIN:
            self.grow(position)

    # grow segment
    def grow(self, pos):

        segment = Turtle("square")

        segment.penup()
        segment.color("white")
        segment.goto(pos)

        self.segments.append(segment)

    # extend snake
    def extend(self):

        self.grow(self.segments[-1].pos())

    # move snake
    def move(self):

        if self.action:
            for i in range(len(self.segments) - 1, 0, -1):
                x = self.segments[i - 1].xcor()
                y = self.segments[i - 1].ycor()
                if i != 0:
                    self.segments[i].goto((x, y))
            self.head.forward(DISTANCE)

    # move up
    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # move down
    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # move left
    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # move right
    def right(self):

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # reset snake
    def restart(self):

        for segment in self.segments:
            segment.goto(600, 600)

        self.segments.clear()
        self.pause()
        self.create()
        self.head = self.segments[0]

    # pause snake
    def pause(self):

        self.action = False if self.action else True
