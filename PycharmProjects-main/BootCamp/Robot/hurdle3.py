def virarDireita():
    turn_left()
    turn_left()
    turn_left()

def pula():
    turn_left()
    move()
    virarDireita()
    move()
    virarDireita()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:
        pula()