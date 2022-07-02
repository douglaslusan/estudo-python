from turtle import Turtle

class Paddle(Turtle):

	def __init__(self):
		super().__init__()
		self.x_pos = 350
		self.y_pos = 0
		self.paddle = Turtle()
		self.create_paddle()

	def create_paddle(self):
		self.paddle.hideturtle()
		self.paddle.shape('square')
		self.paddle.color('white')
		self.paddle.penup()
		self.paddle.goto(self.x_pos, self.y_pos)
		self.paddle.showturtle()
		self.paddle.shapesize(5, 1)

	def up(self):
		new_y = self.paddle.ycor() + 30
		if new_y > 270:
			new_y = 270
		else:
			self.paddle.goto(self.paddle.xcor(), new_y)

	def down(self):
		new_y = self.paddle.ycor() - 30
		if new_y < -270:
			new_y = -270
		else:
			self.paddle.goto(self.paddle.xcor(), new_y)
