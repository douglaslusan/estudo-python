from turtle import Screen
from snake import Snake
import time
from score import Score
from food import Food

snake = Snake()
food = Food()
score = Score()

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 800)
screen.title('cobrinha')
screen.tracer(0)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()


game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()
	score.update_score()

	# detect collision with food
	if snake.head.distance(food) < 15:
		food.refresh()
		score.increase_score()
		snake.extend()

	# detect collision with wall
	if snake.head.xcor() < -395 or snake.head.xcor() > 395 or snake.head.ycor() < -390 or snake.head.ycor() > 390:
		score.reset()
		snake.reset()

	for segment in snake.segments[2:]:
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()


screen.exitonclick()
