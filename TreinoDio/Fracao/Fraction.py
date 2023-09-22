class Fraction:

	def __init__(self, cima, baixo):
		self.__num = cima
		self.__denom = baixo

	def get_num(self):
		return self.__num

	def get_denom(self):
		return self.__denom

	@staticmethod
	def mdc(n, d):
		while n % d != 0:
			mvelho = n
			nvelho = d

			n = nvelho
			d = mvelho % nvelho
		return d

	def __str__(self):
		return f'{self.__num}/{self.__denom}'

	def __add__(self, other):
		novonum = self.__num * other.__denom + self.__denom * other.__num
		novoden = self.__denom * other.__denom
		comum = self.mdc(novonum, novoden)
		return Fraction((novonum // comum), (novoden // comum))

	def __sub__(self, other):
		novonum = self.__num * other.__denom - self.__denom * other.__num
		novoden = self.__denom * other.__denom
		comum = self.mdc(novonum, novoden)
		return Fraction((novonum // comum), (novoden // comum))

	def __mul__(self, other):
		novonum = self.__num * other.__denom * self.__denom * other.__num
		novoden = self.__denom * other.__denom
		comum = self.mdc(novonum, novoden)
		return Fraction((novonum // comum), (novoden // comum))

	def __truediv__(self, other):
		novonum = self.__num * other.__denom // self.__denom * other.__num
		novoden = self.__denom * other.__denom
		comum = self.mdc(novonum, novoden)
		return Fraction((novonum // comum), (novoden // comum))


	def __eq__(self, other):
		primeiro = self.__num * self.__denom
		segundo = other.__num * self.__denom
		return primeiro == segundo

	def __gt__(self, other):
		produto_cruzado_atual = self.__num * other.get_denom()
		produto_cruzado_outra = other.get_num() * self.__denom
		return produto_cruzado_atual > produto_cruzado_outra

	def __ge__(self, other):
		produto_cruzado_atual = self.__num * other.get_denom()
		produto_cruzado_outra = other.get_num() * self.__denom
		return produto_cruzado_atual >= produto_cruzado_outra

	def __lt__(self, other):
		produto_cruzado_atual = self.__num * other.get_denom()
		produto_cruzado_outra = other.get_num() * self.__denom
		return produto_cruzado_atual < produto_cruzado_outra

	def __le__(self, other):
		produto_cruzado_atual = self.__num * other.get_denom()
		produto_cruzado_outra = other.get_num() * self.__denom
		return produto_cruzado_atual <= produto_cruzado_outra

	def __ne__(self, other):
		produto_cruzado_atual = self.__num * other.get_denom()
		produto_cruzado_outra = other.get_num() * self.__denom
		return produto_cruzado_atual != produto_cruzado_outra
