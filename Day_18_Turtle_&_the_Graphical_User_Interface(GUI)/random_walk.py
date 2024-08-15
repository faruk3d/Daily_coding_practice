import random
from turtle import Turtle, Screen

tim = Turtle()
colours = ["dark turquoise", "green yellow", "gold", "sienna", "tomato", "hot pink", "medium orchid", "slate blue"]
directions = [0, 90, 180, 270]


tim.shape("circle")
tim.speed("fastest")
tim.pensize(20)

for _ in range(300):
    tim.color(random.choice(colours))
    #tim.pencolor((random.choice[0, 255], random.choice[0, 255], random.choice[0, 255]))
    tim.setheading(random.choice(directions))
    tim.forward(30)

screen = Screen()
screen.exitonclick()