import random

def desenho(vidas):
	if vidas == 6:
		print('''
	  _______
     |/      |
     |      
     |      
     |      
     |      
     |
    _|___
	''')

	elif vidas == 5:
		print('''
	  _______
     |/      |
     |      (_)
     |      
     |      
     |      
     |
    _|___
	''')
	elif vidas == 4:
		print('''
	  _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
	''')
	elif vidas == 3:
		print('''
	  _______
     |/      |
     |      (_)
     |       |/
     |       |
     |      
     |
    _|___
	''')
	elif vidas == 2:
		print('''
	  _______
	 |/      |
	 |      (_)
	 |      \|/
	 |       |
	 |      
	 |
	_|___
	''')
	elif vidas == 1:
		print('''
	  _______
	 |/      |
	 |      (_)
	 |      \|/
	 |       |
	 |      /
	 |
	_|___
	''')
	else:
		print('''
	  _______
	 |/      |
	 |      (_)
	 |      \|/
	 |       |
	 |      / \\
	 |
	_|___
	''')


palavras = ['airam', 'douglas', 'aline', 'comida']
letraAdvinhada = list()
letrasJaChutadas = list()

ganhou = 6

palavraEscolhida = random.choice(palavras)
tamanho = len(palavraEscolhida)

for i in palavraEscolhida:
	letraAdvinhada.append('_ ')
print(''.join(letraAdvinhada))

while ganhou:

	desenho(ganhou)

	while True:  # verificacao de letras digitadas
		letraEscolhida = input('\nDIGITE UMA LETRA: ').lower()
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

	if letraEscolhida not in palavraEscolhida:
		ganhou -=1
		if ganhou == 0:
			print('Voce perdeu')
			break

	if '_ ' not in letraAdvinhada:
		ganhou = 0
		print('ganhou')
		break

	print(f'Voce tem {ganhou} chances')

	print(' '.join(letraAdvinhada))
