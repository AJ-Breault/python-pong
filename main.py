from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
import time
from paddle import Paddle
from net import Net

# Creating screen background
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Creating net
net = Net()
net.create_net()

ball = Ball()

# Creating both paddles
left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))

# User paddle movements
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.listen()

# Adding Score
user_score = Scoreboard((-100, 265))
bot_score = Scoreboard((100, 265))
game_over = Scoreboard((0, 0))
game_over.clear()

# Game mechanics calling on classes
game_on = True
while game_on:
    time.sleep(0.04)
    screen.update()
    ball.move()
    ball.wall_collision()

    if ball.pong_ball.xcor() > 0:
        right_paddle.paddle_2_bot(ball)

    if (
        ball.pong_ball.distance(right_paddle) < 50 and ball.pong_ball.xcor() > 360
    ) or (
        ball.pong_ball.distance(left_paddle) < 50 and ball.pong_ball.xcor() < -360
    ):
        ball.paddle_collision()

    if ball.pong_ball.xcor() > 385:
        user_score.update_score(ball)
        ball.reset()
        time.sleep(1)

    elif ball.pong_ball.xcor() < -385:
        bot_score.update_score(ball)
        ball.reset()
        time.sleep(1)

    if bot_score.score == 7 or user_score.score == 7:
        game_over.game_over()
        game_on = False

screen.exitonclick()
