from turtle import Turtle, Screen
from snake import Snake
import time

snake = Snake()



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
	time.sleep(0.2)
	snake.move()

# while True:
# 	snake.fd(5)
# 	if snake.xcor() < -790 or snake.xcor() > 790:
# 		break
# 	if snake.ycor() < -790 or snake.ycor() > 790:
# 		break

screen.exitonclick()
