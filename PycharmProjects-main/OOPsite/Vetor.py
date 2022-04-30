class Vetores:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return f'vetor {self.a} {self.b}'

	def __add__(self, other):
		return Vetores(self.a + other.a, self.b + other.b)
