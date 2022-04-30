jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome: '))
partidas = int(input('partidas jogadas: '))
total = 0

for i in range(0, partidas):
	gols.append(int(input(f'quantos gols fez na partida {i+1}: ')))

for i in gols:
	total += i

jogador['gols'] = gols[:]
jogador['total'] = total


for k, v in jogador.items():
	print(f'{k}: {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(jogador['gols']):
	print(f'Na partida {i+1}, fez {v} GOLS')
print(f'Com um total de {jogador["total"]} gols')
