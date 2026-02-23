import field2
import moveTo
import plantEntity

def farmIt(pumpkinField: Any) -> None:     # pumpkinField: field2.FieldList
    for x in pumpkinField:
        for y in pumpkinField[x]:
            moveTo.position(y, x)
            harvest()
            return

def replant(pumpkinField: Any) -> Any:    # pumpkinField: field2.FieldList) -> field2.FieldList
    newField = {}
    for x in pumpkinField:
        for y in pumpkinField[x]:
            moveTo.position(y, x)
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
                plantEntity.water()
                if x not in newField:
                    newField[x] = {}
                newField[x][y] = {}
                newField[x][y]["entity"] = pumpkinField[x][y]["entity"]
                newField[x][y]["water"] = pumpkinField[x][y]["water"]
                newField[x][y]["fertilize"] = pumpkinField[x][y]["fertilize"]
            elif not can_harvest():
                if x not in newField:
                    newField[x] = {}
                newField[x][y] = {}
                newField[x][y]["entity"] = pumpkinField[x][y]["entity"]
                newField[x][y]["water"] = pumpkinField[x][y]["water"]
                newField[x][y]["fertilize"] = pumpkinField[x][y]["fertilize"]
    return newField

def handlePumpkinField(pumpkinField: Any) -> None:     # pumpkinField: field2.FieldList
    # check all pumpkins and replant them (until all are not dead and farmable)
    field = replant(pumpkinField)
    while (field != {}):
        field = replant(field)

    # farm the one
    farmIt(pumpkinField)
    do_a_flip()

    # replant all
    replant(pumpkinField)

def handleFullPumpkinField(field: Any, alreadyPlanted: bool) -> None:      # field: field2.FieldList
    if not alreadyPlanted:
        plantEntity.plantField(field)
    
    # check all pumpkins and replant them (until all are not dead and farmable)
    field = replant(field)
    while (field != {}):
        field = replant(field)

    # farm the one
    farmIt(field)
    do_a_flip()