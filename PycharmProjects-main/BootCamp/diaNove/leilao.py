cliente = {}
listaClientes = []


while True:
	nome = input('digite seu Nome: ')
	valor = float(input('qual o valor a ser ofertado $'))
	opcao = input('quer continuar? [S/N] '). upper()

	cliente[nome] = valor

	if opcao == 'S':
		print('\n' * 10)
	else:
		print(cliente)
		break
