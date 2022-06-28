from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput('Corrida', 'aposte nao cor [blue, red, green, purple]')
colors = ['blue', 'red', 'green', 'purple']
y_position = [80, 60, 40, 20]
all_turtle = []

finish = True
for turtle_index in range(0, 4):
	new_turtle = Turtle(shape='turtle')
	new_turtle.color(colors[turtle_index])
	new_turtle.penup()
	new_turtle.setposition(x=-200, y=y_position[turtle_index])
	all_turtle.append(new_turtle)

while finish:
	for turtle in all_turtle:
		n = randint(0, 10)
		turtle.forward(n)
		if turtle.xcor() > 210:
			winner = turtle.pencolor()
			finish = False
			if winner == bet:
				print(f'a tartaruga {turtle.pencolor()} venceu, Voce Ganhou')
			else:
				print(f'a tartaruga {turtle.pencolor()} venceu, Voce Perdeu')


# def move_fd():
# 	bob.fd(10)
#
#
# def move_bk():
# 	bob.bk(10)
#
#
# def move_lt():
# 	bob.lt(10)
#
#
# def move_rt():
# 	bob.rt(10)
#
#
# def clear():
# 	bob.reset()
#
#
# screen.listen()
# screen.onkey(move_fd, "w")
# screen.onkey(move_bk, "s")
# screen.onkey(move_lt, "a")
# screen.onkey(move_rt, "d")
# screen.onkey(clear, "c")

screen.exitonclick()
