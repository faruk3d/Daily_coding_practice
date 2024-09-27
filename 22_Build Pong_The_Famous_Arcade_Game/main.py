from turtle import Screen, Turtle
from paddle import Paddle



# Create the screen
screen = Screen()
screen.setup(width =800, height = 600)
#screen.tracer(0)
screen.bgcolor("black")
screen.title(titlestring = "P O N G")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()