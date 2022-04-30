pessoas = dict()
cadastro = list()

opc = 'S'
somaIdade = media = 0

while opc == 'S':
	pessoas.clear()
	pessoas['nome'] = str(input('Nome: ')).capitalize()
	while True:
		pessoas['sexo'] = str(input('Sexo: [M/F]: ')).upper()
		if pessoas['sexo'] in 'MF':
			break
		print('digite somente m ou f')
	pessoas['idade'] = int(input('Idade: '))
	somaIdade += pessoas['idade']
	cadastro.append(pessoas.copy())


	while True:
		opc = input('Quer continuar? [s/n] ').upper()[0]
		if opc in 'SN':
			break
		print('digite somente "S" ou "N" ')
	if opc == 'N':
		break
media = somaIdade / len(cadastro)



print('-='*20)
for i in cadastro:
	print(f'{i}')

print(f'foram cadastradas {len(cadastro)} pessoas')
print(f'A media de idade é de {media} anos')
print('As mulheres do grupo sao:')
for i in cadastro:
	if i['sexo'] == 'F':
		print(i['nome'])

for p in cadastro:
	if p['idade'] >= media:
		print(f'{p["nome"]} tem idade acima da media com {p["idade"]} anos ')
