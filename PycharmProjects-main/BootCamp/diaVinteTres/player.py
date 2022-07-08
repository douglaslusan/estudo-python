from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE = 280


class Player(Turtle):
	def __init__(self):
		super().__init__()
		self.penup()
		self.shape('turtle')
		self.goto(START_POSITION)
		self.setheading(90)

	def move(self):
		self.fd(MOVE_DISTANCE)

	def move_back(self):
		self.back(MOVE_DISTANCE)

	def restart(self):
		if self.ycor() >= FINISH_LINE:
			self.goto(START_POSITION)
