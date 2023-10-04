from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.12)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score_board.scoring()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset_score()
        snake.reset_snake()

    for segment in snake.segment_l[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset_score()
            snake.reset_snake()

screen.exitonclick()
