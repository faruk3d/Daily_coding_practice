from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.speed("fastest")