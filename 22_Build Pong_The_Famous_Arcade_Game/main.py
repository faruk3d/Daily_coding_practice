from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

RIGHT_P_POSITION = (350, 0)
LEFT_P_POSITION = (-350, 0)

# Create the screen
screen = Screen()
screen.setup(width =800, height = 600)
screen.bgcolor("black")
screen.title(titlestring = "P O N G")
screen.tracer(0)

# Create and move a paddle
r_paddle = Paddle(RIGHT_P_POSITION)

# Create another paddle
l_paddle = Paddle(LEFT_P_POSITION)

# Create the ball and make it move
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")



# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()