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
estudar = []


while cont != completo:
	answer = screen.textinput(title=f'{cont}/{completo}', prompt='Qual o Estado que Falta?').lower()
	if answer == 'sair':
		for estado in fd.estado:
			if estado not in acertos:
				estudar.append(estado)
		estudar_df = pd.DataFrame(estudar)
		estudar_df.to_csv('estudar.csv')
		break
	for estado in fd.estado:
		if answer == estado:
			coord = fd[fd.estado == answer]
			ponto.goto(int(coord.x), int(coord.y))
			ponto.write(f'{answer.title()}', font=("Arial", 12, "bold"))
			acertos.append(answer)
			cont += 1
