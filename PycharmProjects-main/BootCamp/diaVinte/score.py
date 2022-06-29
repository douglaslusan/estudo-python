from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")
FONT_GAMEOVER = ("Courier", 34, "bold")

class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color('yellow')
		self.hideturtle()
		self.penup()
		self.goto(0, 375)


	def upadate_score(self):
		self.write(f'SCORE: {self.score}', align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.goto(0,0)
		self.write(f'GAME OVER', align=ALIGNMENT, font=FONT_GAMEOVER)

	def increase_score(self):
		self.clear()
		self.score += 1
		self.upadate_score()

