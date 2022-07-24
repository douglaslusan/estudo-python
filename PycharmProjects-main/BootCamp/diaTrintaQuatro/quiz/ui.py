from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#4C54BA"


class QuizInterface:
	def __init__(self, quiz_brain: QuizBrain):
		self.quiz = quiz_brain
		self.window = Tk()
		self.window.title('Quizz')
		self.window.config(bg=THEME_COLOR, pady=20, padx=20)

		self.score = Label(
			text='Score: 0',
			font=('Arial', 15, 'bold'),
			bg=THEME_COLOR,
			pady=20,
			justify='center',
			foreground='white')
		self.score.grid(row=0, column=1)

		self.question = Canvas(width=300, height=250)
		self.question_text = self.question.create_text(
			150,
			125,
			width=280,
			text='question',
			font=('Arial', 15, 'bold'))
		self.question.grid(row=1, column=0, columnspan=2, pady=50)

		image_true = PhotoImage(file='images/true.png')
		image_false = PhotoImage(file='images/false.png')

		self.button_true = Button(image=image_true, highlightthickness=False, command=self.true_pressed)
		self.button_true.grid(row=2, column=0)

		self.button_false = Button(image=image_false, highlightthickness=False, command=self.false_pressed)
		self.button_false.grid(row=2, column=1)

		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		self.question.config(bg='white')
		if self.quiz.still_has_questions():
			self.score.config(text=f'Score: {self.quiz.score}')
			q_text = self.quiz.next_question()
			self.question.itemconfig(self.question_text, text=q_text)
		else:
			self.question.itemconfig(self.question_text, text='GAME OVER')
			self.score.config(text=f'Score: {self.quiz.score}')
			self.button_false.config(state='disabled')
			self.button_true.config(state='disabled')

	def true_pressed(self):
		self.give_feedback(self.quiz.check_answer('True'))

	def false_pressed(self):
		is_right = self.quiz.check_answer('False')
		self.give_feedback(is_right)

	def give_feedback(self, is_right):
		if is_right:
			self.question.config(bg='green')
		else:
			self.question.config(bg='red')
		self.window.after(1000, self.get_next_question)
