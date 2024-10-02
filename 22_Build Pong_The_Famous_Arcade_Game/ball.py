from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)  
        # self.speed("fastest")
        
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)