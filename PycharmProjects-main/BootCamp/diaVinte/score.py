from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")
FONT_GAMEOVER = ("Courier", 34, "bold")

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		with open('data.txt') as file:
			self.high_score = int(file.read())
		self.color('yellow')
		self.hideturtle()
		self.penup()
		self.goto(0, 375)


	def update_score(self):
		self.clear()
		self.write(f'SCORE: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

	def reset(self):
		self.clear()
		if self.score > self.high_score:
			self.high_score = self.score
			with open('data.txt', 'w') as file:
				file.write(f'{self.high_score}')
		self.score = 0


	def increase_score(self):
		self.clear()
		self.score += 1
		self.update_score()

