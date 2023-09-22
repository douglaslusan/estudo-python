x1 = int(input('digite o valor de x do primeiro ponto: '))
y1 = int(input('digite o valor de y do primeiro ponto: '))

x2 = int(input('digite o valor de x do segundo ponto: '))
y2 = int(input('digite o valor de y do segundo ponto: '))

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if distance >= 10:
    print("longe")
else:
    print("perto")