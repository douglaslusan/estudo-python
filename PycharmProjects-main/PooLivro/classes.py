from superclasse import Dog

class ServiceDog(Dog):
	def __init__(self, nome, idade, tamanho, usuario):
		Dog.__init__(self, nome, idade, tamanho)
		self.Usuario = usuario
		self.is_working = False

	def Andar(self):
		print(f'o {self.Nome} está guiando o {self.Usuario}')


	def Late(self):
		if self.is_working:
			print(f'Agora estou trabalhando, nao posso latir')
		else:
			Dog.Late(self)

	def __str__(self):
		return f'{self.Nome}'

class FrisbeeDog(Dog):
	def __init__(self, nome, idade, tamanho, ):
		Dog.__init__(self, nome, idade, tamanho)
		self.Frisbee = None


	def Pega(self, frisbee):
		self.Frisbee = frisbee


	def Entrega(self):
		self.Frisbee = None


	def Late(self):
		if self.Frisbee:
			print('Impossivel latir com o frisbee na boca')
		else:
			Dog.Late(self)

	def __str__(self):
		if self.Frisbee:
			return f'Estou com um Frisbee {self.Frisbee}, preciso entrega lo'
		else:
			return f'{self.Nome}'
