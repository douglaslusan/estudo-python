
frase = input('digite uma frase ').lower()

palavraShift = [ord(asc) for asc in frase]

shift = int(input('digite quantas casas quer modificar as letras: '))

frasePronta = ''

for i in range(len(palavraShift)):
	if palavraShift[i] == 32:
		continue
	palavraShift[i] += shift
	if palavraShift[i] > 122:
		palavraShift[i] -= 26
	palavraCodificada = [chr(num) for num in palavraShift]
	frasePronta = ''.join(palavraCodificada)

print(frasePronta)
opcao = int(input('digite 1 para descodificar ou 0 para sair '))
shift = int(input('digite quantas casas quer modificar as letras: '))
if opcao == 1:
	for i in range(len(palavraShift)):
		if palavraShift[i] == 32:
			continue
		palavraShift[i] -= shift
		if palavraShift[i] < 97:
			palavraShift[i] += 26
		palavraCodificada = [chr(num) for num in palavraShift]
		frasePronta = ''.join(palavraCodificada)

	print(frasePronta)
else:
	print('FIM DO PROGRAMA')


