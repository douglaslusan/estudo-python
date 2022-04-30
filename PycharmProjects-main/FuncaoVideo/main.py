def linha(n):
	print('-'*n)


def mensagem(msg):
	print(f'{msg}')


def soma(num):
	s = soma = 0
	while s < len(num):
		soma += num[s]
		s += 1
	print(soma)



# linha(50)
# mensagem('douglas')
# linha(50)

# numeros = list()
#
# for i in range(0,5):
# 	numeros.append(int(input('digite um numero ')))
#
#
# print(f'{numeros} = ', end='')
# soma(numeros)


