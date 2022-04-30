
pessoa = list()
dados = list()
maior = menor = 0

while True:
	dados.append(str(input('Nome: ')))
	dados.append(float(input('Peso: ')))

	if len(pessoa) == 0:
		maior = menor = dados[1]
	else:
		if dados[1] > maior:
			maior = dados[1]
		if dados[1] < menor:
			menor = dados[1]

	pessoa.append(dados[:])
	dados.clear()
	opc = str(input('quer continuar? [s/n] ')).upper()
	if opc == 'N':
		break

print(f'cadastrado {len(pessoa)} pessoas')
print(f'o maior peso é {maior}Kg ',end=' - ')
for p in pessoa:
	if p[1] == maior:
		print(f'[{p[0]}], ', end='')
print()
print(f'menor peso é {menor}Kg ',end=' - ')

for p in pessoa:
	if p[1] == menor:
		print(f'[{p[0]}], ', end='')
