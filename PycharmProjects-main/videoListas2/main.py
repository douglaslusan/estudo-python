# pessoas = [['aline', 37], ['douglas', 42], ['raziel', 6]]
#
# for i in pessoas:
# 	print(f'{i[0]} tem {i[1]} anos de idade')
#
# pessoa = list()
# dados = list()
#
# for i in range(0,3):
# 	dados.append(str(input('Nome: ')))
# 	dados.append(str(input('Idade: ')))
# 	pessoa.append(dados[:])
# 	dados.clear()
#
# for v in pessoa:
# 	print(v)

def somar(*args):
	soma = 0
	for i in range(0, len(args)):
		soma += args[i]
	return soma

print(somar(5,4,6,8,2))