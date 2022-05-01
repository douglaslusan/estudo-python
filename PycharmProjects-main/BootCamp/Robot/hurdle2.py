def virarDireita():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    move()
    turn_left()
    move()
    virarDireita()
    move()
    virarDireita()
    move()
    turn_left()