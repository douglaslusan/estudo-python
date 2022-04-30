def ficha(nome='desconhecido', gols=0):
	print(f'o jogador {nome} fez {gols} gols no campeonato')



nome = str(input('digite o nome: '))

gols = str(input('digite a quantidade de gols: '))
if gols.isnumeric():
	gols = int(gols)
else:
	gols = 0

if nome.strip() == '':
	ficha(gols = gols)
else:
	ficha(nome, gols)
