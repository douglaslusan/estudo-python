
# filme1 = {'titulo': 'starwars', 'ano': 1977, 'diretor': 'Gerge Lucas'}
# filme2 = {'titulo': 'avengers', 'ano': 2012, 'diretor': 'Joss Whedon'}
# filme3 = {'titulo': 'matrix', 'ano': 1999, 'diretor': 'Watchosky'}
#
# filme1['like'] = 'sim'
# filme2['like'] = 'sim'
# filme3['like'] = 'sim'
#
# # print(filme1.keys())
# # print(filme1.values())
# # print(filme1.items())
# # print(f'O titulo {filme1["titulo"]} foi produzido por {filme1["diretor"]}')
#
# # for k, i in filme1.items():
# # 	print(f'{k} => {i}')
#
# locadora = list()
#
# locadora.append(filme1)
# locadora.append(filme2)
# locadora.append(filme3)
#
# # print(locadora[0]['diretor'])
# # print(locadora[1]['ano'])
# # print(locadora[2]['titulo'])
#
# for i, v in enumerate(locadora):
# 	print(i, v)

Estado = dict()
Brasil = list()

for i in range(0, 2):
	Estado['UF'] = str(input('Unidade Federativa '))
	Estado['sigla'] = str(input('sigla '))
	Brasil.append(Estado.copy())

for i in Brasil:
	for k, v in i.items():
		print(f'{k} {v}')