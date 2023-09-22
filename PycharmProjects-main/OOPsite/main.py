from Parents import *
from Vetor import *
from Abstracao import *

# class Empregado:
# 	empCount = 0
#
# 	def __init__(self, nome, salario):
# 		self.nome = nome
# 		self.salario = salario
# 		Empregado.empCount += 1
#
# 	def imprimirQuantia(self):
# 		print(f'o total de funcionarios {Empregado.empCount}')
#
# 	def imprimirFuncionario(self):
# 		print(f'Nome: {self.nome} Salario: {self.salario}')
#
#
# func1 = Empregado('Douglas', 2000)
# func2 = Empregado('aline', 2000)
# func3 = Empregado('raziel', 2000)
#
# func1.imprimirQuantia()
# func1.imprimirFuncionario()
# func2.imprimirFuncionario()
# func3.imprimirFuncionario()
#
# func1.idade = 20  # pode ser adicionado atributo fora da classe
#
# print(func1.idade)
#
# print(getattr(func1, 'salario'))  # Retorna valor de um atributo
#
# print(hasattr(func1, 'age'))  # verificar se existe um atributo, retorna TRUE ou FALSE
#
# setattr(func1, 'cpf', 30533245800)  # verificar se existe um atributo, se nao, será criado
#
# print(func1.cpf)
#
# delattr(func1, 'cpf')  # Deleta atributo 'cpf'
#
# print("Employee.__doc__:", Empregado.__doc__)
# print("Employee.__name__:", Empregado.__name__)
# print("Employee.__module__:", Empregado.__module__)
# print("Employee.__bases__:", Empregado.__bases__)
# print("Employee.__dict__:", Empregado.__dict__)

# from Ponto import Point
#
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts
# del pt1
# del pt2
# del pt3


# f = Filho()
#
# f.metodoFilho()
# f.metodoPai()
# f.setAtributo(200)
# f.getAtributo()
#
# print(issubclass(Filho, Pai))
# print(isinstance(f, Filho))
#
# f.meuMetodo()	 # metodo sobreposto, pois os dois tem o mesmo metodo, prevalece o do objeto

# v1 = Vetores(2,10)
# v2 = Vetores(5,-2)
#
# print(v1 + v2)
# # resultado 7 8

c = SoContador()

c.count()
c.count()

print(c)

