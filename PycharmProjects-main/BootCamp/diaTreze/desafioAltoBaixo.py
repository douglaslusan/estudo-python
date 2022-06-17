from Dados import datas
from random import choice
import logo

def get_random():
	return choice(datas)

def get_data(data):
	name = data['name']
	description = data['description']
	country = data['country']
	return f'{name} a {description} from: {country}'

def check(guess, a_follower, b_follower):
	if a_follower > b_follower:
		return guess == 'A'
	else:
		return guess == 'B'

def game():
	print(logo.logo)
	score = 0
	game_continue = True
	account_a = get_random()
	account_b = get_random()

	while game_continue:
		account_a = account_b
		account_b = get_random()

		while account_a == account_b:
			account_b = get_random()
		print(f'Compare A: {get_data(account_a)}')
		print(logo.vs)
		print(f'Compare B: {get_data(account_b)}')

		guess = input('Quem é o mais Popular? "A" ou "B"? ').upper()

		a_follower_count = account_a['follower_count']
		b_follower_count = account_b['follower_count']

		is_correct = check(guess, a_follower_count, b_follower_count)

		if is_correct:
			score += 1
			print(f'Voce Acertou! seu Score {score}')
		else:
			game_continue = False
			print(f'Me desculpe, Voce Errou! Pontos Final {score}')


game()


