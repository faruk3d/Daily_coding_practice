from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)

def move_counter():
    tim.left(45)
    
def move_clockwise():
    tim.right(45)
    
screen.listen()
screen.onkey(key = 'w', fun = move_forwards)
screen.onkey(key = 's', fun = move_backwards)
screen.onkey(key = 'a', fun = move_counter)
screen.onkey(key = 'd', fun = move_clockwise)
screen.exitonclick()