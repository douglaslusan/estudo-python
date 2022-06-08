class Gato:
	def __init__(self, nome, idade, tamanho):
		self.Nome = nome
		self.Idade = idade
		self.Tamanho = tamanho


	def Miar(self):
		print('Miau')

	def __str__(self):
		return f'sou um gato chamado {self.Nome}'