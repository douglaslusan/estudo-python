from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")
FONT_GAMEOVER = ("Courier", 60, "bold")


class Score(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color('darkBlue')
		self.hideturtle()
		self.penup()
		self.update_score()

	def update_score(self):
		self.goto(-270, 250)
		self.write(f'Level: {self.score}', align='left', font=FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write(f'GAME OVER', align=ALIGNMENT, font=("Courier", 70, "bold"))

	def increase_score(self):
		self.clear()
		self.score += 1
		self.update_score()
