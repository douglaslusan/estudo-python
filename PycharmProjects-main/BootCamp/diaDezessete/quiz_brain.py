class QuizBrain:
	def __init__(self, list_question):
		self.question_list = list_question
		self.question_number = 0
		self.score = 0

	def still_has_question(self):
		return self.question_number < len(self.question_list)

	def next_question(self):
		current_question = self.question_list[self.question_number]
		current_answer = self.question_list[self.question_number]
		self.question_number += 1
		answer = input(f'Q.{self.question_number}: {current_question.text} [True/False]? ').title()
		self.check_answer(answer, current_answer.answer)

	def check_answer(self, answer, correct_answer):
		if  answer == correct_answer:
			self.score += 1
			print(f"\033[1;32mYou got it right!\033[0;0m")
		else:
			print("\033[1;91mThat's wrong!\033[0;0m")
		print(f'\033[1;94mYour current Score: {self.score}/{self.question_number}\033[0;0m')

