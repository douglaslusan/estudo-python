def fatorial(num):
	f = 1
	for c in range(num, 0, -1):
		f *= c
	return f


n = int(input('digite um numero '))

print(fatorial(n))