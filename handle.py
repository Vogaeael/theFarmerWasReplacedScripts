import entityGrid
import field2
import fullFieldSolution
import hat
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

def handleWithSupportDrone() -> None:
    hat.randomHat()
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            moveTo.position(y, x)
            entity = get_entity_type()
            if can_harvest():
                harvest()
                default = entityGrid.getDefaultToEntity(entity)
                plantEntity.plantEntity(entity, default["water"], default["fertilize"])

def handleCompleteField(field: Any, alreadyPlanted: bool, valuesDict: dict) -> bool:    # field: field2.FieldList
    #if not alreadyPlanted:
    #    plantEntity.plantField(field)
    
    nextEntity = next.next()
    nextField = fullFieldSolution.getValues(valuesDict, nextEntity)["field"]

    separator = get_world_size() / max_drones()
    i = 0
    for x in field:
        i = i + 1
        for y in field[x]:
            moveTo.position(y, x)
            if can_harvest():
                harvest()
            if None != nextField:
                nextFieldPosition = nextField[x][y]
                plantEntity.plantEntity(nextFieldPosition["entity"], nextFieldPosition["water"], nextFieldPosition["fertilize"])
        
        if x != 0 and i % separator == 0 and max_drones() > num_drones():
            spawn_drone(handleWithSupportDrone)

    return True
