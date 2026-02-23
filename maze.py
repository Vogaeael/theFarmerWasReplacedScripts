
def getSideDict() -> dict[str, dict[Direction, Direction]]:
    return {
        "right": {
            North: East,
            East: South,
            South: West,
            West: North,
        },
        "left": {
            North: West,
            West: South,
            South: East,
            East: North,
        },
        "opposite": {
            North: South,
            South: North,
            East: West,
            West: East,
        },
    }

def solveWithoutLoop() -> None:
    sideDict = getSideDict()
    lastDirection = North
    while get_entity_type() != Entities.Treasure:
        right = sideDict["right"][lastDirection]
        left = sideDict["left"][lastDirection]
        opposite = sideDict["opposite"][lastDirection]
        if can_move(right):
            move(right)
            lastDirection = right
        elif can_move(lastDirection):
            move(lastDirection)
        elif can_move(left):
            move(left)
            lastDirection = left
        elif can_move(opposite):
            move(opposite)
            lastDirection = opposite
        else:
            print("Error, no direction possitble")
    
    harvest()

def createAndSolveMaze() -> None:
    plant(Entities.Bush)
    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    use_item(Items.Weird_Substance, substance)

    solveWithoutLoop()
