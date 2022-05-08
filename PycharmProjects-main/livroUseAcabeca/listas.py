frase = "don't panic!"
lista = list(frase)
print('\033[1;96m',frase, '\033[0;0m')
print(lista)
# mudar o "don't panic!" para "on tap" usando somente metodos de lista

for i in range(4): #remove os 4 ultimos da lista
	lista.pop()

lista.pop(0) # Remove o primeiro
lista.remove("'") # Remove o "'"
lista.extend([lista.pop(),lista.pop()]) #remove primeiro o 'a' e adiciona, remove o 'p' e adiciona (invertendo os)
lista.insert(2, lista.pop(3)) # remove o espaco e o adiciona no indice 2

frase_nova = ''.join(lista) # transforma lista em string
print(lista)
print('\033[1;96m',frase_nova)
