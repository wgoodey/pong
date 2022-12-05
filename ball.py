from random import choice, randint
from turtle import Turtle


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
        super().__init__("circle")
        self.fillcolor("white")
        self.penup()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.set_initial_angle()

    def set_initial_angle(self):
        angle = 180
        while angle == 180:
            angle = randint(145, 215)
        right = choice([True, False])
        if right:
            angle -= 180
        self.setheading(angle)

    def move(self, distance):
        super().forward(distance)
        # self.settiltangle(-self.heading())

    def bounce(self, surface="wall"):
        bounce_type = {
            "wall" : 0,
            "paddle": 180
        }
        self.setheading(-self.heading() + bounce_type[surface])
