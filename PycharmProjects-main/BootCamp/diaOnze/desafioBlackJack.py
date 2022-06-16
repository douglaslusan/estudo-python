import random

def printCards(lista):
	for i in range(len(lista)):
		if lista[i] == 1:
			print('''
			 ___  
		    |A  | 
		    |(`)| 
		    |___| ''')

		elif lista[i] == 11:
			print('''
			 ___  
			|A  | 
			|(`)| 
			|___| ''')

		elif lista[i] == 10:
			print('''
			 ___  
		 	|10 | 
		 	|(`)| 
		 	|___| ''')

		elif lista[i] == 9:
			print('''
			 ___   
		 	|9  | 
		 	|(`)| 
		 	|___| ''')
		elif lista[i] == 8:
			print('''
			 ___  
		 	|8  | 
		 	|(`)| 
		 	|___| ''')
		elif lista[i] == 7:
			print('''
			 ___  
		 	|7  | 
		 	|(`)| 
		 	|___| ''')
		elif lista[i] == 6:
			print('''
			 ___  
		 	|6  | 
		 	|(`)| 
		 	|___| ''')
		elif lista[i] == 5:
			print('''
			 ___  
		 	|5  | 
		 	|(`)| 
		 	|___| ''')
		elif lista[i] == 4:
			print('''
			 ___  
		 	|4  | 
		 	|(`)| 
		 	|___| ''')
		elif lista[i] == 3:
			print('''
			 ___  
		 	|3  | 
		 	|(`)| 
		 	|___| ''')
		elif lista[i] == 2:
			print('''
			 ___  
		 	|2  | 
		 	|(`)| 
		 	|___| ''')


def sum_hand(lista):
	'''faz a soma e das cartas na mao e vefica se ja ultrapassou o 21 e se tiver o 11 que seria o A, modifica para 1'''
	result = 0
	for i in range(len(lista)):
		result = result + lista[i]
		if result > 21:
			if 11 in lista:
				for j in range(len(lista)):
					if lista[j] == 11 and result > 21:
						lista[j] = 1
						result = sum_hand(lista)
						return result

	return result

def choose_card():
	'''escolhe carta da lista'''
	list_card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(list_card)
	return card

list_hand = list()
list_pc_hand = list()


for i in range(2):
	list_hand.append(choose_card())
	list_pc_hand.append(choose_card())

total_hand = sum_hand(list_hand)
total_pc = sum_hand(list_pc_hand)

opc = 'Y'

while opc == 'Y':
	total_hand = sum_hand(list_hand)
	print(f'\nvoce recebeu as cartas {list_hand}')
	if total_hand > 21:
		print('VOCE PERDEU')
		print(total_hand)
		exit()
	print(total_hand)

	printCards(list_hand)
	opc = input('Gostaria de pedir mais carta? [Y / N]: ').upper()
	if opc == 'Y':
		list_hand.append(choose_card())

	else:
		opc = 'N'
		total_hand = sum_hand(list_hand)
		total_pc = sum_hand(list_pc_hand)
		while total_pc < total_hand:
			if total_pc > 21:
				print('VOCE GANHOU')
				print(f'O PC fez {total_pc} pontos')
				exit()

			list_pc_hand.append(choose_card())
			total_pc = sum_hand(list_pc_hand)

		if total_hand == total_pc:
			print()
			print('*'*10)
			print('EMPATE')

		elif total_hand < total_pc:
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
		print(f'o PC tem {list_pc_hand} total de {total_pc}')
		print(f'Suas cartas são {list_hand} total de {total_hand}')
		print('*' * 10)
