from random import choice, randint
from turtle import Turtle

INITIAL_SPEED = 0.05
SPEED_MODIFIER = 0.9
MOVE_DISTANCE = 10

def set_initial_angle():
    angle = 180
    while angle == 180:
        angle = randint(145, 215)
    right = choice([True, False])
    if right:
        angle -= 180
    return angle


class Ball(Turtle):

    def __init__(self, screen_height, screen_width):
        super().__init__("square")
        self.fillcolor("white")
        self.penup()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.ball_speed = INITIAL_SPEED
        self.prepare_ball()

    def prepare_ball(self):
        self.ball_speed = INITIAL_SPEED
        angle = 180
        while angle == 180:
            angle = randint(145, 215)
        right = choice([True, False])
        if right:
            angle -= 180
        self.setheading(angle)
        self.settiltangle(-self.heading())

    def move(self):
        self.forward(MOVE_DISTANCE)

    def bounce(self, surface="wall"):
        bounce_type = {
            "wall" : 0,
            "paddle": 180
        }
        if surface == "paddle":
            self.ball_speed *= SPEED_MODIFIER

        self.setheading(-self.heading() + bounce_type[surface])
        self.settiltangle(-self.heading())
