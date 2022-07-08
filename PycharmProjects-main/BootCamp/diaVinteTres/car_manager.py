from random import randint, choice
from turtle import Turtle
from random import choice

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 2



class CarManager():
	def __init__(self):
		self.all_cars = []
		self.car_speed = STARTING_MOVE_DIST

	def create(self):
		random_chance = randint(1, 6)
		if random_chance == 1:
			new_car = Turtle()
			new_car.penup()
			new_car.shape('square')
			new_car.shapesize(stretch_wid=1, stretch_len=2)
			new_car.color(choice(COLORS))
			new_car.setheading(180)
			new_car.goto(200, self.aleatorio())
			self.all_cars.append(new_car)

	def aleatorio(self):
		lista = [-210, -190, -170, -150, -130, -110, -90, -70, -50, -30, -10, 10, 30, 50, 70, 90, 110, 130,
				 150, 170, 190, 210, 230, 250]
		y = choice(lista)
		return y

	def move_cars(self):
		for car in self.all_cars:
			car.fd(self.car_speed)

	def level_up(self):
		self.car_speed += MOVE_INCREMENT
