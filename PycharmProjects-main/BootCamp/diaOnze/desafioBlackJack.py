import random

def pedir_cartas(lista):
	lista_mao.append(lista_cartas[random.randint(0, 12)])


def somarMao(lista):
	soma = 0
	for i in range(len(lista)):
		soma = soma + lista[i]

		if soma > 21:
			if 11 in lista:
				for j in range(len(lista)):
					if lista[j] == 11 and soma > 21:
						lista[j] = 1
						soma = somarMao(lista)
						return soma
			else:
				print(f'Voce PERDEU {soma}')
				exit()
	return soma


lista_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
lista_mao = list()
lista_pc_mao = list()

for i in range(2):
	lista_mao.append(lista_cartas[random.randint(0, 12)])


for i in range(2):
	lista_pc_mao.append(lista_cartas[random.randint(0, 12)])


total_mao = somarMao(lista_mao)
total_pc = somarMao(lista_pc_mao)

opc = 'Y'
decisao = False

while not decisao:
	while opc == 'Y':
		print(f'voce recebeu as cartas {lista_mao}')
		total_mao = somarMao(lista_mao)
		print(total_mao)
		opc = input('Gostaria de pedir mais carta? [Y / N]: ').upper()
		if opc == 'Y':
			pedir_cartas(lista_mao)
		else:
			opc = 'N'
			total_mao = somarMao(lista_mao)
			total_pc = somarMao(lista_pc_mao)
			if total_mao == total_pc:
				print()
				print('*'*10)
				print('EMPATE')

			elif total_mao < total_pc:
				print()
				print('*' * 10)
				print('VOCE PERDEU')
			else:
				print()
				print('*' * 10)
				print('VOCE GANHOU')
			print(f'o PC tem {lista_pc_mao} total de {total_pc}')
			print(f'Suas cartas são {lista_mao} total de {total_mao}')
			print('*' * 10)
			decisao = True


