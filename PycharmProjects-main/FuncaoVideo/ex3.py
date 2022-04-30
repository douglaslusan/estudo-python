from time import sleep

def contador(i, f, p):
	print(f'Contagem de {i} ate {f} de {p} em {p}')
	print("_"*30)
	if i < f:
		cont = i
		while cont <= f:
			print(f'{cont} ', end='')
			sleep(0.2)
			cont += p
		print('FIM')
	else:
		cont = i
		while cont >= f:
			print(f'{cont} ', end='')
			sleep(0.2)
			cont -= p
		print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)

print('agora sua vez de contar')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
contador(inicio, fim, passo)
