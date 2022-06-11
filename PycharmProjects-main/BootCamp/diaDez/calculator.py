def logo():
	print('''
 _____________________
|  _________________  |
| | Douglas      0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')


def calculo(n1, n2, sinal):
	if sinal == '+':
		return n1 + n2
	if sinal == '-':
		return n1 - n2
	if sinal == '*':
		return n1 * n2
	if sinal == '/':
		return n1 / n2


logo()

while True:
	n1 = float(input('digite o numero: '))
	operacao = input('digite o operador: \n'
					 '+\n-\n*\n/\n')
	n2 = float(input('digite o numero: '))
	result = calculo(n1, n2, operacao)
	escolha = input(f'o resultado é {result}\nDeseja continuar calculando com o resultado?\n'
		  f'digite [E] para encerrar ou [C] para continuar ou [N] para comecar um novo calculo: ').upper()
	if escolha == 'E':
		break

	elif escolha == 'C':
		while escolha == 'C':
			operacao = input('digite o operador: \n'
							 '+\n-\n*\n/\n')
			n2 = float(input('digite o numero: '))
			result = calculo(result, n2, operacao)
			escolha = input(f'o resultado é {result}\nDeseja continuar calculando com o resultado?\n'
							f'digite [E] para encerrar ou [C] para continuar ou [N] para comecar um novo calculo: ').upper()
			if escolha == 'E':
				break
print('\n\n**** OBRIGADO POR UTILIZAR NOSSA CALCULADORA ****')