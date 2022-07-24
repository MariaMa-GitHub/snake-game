# Game Food
from turtle import Turtle
from random import randrange


# food class
class Food(Turtle):

    # initialize settings
    def __init__(self, snake):

        super().__init__()

        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)

        self.refresh(snake)

    # reset food
    def refresh(self, snake):

        for segment in snake:
            while segment.distance(self) < 10:
                x = randrange(-240, 240, 20)
                y = randrange(-240, 240, 20)
                self.goto(x, y)
