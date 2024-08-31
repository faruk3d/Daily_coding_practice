from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title(titlestring = "Metal Gear Solide Snake")

# Create a snake body
snake = Snake()


# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
# Control the snake


# Detect collision with food
# Create a scoreboard
# Detect collision with wall
# Detect collision with tail












screen.exitonclick()