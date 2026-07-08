from turtle import Turtle
class Scoreboard(Turtle):


    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", False, 'center' , ('Arial', 20, 'normal'))



    def update_score(self, ball):
            self.clear()
            self.score += 1
            self.write(f"{self.score}", False, 'center', ('Arial', 20, 'normal'))


    def game_over(self):
        self.write(f"Game Over", False, 'center', ('Arial', 50, 'normal'))



