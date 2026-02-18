def position(X: int, Y: int) -> None:
    max_value = get_world_size()
    
    # determine steps north and south
    currentY = get_pos_y()
    if Y == currentY:
        northSteps = 0
        southSteps = 0
    elif Y > currentY:
        northSteps = Y - currentY
        southSteps = currentY + max_value - Y
    else:
        northSteps = max_value - currentY + Y
        southSteps = currentY - Y
    
    # go steps north or south
    if northSteps < southSteps:
        for i in range(northSteps):
            move(North)
    else:
        for i in range(southSteps):
            move(South)
    
    # determine steps east and west
    currentX = get_pos_x()
    if X == currentX:
        eastSteps = 0
        westSteps = 0
    elif X > currentX:
        eastSteps = X - currentX
        westSteps = currentX + max_value - X
    else:
        eastSteps = max_value - currentX + X
        westSteps = currentX - X
    
    # go steps east or west
    if eastSteps < westSteps:
        for i in range(eastSteps):
            move(East)
    else:
        for i in range(westSteps):
            move(West)

def start() -> None:
    position(0,0)
