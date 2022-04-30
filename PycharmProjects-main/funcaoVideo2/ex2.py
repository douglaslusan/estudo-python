def fatorial(num=1, show = False):
	'''

	:param num: digite um numero para calcular o fatorial
	:param show: FALSE para mostrar somente resultado ou TRUE para mostrar o calculo
	:return: valor
	'''
	f = 1
	for c in range(num, 0, -1):
		if show:
			print(c, end='')
			if c > 1:
				print(f' x ', end='')
			else:
				print(' = ',end='')
		f *= c
	return f


print(fatorial(5, True))
