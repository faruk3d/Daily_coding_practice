from turtle import Turtle, Screen

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
my_list = [{"num_side": 3, "color": "dark turquoise"}, {"num_side": 4, "color": "green yellow"}, {"num_side": 5, "color": "gold"}, {
    "num_side": 6, "color": "sienna"}, {"num_side": 7, "color": "tomato"}, {"num_side": 8, "color": "hot pink"}, {"num_side": 9, "color": "medium orchid"}, {"num_side": 10, "color": "slate blue"}]

for item in my_list:
    angle = 360 / item.get("num_side")
    color = item.get("color")
    for l in range(item.get("num_side")):
        tim.color(color)
        tim.left(angle)
        tim.forward(100)


screen = Screen()
screen.exitonclick()
