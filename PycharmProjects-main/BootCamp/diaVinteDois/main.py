from paddle import Paddle
from turtle import Screen
import time
from ball import Ball
from wall import Wall
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
wall = Wall()
score = Score()


r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)

ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_is_on = True

while game_is_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	if ball.ycor() > 275 or ball.ycor() < -275:
		ball.bounce_y()

	if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
		ball.bounce_x()
		ball.move_speed *= 0.9

	if ball.xcor() > 375:
		score.increase_score_l()
		ball.reset_ball()
		ball.bounce_x()

	if ball.xcor() < -375:
		score.increase_score_r()
		ball.reset_ball()
		ball.bounce_x()

	if score.score_l == 10 or score.score_r == 10:
		score.game_over()
		game_is_on = False




screen.exitonclick()
