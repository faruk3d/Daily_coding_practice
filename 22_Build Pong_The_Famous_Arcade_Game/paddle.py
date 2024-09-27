from turtle import Turtle


UP = 90
DOWN = 270


class Paddle:
    def __init__(self) -> None:   
        self.create_paddle()
        
    
    def create_paddle(self):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid = 5, stretch_len = 1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(350, 0)
        
    def up(self):
        new_y = self.paddle.ycor() + 40
        self.paddle.goto(self.paddle.xcor(), new_y)
        
    def down(self):
        new_y = self.paddle.ycor() - 40
        self.paddle.goto(self.paddle.xcor(), new_y)