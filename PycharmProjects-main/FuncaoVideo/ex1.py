def area(c, l):
	a = c * l
	print(f'a area total {a:.2f}m²')


def linha(n):
	print('-'*n)


l = float(input('digite a largura: '))
c = float(input('digite o comprimento: '))

linha(30)
area(c, l)
