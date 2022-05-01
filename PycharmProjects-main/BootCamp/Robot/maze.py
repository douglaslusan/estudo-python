def virarDireita():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            virarDireita()
    else:
        turn_left()
