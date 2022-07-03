from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, x_pos, y_pos):
		super().__init__()
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.hideturtle()
		self.shape('square')
		self.color('white')
		self.penup()
		self.goto(self.x_pos, self.y_pos)
		self.showturtle()
		self.shapesize(5, 1)

	def up(self):
		new_y = self.ycor() + 30
		if new_y > 270:
			new_y = 270
		else:
			self.goto(self.xcor(), new_y)

	def down(self):
		new_y = self.ycor() - 30
		if new_y < -270:
			new_y = -270
		else:
			self.goto(self.xcor(), new_y)
