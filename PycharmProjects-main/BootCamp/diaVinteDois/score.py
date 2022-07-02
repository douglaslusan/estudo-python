from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 40, "bold")
FONT_GAMEOVER = ("Courier", 60, "bold")

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.score_l = 0
		self.score_r = 0
		self.color('yellow')
		self.hideturtle()
		self.penup()
		self.update_score()

	def update_score(self):
		self.goto(-100, 220)
		self.write(f'{self.score_l}', align=ALIGNMENT, font=FONT)
		self.goto(100, 220)
		self.write(f'{self.score_r}', align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.goto(0,0)
		self.write(f'GAME OVER', align=ALIGNMENT, font=FONT_GAMEOVER)

	def increase_score_l(self):
		self.clear()
		self.score_l += 1
		self.update_score()

	def increase_score_r(self):
		self.clear()
		self.score_r += 1
		self.update_score()