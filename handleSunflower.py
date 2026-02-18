import moveTo

def farmIt(sortedField: dict[int, list[int, list[str, Entity]]]) -> None:
    lastHighest = 99
    keys = []
    for i in range(len(sortedField)):
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

def replant(sunflowerField: dict[int, list[int, list[str, Entity]]]) -> None:
    for x in sunflowerField:
        for y in sunflowerField[x]:
            moveTo.position(y, x)
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Sunflower)

def determineFlowerSizes(sunflowerField: dict[int, list[int, list[str, Entity]]]) -> dict[int, dict[str, int]]:
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


def handleSunflowerField(sunflowerField: dict[int, list[int, list[str, Entity]]]) -> None:
    # getfield
    sortedField = determineFlowerSizes(sunflowerField)

    # farm the one
    farmIt(sortedField)
    do_a_flip()

    # replant all
    replant(sunflowerField)
