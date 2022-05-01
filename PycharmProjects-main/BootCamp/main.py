import random

palavras = ['airam', 'douglas', 'aline', 'comida']
letraAdvinhada = list()
letrasJaChutadas = list()

ganhou = 7

palavraEscolhida = random.choice(palavras)

for i in range(len(palavraEscolhida)):
	letraAdvinhada.append('_ ')
print(palavraEscolhida)
print(''.join(letraAdvinhada))

while ganhou:
	letraEscolhida = input('\nDIGITE UMA LETRA: ')
	letrasJaChutadas.append(letraEscolhida)
	print(f'Voce ja Chutou as letras:\n{letrasJaChutadas}\n\n')

	for i in range(len(palavraEscolhida)):
		if letraEscolhida == palavraEscolhida[i]:
			letraAdvinhada[i] = letraEscolhida


	for i in letraAdvinhada:
		if '_ ' not in letraAdvinhada:
			ganhou = 0
			print('ganhou')
			break

	print(' '.join(letraAdvinhada))
