from turtle import Turtle


UP = 90
DOWN = 270

        
class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.penup()
        self.goto(position)
        
    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)  