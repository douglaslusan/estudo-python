enemies = 1

def increase_enemies():
	global enemies
	enemies += 1
	print(f'Dentro da funcao: {enemies}')


increase_enemies()


print(f'fora da funcao {enemies}')

