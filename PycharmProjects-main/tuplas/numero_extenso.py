n = ('Zero', 'Um', 'Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze',
     'Treze','Quatorze','Quinze','Dezesseis', 'Dezesete','Dezoito', 'Dezenove','Vinte')
escolha = 0

while escolha > -1:
    escolha = int(input('Digite um numero de zero a vinte ou para encerrar digite um numero negativo: '))
    if escolha < 21:
        print(n[escolha])
    else:
        print('numero invalido')
