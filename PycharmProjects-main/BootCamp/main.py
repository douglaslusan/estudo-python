import random

palavras = ['airam', 'douglas', 'aline', 'comida']
letraAdvinhada = list()
letrasJaChutadas = list()

palavraEscolhida = random.choice(palavras)

for i in range(len(palavraEscolhida)):
	letraAdvinhada.append('_ ')
print(palavraEscolhida)
print(letraAdvinhada)
while True:

	letraEscolhida = input('\nDIGITE UMA LETRA: ')
	letrasJaChutadas.append(letraEscolhida)
	print(f'Voce ja Chutou as letras:\n{letrasJaChutadas}\n\n')


	for i in range(len(palavraEscolhida)):
		if letraEscolhida == palavraEscolhida[i]:
			letraAdvinhada[i] = letraEscolhida


	print(letraAdvinhada)