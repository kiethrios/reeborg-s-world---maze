def turn_right():
    for i in range(0,3):
        turn_left()

def goal():
    while front_is_clear():
        move()
    
    turn_left()
        
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
goal()
