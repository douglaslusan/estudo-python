import random

def imprimirCartas(lista):
	for i in range(len(lista)):
		if lista[i] == 1:
			print('''
			 ___  
		    |A  | 
		    |(`)| 
		    |_\_| ''')

		elif lista[i] == 11:
			print('''
			 ___  
			|A  | 
			|(`)| 
			|_\_| ''')

		elif lista[i] == 10:
			print('''
			 ___  
		 	|10 | 
		 	|(`)| 
		 	|_\_| ''')

		elif lista[i] == 9:
			print('''
			 ___   
		 	|9  | 
		 	|(`)| 
		 	|_\_| ''')
		elif lista[i] == 8:
			print('''
			 ___  
		 	|8  | 
		 	|(`)| 
		 	|_\_| ''')
		elif lista[i] == 7:
			print('''
			 ___  
		 	|7  | 
		 	|(`)| 
		 	|_\_| ''')
		elif lista[i] == 6:
			print('''
			 ___  
		 	|6  | 
		 	|(`)| 
		 	|_\_| ''')
		elif lista[i] == 5:
			print('''
			 ___  
		 	|5  | 
		 	|(`)| 
		 	|_\_| ''')
		elif lista[i] == 4:
			print('''
			 ___  
		 	|4  | 
		 	|(`)| 
		 	|_\_| ''')
		elif lista[i] == 3:
			print('''
			 ___  
		 	|3  | 
		 	|(`)| 
		 	|_\_| ''')
		elif lista[i] == 2:
			print('''
			 ___  
		 	|2  | 
		 	|(`)| 
		 	|_\_| ''')


def somarMao(lista):
	'''faz a soma e das cartas na mao e vefica se ja ultrapassou o 21 e se tiver o 11 que seria o A, modifica para 1'''
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
				continue

	return soma

def escolher_carta():
	'''escolhe carta da lista'''
	lista_cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	carta = random.choice(lista_cartas)
	return carta

lista_mao = list()
lista_pc_mao = list()


for i in range(2):
	lista_mao.append(escolher_carta())
	lista_pc_mao.append(escolher_carta())

total_mao = somarMao(lista_mao)
total_pc = somarMao(lista_pc_mao)

opc = 'Y'

while opc == 'Y':
	print(f'\nvoce recebeu as cartas {lista_mao}')
	total_mao = somarMao(lista_mao)
	if total_mao > 21:
		print('VOCE PERDEU')
		print(total_mao)
		exit()
	print(total_mao)

	imprimirCartas(lista_mao)
	opc = input('Gostaria de pedir mais carta? [Y / N]: ').upper()
	if opc == 'Y':
		lista_mao.append(escolher_carta())

	else:
		opc = 'N'
		total_mao = somarMao(lista_mao)
		total_pc = somarMao(lista_pc_mao)
		while total_pc < total_mao:
			if total_pc > 21:
				print('VOCE GANHOU')
				print(f'O PC fez {total_pc} pontos')
				exit()

			lista_pc_mao.append(escolher_carta())
			total_pc = somarMao(lista_pc_mao)

		if total_mao == total_pc:
			print()
			print('*'*10)
			print('EMPATE')

		elif total_mao < total_pc:
			if total_pc > 21:
				print('*' * 10)
				print('VOCE GANHOU')
			else:
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
