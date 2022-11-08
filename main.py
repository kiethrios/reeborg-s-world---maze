def turn_right():
    for i in range(0,3):
        turn_left()

def face_north():
    while not is_facing_north():
        turn_left()

def goal():
    while not at_goal():
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
        else:
            turn_left()

face_north()
goal()
