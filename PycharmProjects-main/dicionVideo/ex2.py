from random import randint
from time import sleep
from operator import itemgetter


jogo = {'DOUGLAS': randint(1, 6),
		'RAZIEL': randint(1, 6),
		'ALINE': randint(1, 6),
		'AIRAM': randint(1, 6)}
ranking = list()

print('VALORES SORTEADOS:')

for k, v in jogo.items():
	print(f'O {k} jogou {v} no dado')
	sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('EM ORDEM DO MAIOR PARA MENOR')

for i, v in enumerate(ranking):
	print(f'O {i+1}º LUGAR foi {v[0]} fez {v[1]} pontos')
