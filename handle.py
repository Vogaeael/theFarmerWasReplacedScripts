import entityGrid
import field2
import fullFieldSolution
import moveTo
import next
import plantEntity

def handle(entity: Any, farmSeparate: bool) -> None:     # entity: field2.FieldEntity
    if entity["water"]:
        plantEntity.water()

    if entity["fertilize"]:
        plantEntity.fertilize()

    # is skipable?
    if entity["entity"] in farmSeparate and farmSeparate[entity["entity"]]:
        # skip
        return

    # check costs
    cost = get_cost(entity["entity"])
    for item in cost:
        if num_items(item) < cost[item]:
            nextEntity = entityGrid.items()[item]
            handle(nextEntity)
            return

    if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
        harvest()

        neededGroundType = entityGrid.getGroundToEntity(entity["entity"])
        if get_ground_type() != neededGroundType:
            till()
        plant(entity["entity"])

def handleCompleteField(field: Any, alreadyPlanted: bool, valuesDict: dict) -> bool:    # field: field2.FieldList
    if not alreadyPlanted:
        plantEntity.plantField(field)
    
    nextEntity = next.next()
    nextField = fullFieldSolution.getValues(valuesDict, nextEntity)["field"]

    for x in field:
        for y in field[x]:
            moveTo.position(y, x)
            if can_harvest():
                harvest()
            if None != nextField:
                nextFieldPosition = nextField[x][y]
                plantEntity.plantEntity(nextFieldPosition["entity"], nextFieldPosition["water"], nextFieldPosition["fertilize"])

    return True
