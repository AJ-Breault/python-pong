from turtle import Turtle, Screen
from ball import Ball


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
paddles = []
positions = [(-280, 0), (280, 0)]
ball = Ball()

for position in positions:
    paddle = Turtle()
    paddle.color("white")
    paddle.shape("square")
    paddle.shapesize(4, 1)
    paddle.penup()
    paddle.goto(position)
    paddles.append(paddle)

def move_up():
    p = paddles[0]
    p.goto(p.xcor(), p.ycor() + 20)

def move_down():
    p = paddles[0]
    p.goto(p.xcor(), p.ycor() - 20)



screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.listen()


ball.random_direction()

game_on = True
while game_on:

    if -280 < ball.pongball.xcor() < 280:
        ball.move()
    else:
        game_on = False

        #next task make ball bounce when it hits a wall









screen.exitonclick()
