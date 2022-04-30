jogador = dict()
gols = list()
classificacao = list()

while True:
	jogador.clear()
	gols.clear()
	jogador['nome'] = str(input('Nome: ')).capitalize()
	jogador['partidas'] = int(input('partidas jogadas: '))
	total = 0

	for i in range(0, jogador['partidas']):
		gols.append(int(input(f'quantos gols fez na partida {i+1}: ')))

	for i in gols:
		total += i

	jogador['gols'] = gols[:]
	jogador['total'] = total
	classificacao.append(jogador.copy())

	while True:
		opc = str(input('Quer continuar? S/N ')).upper()
		if opc in 'SN':
			break
		print('digite S ou N')
	if opc == 'N':
		break
print('-'*60)
print('Cod ',end='')
for i in jogador.keys():
	print(f'{i:<17}', end='')
print()
print('-='*30)

for k, v in enumerate(classificacao):
	print(f'{k:>2} ', end='')
	for d in v.values():
		print(f'{str(d):<19}', end='')
	print()
print('-='*30)

while True:
	busca = int(input('Mostrar dados de qual Jogador: digite numero n existente para terminar: '))
	if busca > len(classificacao):
		break
	else:
		print(f'LEVANTAMENTO DE DADOS DO JOGADOR {classificacao[busca]["nome"]}')
		for i, g in enumerate(classificacao[busca]["gols"]):
			print(f'	no jogo {i+1} fez {g} gols')
	print('-'*60)