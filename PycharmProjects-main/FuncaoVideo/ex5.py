from random import randint


def sorteia(lista):
	for i in range(5):
		lista.append(randint(1, 30))

def somaPar(lista):
	s = 0
	for i in lista:
		if i % 2 == 0:
			s += i
	print(f'A soma dos pares na lista é \033[34m{s}')

numeros = list()

sorteia(numeros)

print(numeros)

somaPar(numeros)
