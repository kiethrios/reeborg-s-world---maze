def turn_right():
    for i in range(0,3):
        turn_left()

def goal():
    while front_is_clear():
        move()
    
    turn_left()
        
    while not at_goal():
        if front_is_clear():
            move()
        elif right_is_clear():
            turn_right()
        else:
            turn_left()
goal()
