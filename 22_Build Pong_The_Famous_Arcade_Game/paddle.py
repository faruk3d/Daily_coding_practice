from turtle import Turtle

STARTING_POSITION = [(0, 0), (0, 20), (0, 40)]


class Paddle:
    def __init__(self) -> None:   
        self.segments = []
        self.create_paddle()
        
    
    def create_paddle(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        new_segment = Turtle(shape = "square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)