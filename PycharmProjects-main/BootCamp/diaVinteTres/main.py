from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Score


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
screen.onkey(player.move, 'Up')
screen.onkey(player.move_back, 'Down')
screen.listen()

cars = CarManager()
score = Score()

game_is_on = True


while game_is_on:
	time.sleep(0.1)
	screen.update()
	cars.create()
	cars.move_cars()
# 	detect colision
	for car in cars.all_cars:
		if car.distance(player) < 20:
			game_is_on = False
			score.game_over()

	if player.finish():
		score.increase_score()
		player.go_to_start()
		cars.level_up()

screen.exitonclick()
