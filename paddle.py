from turtle import Turtle

class Paddle(Turtle):

        def __init__(self, position):
            super().__init__()
            self.shape("square")
            self.color("white")
            self.penup()
            self.shapesize(stretch_wid=4, stretch_len=1)
            self.goto(position)

        # Connecting user paddle to a keybind
        def move_up(self):
            self.goto(self.xcor(), self.ycor() + 30)

        def move_down(self):
            self.goto(self.xcor(), self.ycor() - 30)

        def paddle_2_bot(self, ball):
            if self.ycor() < ball.pong_ball.ycor():
                self.goto(self.xcor(), self.ycor() + 7.5)
            elif self.ycor() > ball.pong_ball.ycor():
                self.goto(self.xcor(), self.ycor() - 7.5)






