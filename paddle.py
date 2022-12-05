from turtle import Turtle

BASE_SIZE = 20
DISTANCE = 20
UP = 90
DOWN = 270


def get_top_corner(side, screen_height, screen_width, paddle_width):
    if side == "left":
        return (-screen_width / 2) + paddle_width, (screen_height / 2)
    elif side == "right":
        return (screen_width / 2) - paddle_width, (screen_height / 2)


def get_bottom_corner(side, screen_height, screen_width, paddle_width):
    if side == "left":
        return (-screen_width / 2) + paddle_width, (-screen_height / 2)
    elif side == "right":
        return (screen_width / 2) - paddle_width, (-screen_height / 2)


class Paddle(Turtle):

    def __init__(self, side, screen_height, screen_width, paddle_height=100, paddle_width = 20):

        super().__init__("square")
        self.color("white")
        self.penup()
        self.paddle_height = paddle_height
        self.paddle_width = paddle_width
        self.shapesize(stretch_wid=paddle_height / BASE_SIZE, stretch_len=paddle_width / BASE_SIZE)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.top_edge = get_top_corner(side, screen_height, screen_width, self.paddle_width)
        self.bottom_edge = get_bottom_corner(side, screen_height, screen_width, self.paddle_width)
        self.move_to_side(side)

    def up(self):
        if self.distance(self.top_edge) <= self.paddle_height / 2:
            return

        self.sety(self.ycor() + DISTANCE)

    def down(self):
        if self.distance(self.bottom_edge) <= self.paddle_height / 2:
            return

        self.sety(self.ycor() - DISTANCE)

    def move_to_side(self, side):
        if side == "left":
            offset = -(self.screen_width / 2) + self.paddle_width
        else:
            offset = (self.screen_width / 2) - self.paddle_width

        self.setposition(offset, 0)
