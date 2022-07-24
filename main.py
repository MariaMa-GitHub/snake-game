# SNAKE GAME by Maria
from snake import Snake
from food import Food
from score import Scoreboard
from turtle import Screen
from menu import Menu
import time

# game settings
PROGRAM_NAME = "Snake Game"
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BG_COLOR = "black"
POSITIVE_BORDER = 245
NEGATIVE_BORDER = -245

# game screen
screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.title(PROGRAM_NAME)
screen.bgcolor(BG_COLOR)
screen.tracer(0)

# game objects
snake = Snake()
food = Food(snake.segments)
scoreboard = Scoreboard()
instructions = Menu()

# game controls
screen.listen()
screen.onkeypress(snake.pause, "space")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


# game program
def program():

    # update game
    screen.update()
    time.sleep(0.1)

    # snake movement
    snake.move()

    # food collision
    if snake.head.distance(food) < 15:
        food.refresh(snake.segments)
        snake.extend()
        scoreboard.score += 1
        scoreboard.update()

    # wall collision
    if snake.head.xcor() > POSITIVE_BORDER or snake.head.xcor() < NEGATIVE_BORDER or snake.head.ycor() > POSITIVE_BORDER or snake.head.ycor() < NEGATIVE_BORDER:
        scoreboard.restart()
        snake.restart()

    # snake collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.restart()
            snake.restart()

    # display menu
    instructions.display(snake.action)

    # run game
    screen.ontimer(program)


# game loop
program()
screen.mainloop()
