import entityGrid
import field2
import moveTo

def water() -> None:
    if 0 == get_water():
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

def plantField(field: Any) -> None:        # field: field2.FieldList
    for x in field:
        for y in field[x]:
            moveTo.position(y, x)
            position = field[x][y]
            plantEntity(position["entity"], position["water"], position["fertilize"])
