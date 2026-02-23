import moveTo
import plantEntity
import field2

def farmIt(cactusField: Any) -> None:      # cactusField: field2.FieldList
    for x in cactusField:
        for y in cactusField[x]:
            moveTo.position(y, x)
            harvest()
            return

def sort(cactusField: Any, falseOrder: bool) -> None:      # cactusField: field2.FieldList
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

def handleCactusField(cactusField: Any, falseOrder = False) -> None:       # cactusField: field2.FieldList
    sort(cactusField, falseOrder)

    # farm the one
    farmIt(cactusField)
    do_a_flip()

    # replant all
    plantEntity.plantField(cactusField)

def handleFullCactusField(field: Any, alreadyPlanted: bool, falseOrder = False) -> Entity|None:    # field: field2.FieldList
    if not alreadyPlanted:
        plantEntity.plantField(field)
    sort(field, falseOrder)
    farmIt(field)
    do_a_flip()
