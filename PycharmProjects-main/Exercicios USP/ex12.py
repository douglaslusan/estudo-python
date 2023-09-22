import math

a = float(input("Entre com o numero para a equação: "))
b = float(input("Entre com o numero para a equação: "))
c = float(input("Entre com o numero para a equação: "))

Delta = b*b - 4*a*c

if Delta < 0:
    print("Não possui raízes reais")
elif Delta == 0:
    print("Apenas uma raiz")
    raiz = (-b + pow(Delta,1/2))/2*a
    print(f"A raiz é: x = {raiz}")
else:
    print("Duas raízes")
    raiz1 = (-b + pow(Delta,1/2))/2*a
    raiz2 = (-b - pow(Delta,1/2))/2*a
    print(f"x1 = {raiz1:.2f}, x2 = {raiz2:.2f}")
    print("as raízes da equação são", raiz1, "e", raiz2)