# Game Menu
from turtle import Turtle

# menu settings
MOVE = False
ALIGN = "center"
FONT = {
    "title": ("Arial", 48, "bold"),
    "instructions": ("Arial", 20, "normal")
}


# menu class
class Menu(Turtle):

    # initialize settings
    def __init__(self):

        super().__init__()

        self.penup()
        self.hideturtle()
        self.color("white")

    # display menu
    def display(self, action):

        if action:
            self.clear()
        else:
            try:
                self.goto(0, 50)
                self.write("SNAKE GAME", MOVE, ALIGN, FONT["title"])
                self.goto(0, -100)
                self.write("Press [Enter] to Play", MOVE, ALIGN, FONT["instructions"])
                self.goto(0, -150)
                self.write("Use Arrows to Move", MOVE, ALIGN, FONT["instructions"])
            except:
                pass
