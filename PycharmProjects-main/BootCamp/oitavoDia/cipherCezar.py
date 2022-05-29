modo = input('digite [c] para criptografar ou [d] para descriptografar: ')
frase = input('digite uma frase ').lower()

palavraShift = [ord(asc) for asc in frase]

shift = int(input('digite quantas casas quer modificar as letras: '))

frasePronta = ''

if modo == 'c':
	for i in range(len(palavraShift)):
		if palavraShift[i] == 32:
			continue
		palavraShift[i] += shift
		if palavraShift[i] > 122:
			palavraShift[i] -= 26
		palavraCodificada = [chr(num) for num in palavraShift]
		frasePronta = ''.join(palavraCodificada)

	print(frasePronta)
else:
	for i in range(len(palavraShift)):
		if palavraShift[i] == 32:
			continue
		palavraShift[i] -= shift
		if palavraShift[i] < 97:
			palavraShift[i] += 26
		palavraCodificada = [chr(num) for num in palavraShift]
		frasePronta = ''.join(palavraCodificada)

	print(frasePronta)


