from turtle import Turtle

class Wall(Turtle):
	def __init__(self):
		super().__init__()
		self.pensize(5)
		self.color('white')
		self.penup()
		self.goto(-380, 295)
		self.pendown()
		self.goto(380, 295)
		self.penup()
		self.goto(-380, -295)
		self.pendown()
		self.goto(380, -295)