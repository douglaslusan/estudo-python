from paddle import Paddle
from turtle import Screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)

paddle_j1 = Paddle()


screen.listen()
screen.onkeypress(paddle_j1.up, 'Up')
screen.onkeypress(paddle_j1.down, 'Down')

game_is_on = True

while True:
	screen.update()


screen.exitonclick()
