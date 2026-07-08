from turtle import Turtle

class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.teleport(0, 300)
        self.setheading(270)
        self.hideturtle()
        self.color("white")

    def create_net(self):
        for _ in range(100):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)