frase = "don't panic!"
lista = list(frase)
print(frase)
print(lista)

# mudar o "don't panic!" para "on tap" usando somente metodos de lista

for i in range(4):
	lista.pop()
lista.pop(0)
lista.remove("'")
lista.extend([lista.pop(),lista.pop()])
lista.insert(2, lista.pop(3))

frase_nova = ''.join(lista)
print(lista)
print(frase_nova)
