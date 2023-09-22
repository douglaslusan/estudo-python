from superclasse import Dog

class Hotel:
	def __init__(self, nome):
		self.kennel = nome


	def check_in(self, dog):
		if isinstance(dog, Dog):
			self.Clientes.append(dog.Nome)
			self.Dogs.append(dog)
			print(f'{dog.Nome} foi checado e hospedado')
		else:
			print(f'So aceitamos Cães, sinto muito')

	def check_out(self, nome):
		for i in range(0, len(self.Clientes)):
			if nome == self.Clientes[i]:
				dog = self.Dogs
				del self.Clientes[i]
				del self.Dogs[i]
				print(f'feito check-out de {dog.nome}')
				return dog
			else:
				print(f'Desculpe, {nome}, nao está em nosso Hotel')
				return None


	def __str__(self):
		return f'{self.Clientes}'
