from turtle import Turtle
import random

DIRECTIONS = [45, 135, 225, 315]

class Ball:

    def __init__(self):
        self.pongball = Turtle()
        self.pongball.shape("circle")
        self.pongball.color("white")
        self.pongball.penup()
        self.random_direction()

    def random_direction(self):
        self.pongball.setheading(random.choice(DIRECTIONS))

    def move(self):
        self.pongball.forward(10)




