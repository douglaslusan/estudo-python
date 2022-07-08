from turtle import Screen
import time
from player import Player
from car_manager import CarManager


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)

player = Player()
screen.onkey(player.move, 'Up')
screen.onkey(player.move_back, 'Down')
screen.listen()

cars = CarManager()

game_is_on = True


while game_is_on:
	time.sleep(0.1)
	player.restart()
	screen.update()
	cars.create()
	cars.move_cars()


screen.exitonclick()
