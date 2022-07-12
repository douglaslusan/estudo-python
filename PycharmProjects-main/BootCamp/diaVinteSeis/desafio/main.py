import pandas as pd

data = pd.read_csv('alphabet.csv')
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input('digite uma frase ou palavra para traduzir para o alfabeto fonetico ').upper()

word_list = [phonetic_dict[letter] for letter in word]

print(word_list)
