import random

palavras = ['airam', 'douglas', 'aline', 'comida']
letraAdvinhada = list()
letrasJaChutadas = list()

ganhou = 7

palavraEscolhida = random.choice(palavras)
tamanho = len(palavraEscolhida)

for i in palavraEscolhida:
	letraAdvinhada.append('_ ')
print(''.join(letraAdvinhada))

while ganhou:
	ganhou -= 1

	while True:  # verificacao de letras digitadas
		letraEscolhida = input('\nDIGITE UMA LETRA: ')
		if letraEscolhida.isalpha():
			if letraEscolhida not in letrasJaChutadas:
				letrasJaChutadas.append(letraEscolhida)
				break
			else:
				print('Voce ja chutou esta letra')
		else:
			print('Digite somente LETRAS')

	print(f'Voce ja Chutou as letras:\n{letrasJaChutadas}\n\n')

	for i in range(tamanho):
		if letraEscolhida == palavraEscolhida[i]:
			letraAdvinhada[i] = letraEscolhida
			ganhou += 1
			if ganhou > 7:
				ganhou = 7

	if ganhou == 0:
		print('Voce perdeu')
		break

	print(f'Voce tem {ganhou} chances' )

	if '_ ' not in letraAdvinhada:
		ganhou = 0
		print('ganhou')
		break


	print(' '.join(letraAdvinhada))
