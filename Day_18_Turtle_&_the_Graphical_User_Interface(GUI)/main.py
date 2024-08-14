from turtle import Turtle, Screen

tim = Turtle()
tim.shape("circle")
tim.color("black")

# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()













screen = Screen()
screen.exitonclick()