
nome = []
idade = []

resposta = 's'

while resposta == 's':
    nome.append(input('Nome: '))
    idade.append(int(input('Idade: ')))
    resposta = input('digite s para continuar ')

resposta = 's'

while resposta == 's':
    busca = input('digite o nome para bucar: ')
    for indice in range(0, len(nome)):
        if busca == nome[indice]:
            print('Nome: ', nome[indice])
            print('idade: ', idade[indice])
    resposta = input('digite s para buscar outro nome ')



print('fim do programa')

