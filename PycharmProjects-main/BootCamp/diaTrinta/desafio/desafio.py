import pandas as pd

data = pd.read_csv('alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# def phonetics():
# 	word = input('digite uma palavra para traduzir para o alfabeto fonetico ').upper()
# 	try:
# 		word_list = [phonetic_dict[letter] for letter in word]
# 	except:
# 		print('Digite somente LETRAS, Estupido')
# 		phonetics()
# 	else:
# 		return word_list
#
# print(phonetics())

while True:
	try:
		word = input('digite uma palavra para traduzir para o alfabeto fonetico ').upper()
		word_list = [phonetic_dict[letter] for letter in word]
	except:
		print('Digite somente LETRAS, Estupido')
	else:
		break

print(word_list)

# continua: desafio 29 melhorado
