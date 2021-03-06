from turtle import Turtle


class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color('white')
		self.penup()
		self.move_speed = 0.07
		self.x_move = 10
		self.y_move = 10

	def move(self):
		self.new_x = self.xcor() + self.x_move
		self.new_y = self.ycor() + self.y_move
		self.goto(self.new_x, self.new_y)

	def reset_ball(self):
		self.goto(0,0)
		self.move_speed = 0.1

	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1
