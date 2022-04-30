class Pai:
	paiAtributo = 100
	def __init__(self):
		print('Chamando o construtor Pai')

	def metodoPai(self):
		print('Chamando o metodo Pai')

	def meuMetodo(self):
		print('meu metodo de pai')

	def setAtributo(self, atributo):
		Pai.paiAtributo = atributo

	def getAtributo(self):
		print('pai atributo', Pai.paiAtributo)

class Filho(Pai):
	def __init__(self):
		print('chamando o construtor filho')

	def	metodoFilho(self):
		print('chamando o metodo filho')

	def meuMetodo(self):
		print('meu metodo de filho')


