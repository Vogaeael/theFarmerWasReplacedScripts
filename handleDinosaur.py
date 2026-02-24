import hat

def createDirectionOrder() -> list[Direction]:
    directionOrder = []
    directionOrder.append(North)
    for _ in range((get_world_size() / 2) - 1):
        for _ in range(get_world_size() - 2):
            directionOrder.append(North)
        directionOrder.append(East)
        for _ in range(get_world_size() - 2):
            directionOrder.append(South)
        directionOrder.append(East)
    for _ in range(get_world_size() - 2):
        directionOrder.append(North)
    directionOrder.append(East)
    for _ in range(get_world_size() - 1):
        directionOrder.append(South)
    for _ in range(get_world_size() - 1):
        directionOrder.append(West)
    
    return directionOrder

def handleDinosaur() -> None:
    clear()
    change_hat(Hats.Dinosaur_Hat)
    directionOrder = createDirectionOrder()
    i = 0
    currentDirection = directionOrder[i]
    while can_move(currentDirection):
        move(currentDirection)
        i = i + 1
        i = i % len(directionOrder)
        currentDirection = directionOrder[i]
    hat.randomHat()
