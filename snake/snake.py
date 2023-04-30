from turtle import Turtle,  Screen
import time

from snake_class import Snake
from food import Food

from score import Score
scorre = Score()

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.setup(width=600, height=600)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
gmae_on = True
while gmae_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.move[0].distance(food) < 15:
        # food.goto(random_x, random_y)
        snake.extend()
        food.refresh()
        scorre.score_count()
    if (snake.move[0].xcor() > 290 or snake.move[0].xcor() < -290 or snake.move[0].ycor() > 290 or snake.move[0].ycor() < -290):

        scorre.high_score()
        snake.reset()

    for i in snake.move[1:]:
        if snake.move[0].distance(i) < 10:
            scorre.high_score()
            snake.reset()
screen.exitonclick()
