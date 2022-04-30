lista = ('Pão', 1.5, 'Presunto', 14.00, 'Queijo', 20.00, 'Maionese', 6.00, 'Salame', 32.0)

print("-"*30)
print(f'{"listagem de preços":^30}')
print("-"*30)
for i in range(0,len(lista),2):
    print(f'{lista[i]:.<20} R$ {lista[i+1]:5.2f}')
