def virarDireita():
	turn_left()
	turn_left()
	turn_left()


def pula():
	turn_left()
	while wall_on_right():
		move()
	virarDireita()
	move()
	virarDireita()
	while front_is_clear():
		move()
	turn_left()


while not at_goal():
	if front_is_clear():
		move()
	else:
		pula()
