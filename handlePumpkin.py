import field2
import moveTo
import plantEntity

def farmIt(pumpkinField: Any) -> None:     # pumpkinField: field2.FieldList
    for x in pumpkinField:
        for y in pumpkinField[x]:
            moveTo.position(y, x)
            harvest()
            return

def replantWithSupportDrone() -> None:
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            moveTo.position(y, x)
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() != Entities.Pumpkin:
                plant(Entities.Pumpkin)
                plantEntity.water()

def replant(pumpkinField: Any, completeField: bool = False) -> Any:    # pumpkinField: field2.FieldList) -> field2.FieldList
    separator = get_world_size() / max_drones()
    newField = {}
    i = 0
    for x in pumpkinField:
        i = i + 1
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
        if i % separator == 0:
            if max_drones() > num_drones():
                spawn_drone(replantWithSupportDrone)
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
        plantEntity.plantField(field, replantWithSupportDrone)
    
    # check all pumpkins and replant them (until all are not dead and farmable)
    field = replant(field, True)
    while (field != {}):
        field = replant(field, True)

    # farm the one
    farmIt(field)
    do_a_flip()