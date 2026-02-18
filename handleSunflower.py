import moveTo

def farmIt(sortedField):
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

def replant(sunflowerField):
    for x in sunflowerField:
        for y in sunflowerField[x]:
            moveTo.position(y, x)
            if get_ground_type() != Grounds.Soil:
                till()
            plant(Entities.Sunflower)

def determineFlowerSizes(sunflowerField):
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


def handleSunflowerField(sunflowerField):
    # getfield
    sortedField = determineFlowerSizes(sunflowerField)

    # farm the one
    farmIt(sortedField)
    do_a_flip()

    # replant all
    replant(sunflowerField)
