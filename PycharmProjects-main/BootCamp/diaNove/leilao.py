def titulo():
	print('*-'*30)
	print(f'{"COMEÇANDO O LEILÃO":^60}')
	print('*-' * 30)


def achar_maximo(clientes):
	max_key = max(clientes, key=lambda key: clientes[key])
	print(f'O vencedor é: {max_key} que ofertou valor de ${clientes[max_key]}')

def logo():
	print('''
						 ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
	
	''')

clientes = {}

titulo()
while True:
	logo()
	nome = input('digite seu Nome para dar um lance: ').title()
	valor = float(input('qual o valor do lance $'))

	clientes[nome] = valor

	opcao = input('quer continuar? [S/N] ').upper()

	if opcao == 'S':
		print('\n')
	else:
		achar_maximo(clientes)
		break

