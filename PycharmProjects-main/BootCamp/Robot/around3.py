def turn_right():
    for i in range(3):
        turn_left()
put()
turn_left()
move()
turn_right()
move()
move()
turn_right()
move()
turn_left()


while not object_here():
    if front_is_clear():
        move()
        if wall_in_front():
            turn_left()
        elif right_is_clear():
            turn_right()