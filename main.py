from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle

#Creating screen background
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
ball = Ball()

# Creating both paddles
left_paddle = Paddle((-280, 0))
right_paddle = Paddle((280, 0))

# User paddle movements
screen.onkeypress(left_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_down, "Down")
screen.listen()


# Game mechanics calling on classes
game_on = True
while game_on:
    ball.move()
    ball.wall_collision()










screen.exitonclick()
