import field2
import moveTo
import plantEntity

def farmIt(sortedField: dict[int, list[int, list[str, Entity]]]) -> None:
    lastHighest = 99
    keys = []
    for _ in range(len(sortedField)):
        highest = -1
        for key in sortedField:
            if key > highest and key < lastHighest:
                highest = key
        keys.append(highest)
        lastHighest = highest
        
    for key in keys:
        for pos in sortedField[key]:
            moveTo.position(pos["y"], pos["x"])
            harvest()

def determineFlowerSizes(sunflowerField: Any) -> dict[int, dict[str, int]]:        # sunflowerField: field2.FieldList
    sortedField = {}
    for x in sunflowerField:
        for y in sunflowerField[x]:
            moveTo.position(y, x)
            size = measure()
            if size != None:
                if size not in sortedField:
                    sortedField[size] = []
                sortedField[size].append({"x": x, "y": y})
    return sortedField


def handleSunflowerField(sunflowerField: Any) -> None:     # sunflowerField: field2.FieldList
    # getfield
    sortedField = determineFlowerSizes(sunflowerField)

    # farm it in order
    farmIt(sortedField)
    do_a_flip()

    # replant all
    plantEntity.plantField(sunflowerField)

def handleFullSunflowerField(sunflowerField: Any, alreadyPlanted: bool) -> None:    # sunflowerField: field2.FieldList
    if not alreadyPlanted:
        plantEntity.plantField(sunflowerField)
    
    # getfield
    sortedField = determineFlowerSizes(sunflowerField)

    # farm it in order
    farmIt(sortedField)
    do_a_flip()
