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
            self.goto(self.xcor(), self.ycor() + 20)

        def move_down(self):
            self.goto(self.xcor(), self.ycor() - 20)

