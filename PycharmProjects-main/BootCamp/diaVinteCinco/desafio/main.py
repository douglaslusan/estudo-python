import turtle
import pandas as pd

# def pega_coord(x, y):
# 	print(f'{x},{y}')

screen = turtle.Screen()
screen.title('Estados Brasil')
image = 'brasil.gif'
screen.setup(800, 800)
screen.bgpic(image)
ponto = turtle.Turtle()
ponto.shape('circle')
ponto.penup()
ponto.hideturtle()
# screen.onscreenclick(pega_coord)

coord = pd.read_csv('coordenadas.csv')
fd = pd.DataFrame(coord)
cont = 0
completo = 26
acertos = []

while cont != completo:
	answer = screen.textinput(title=f'{cont}/{completo}', prompt='Qual o Estado que Falta?').lower()
	if answer == 'sair':
		estados_esquecidos = [estado for estado in fd.estados if estado not in acertos]
		estados_esquecidos_df = pd.DataFrame(estados_esquecidos)
		estados_esquecidos_df.to_csv('estados_esquecidos.csv')
		break
	for estado in fd.estado:
		if answer == estado:
			coord = fd[fd.estado == answer]
			ponto.goto(int(coord.x), int(coord.y))
			ponto.write(f'{answer.title()}', font=("Arial", 12, "bold"))
			acertos.append(answer)
			cont += 1
