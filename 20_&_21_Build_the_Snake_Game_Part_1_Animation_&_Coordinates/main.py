from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title(titlestring = "Metal Gear Solide Snake")

# Create a snake body
snake = Snake()
food = Food()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()



# Create a scoreboard

# Detect collision with wall
# Detect collision with tail












screen.exitonclick()