from turtle import Turtle
import random

class Ball:
    def __init__(self):
        self.pong_ball = Turtle()
        self.pong_ball.shape("circle")
        self.pong_ball.color("white")
        self.pong_ball.penup()

        self.x_move = random.choice([-10, 10])
        self.y_move = random.choice([-10, 10])

    def move(self):
        new_x = self.pong_ball.xcor() + self.x_move
        new_y = self.pong_ball.ycor() + self.y_move
        self.pong_ball.goto(new_x, new_y)

    def wall_collision(self):
        if self.pong_ball.ycor() > 280 or self.pong_ball.ycor() < -280:
            self.y_move *= -1




