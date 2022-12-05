from turtle import Turtle
from score import Score

DIVIDER_WIDTH = 10


class Scoreboard:

    def __init__(self, screen_height, block_size):
        self.screen_height = screen_height
        self.left = Score("left", screen_height, block_size)
        self.right = Score("right", screen_height, block_size)
        self.divide_court()
        self.winner = ""
        self.set_winner()

    def divide_court(self):
        divider = Turtle("square")
        divider.color("white")
        divider.shapesize(0.5)
        divider.penup()
        divider.setposition(0, self.screen_height / 2 - DIVIDER_WIDTH)
        divider.setheading(270)

        x, y = divider.pos()
        while y > self.screen_height / -2:
            divider.stamp()
            divider.forward(DIVIDER_WIDTH * 3)
            x, y = divider.pos()

        divider.hideturtle()


    def set_winner(self):
        if self.left.score > self.right.score:
            winner = "Player 1"
        else:
            winner = "Player 2"
        self.winner = winner


    def reset(self):
        self.left.score = 0
        self.left.update()
        self.right.score = 0
        self.left.update()
