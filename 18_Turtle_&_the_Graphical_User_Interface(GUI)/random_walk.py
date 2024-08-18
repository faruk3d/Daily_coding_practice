import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.shape("circle")
tim.speed("fastest")
tim.pensize(20)
directions = [0, 90, 180, 270]

def random_color():
    r = random.choice(range(256))
    g =  random.choice(range(256))
    b = random.choice(range(256))
    return (r, g, b)

for _ in range(300):
    tim.pencolor(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(30)