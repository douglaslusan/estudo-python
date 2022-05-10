vogais = ['a','e','i','o','u']
found = {}

cont = 0
palavra = input('digite uma palavra ')
for i in sorted(palavra):
	cont += 1
	if i in vogais:
		found.setdefault(i, 0)
		found[i] += 1

print(found)
print(cont)
