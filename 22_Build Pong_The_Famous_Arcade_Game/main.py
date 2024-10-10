from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Detect collision with both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
        
    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    

screen.exitonclick()