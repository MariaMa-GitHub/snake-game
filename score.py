# Game Score
from turtle import Turtle

# score settings
MOVE = False
ALIGN = "center"
FONT = {"score": ("Courier", 20, "bold"), "game": ("Arial", 48, "bold")}


# scoreboard class
class Scoreboard(Turtle):

    # initialize settings
    def __init__(self):

        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 205)

        try:
            with open("data.txt") as file:
                self.best = int(file.read())
        except:
            self.best = 0

        self.score = 0
        self.update()

    # update score
    def update(self):

        self.clear()
        self.write(f"Score: {self.score}   Best: {self.best}", MOVE, ALIGN, FONT["score"])

    # reset score
    def restart(self):

        if self.score > self.best:
            self.best = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.best}")

        self.score = 0
        self.update()
