import random

n = random.randint(1, 100)

chance = 0

def lvl_choice(chance, lvl):
	if lvl == "hard":
		chance = 5
		return chance
	else:
		chance = 10
		return chance


lvl = input('Digite "easy" para Facil, "hard" para Díficil: ')

chance = lvl_choice(chance, lvl)

while chance:
	choice = int(input('Digite um numero para advinhar qual o numero o Computador pensou: '))

	if n == choice:
		print('Voce Acertou')
		print(n)
		exit()
	elif n > choice:
		print('sua escolha é pequena, escolha um numero maior\n')
		chance -= 1
		print(f'voce tem {chance} tentaivas')
	else:
		print('sua escolha é grande, escolha um menor\n')
		chance -= 1
		print(f'voce tem {chance} tentaivas')

print(f'acabou suas chances, FIM DO JOGO, o número correto era {n}')
