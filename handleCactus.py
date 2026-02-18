import moveTo

def farmIt(cactusField: dict[int, list[int, list[str, Entity]]]) -> None:
    for x in cactusField:
        for y in cactusField[x]:
            moveTo.position(y, x)
            harvest()
            return

def replant(cactusField: dict[int, list[int, list[str, Entity]]]) -> None:
    for x in cactusField:
        for y in cactusField[x]:
            moveTo.position(y, x)
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Cactus)

def sort(
        cactusField: dict[int, list[int, list[str, Entity]]],
        falseOrder: bool) -> None:
    didSwap = True
    while didSwap:
        didSwap = False
        for x in cactusField:
            for y in cactusField[x]:
                moveTo.position(y, x)
                if (x + 1) in cactusField and y in cactusField[x + 1]:
                    currentSize = measure()
                    northSize = measure(North)
                    if northSize < currentSize and not falseOrder:
                        swap(North)
                        didSwap = True
                    elif northSize > currentSize and falseOrder:
                        swap(North)
                        didSwap = True
                if (x - 1) in cactusField and y in cactusField[x - 1]:
                    currentSize = measure()
                    southSize = measure(South)
                    if southSize > currentSize and not falseOrder:
                        swap(South)
                        didSwap = True
                    elif southSize < currentSize and falseOrder:
                        swap(South)
                        didSwap = True
                if (y + 1) in cactusField[x]:
                    currentSize = measure()
                    eastSize = measure(East)
                    if eastSize < currentSize and not falseOrder:
                        swap(East)
                        didSwap = True
                    elif eastSize > currentSize and falseOrder:
                        swap(East)
                        didSwap = True
                if (y - 1) in cactusField[x]:
                    currentSize = measure()
                    westSize = measure(West)
                    if westSize > currentSize and not falseOrder:
                        swap(West)
                        didSwap = True
                    if westSize < currentSize and falseOrder:
                        swap(West)
                        didSwap = True
                    


def handleCactusField(
        cactusField: dict[int, list[int, list[str, Entity]]],
        falseOrder = False
        ) -> None:
    sort(cactusField, falseOrder)

    # farm the one
    farmIt(cactusField)
    do_a_flip()

    # replant all
    replant(cactusField)
