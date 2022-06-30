from turtle import Turtle

START_POSITION = [(0,0), (-20,0),(-40,0)]

MOVE_DISTANCE = 20

class Snake:
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]


	def create_snake(self):
		for position in START_POSITION:
			self.add_segment(position)


	def add_segment(self, position):
		new_snake = Turtle(shape='square')
		new_snake.color('white')
		new_snake.penup()
		new_snake.goto(position)
		self.segments.append(new_snake)

	def extend(self):
	# add a new segment to the snake
		self.add_segment(self.segments[-1].position())


	def move(self):
		for seg in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[seg - 1].xcor()
			new_y = self.segments[seg - 1].ycor()
			self.segments[seg].goto(new_x, new_y)
		self.head.fd(MOVE_DISTANCE)

	def up(self):
		if self.head.heading() != 270:
			self.head.setheading(90)

	def down(self):
		if self.head.heading() != 90:
			self.head.setheading(270)

	def left(self):
		if self.head.heading() != 0:
			self.head.setheading(180)

	def right(self):
		if self.head.heading() != 180:
			self.head.setheading(0)

