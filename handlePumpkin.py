import moveTo
import handle

def farmIt(pumpkinField):
    for x in pumpkinField:
        for y in pumpkinField[x]:
            moveTo.position(y, x)
            harvest()
            return

def replant(pumpkinField):
    newField = {}
    for x in pumpkinField:
        for y in pumpkinField[x]:
            moveTo.position(y, x)
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
                handle.water()
                if x not in newField:
                    newField[x] = []
                newField[x].append(y)
            elif not can_harvest():
                if x not in newField:
                    newField[x] = []
                newField[x].append(y)
    return newField

def handlePumpkinField(pumpkinField):
    replanted = {}
    # check all pumpkins and replant them (until all are not dead and farmable)
    field = replant(pumpkinField)
    while (field != {}):
        field = replant(field)
    

    # farm the one
    farmIt(pumpkinField)
    do_a_flip()

    # replant all
    replant(pumpkinField)
