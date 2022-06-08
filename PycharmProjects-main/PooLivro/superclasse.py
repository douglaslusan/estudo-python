class Dog:
	def __init__(self, nome, idade, tamanho):
		self.Nome = nome
		self.Idade = idade
		self.Tamanho = tamanho


	def Late(self):
		if self.Tamanho < 29:
			print(f'{self.Nome} está latindo woof woof woof')
		else:
			print(f'{self.Nome} está latindo WOOF WOOF WOOF')


	def __str__(self):
		return f'{self.Nome}'
