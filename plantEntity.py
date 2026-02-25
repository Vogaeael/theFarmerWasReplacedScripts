import entityGrid
import field2
import moveTo

def water() -> None:
    while 0.9 > get_water():
        use_item(Items.Water)

def fertilize() -> None:
    use_item(Items.Fertilizer)

def plantEntity(entity: Entity, withWater: bool, withFertilizer: bool) -> None:
    neededGroundType = entityGrid.getGroundToEntity(entity)
    if get_ground_type() != neededGroundType:
        till()
    plant(entity)

    if withWater:
        water()

    if withFertilizer:
        fertilize()

def plantField(field: Any, supportDrone: function = None) -> None:        # field: field2.FieldList
    i = 0
    separater = get_world_size() / max_drones()
    for x in field:
        i = i + 1
        for y in field[x]:
            moveTo.position(y, x)
            position = field[x][y]
            plantEntity(position["entity"], position["water"], position["fertilize"])
        if None != supportDrone:
            if i % separater == 0:
                if max_drones() > num_drones():
                    spawn_drone(supportDrone)
