import random
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
directions = [0, 90, 180, 270]

def random_color():
    r = random.choice(range(256))
    g =  random.choice(range(256))
    b = random.choice(range(256))
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        
draw_spirograph(5)