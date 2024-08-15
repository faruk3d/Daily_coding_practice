from turtle import Turtle, Screen
import random as r

tim = Turtle()
# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# Version 1
my_list = [{"num_side": 3, "colour": "dark turquoise"}, {"num_side": 4, "colour": "green yellow"}, {"num_side": 5, "colour": "gold"}, {
    "num_side": 6, "colour": "sienna"}, {"num_side": 7, "colour": "tomato"}, {"num_side": 8, "colour": "hot pink"}, {"num_side": 9, "colour": "medium orchid"}, {"num_side": 10, "colour": "slate blue"}]

for item in my_list:
    angle = 360 / item.get("num_side")
    colour = item.get("colour")
    for l in range(item.get("num_side")):
        tim.color(colour)
        tim.left(angle)
        tim.forward(100)

# Version 2
# colours = ["dark turquoise", "green yellow", "gold", "sienna", "tomato", "hot pink", "medium orchid", "slate blue"]
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.right(angle)
#         tim.forward(100)

# for shape_side in range(3, 11):
#     tim.color(r.choice(colours))
#     draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
