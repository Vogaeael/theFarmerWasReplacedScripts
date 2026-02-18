def getArrayObjects(num: int, entity: Entity, water: bool = False, fertilize: bool = False) -> list[dict[str, Entity|bool]]:
    array = []
    for i in range(num):
        array.append({"entity": entity, "fertilize": fertilize, "water": water})
    return array

def getArrayDoubleSwitchObjects(
        num: int,
        entityFirst: Entity,
        waterFirst: bool,
        fertilizeFirst: bool,
        entitySecond: Entity,
        waterSecond: bool,
        fertilizeSecond: bool
        ) -> list[dict[str, Entity|bool]]:
    array = []
    for i in range(num):
        if i % 0:
            array.append({"entity": entitySecond, "fertilize": fertilizeSecond, "water": waterSecond})
        else:
            array.append({"entity": entityFirst, "fertilize": fertilizeFirst, "water": waterFirst})
    return array

# get and array of arrays
def field() -> list[list[dict[str, Entity|bool]]]:
    fieldSize = get_world_size()
    array = []
    if 8 == fieldSize:
        # 1
        array.append(getArrayObjects(8, Entities.Grass))
        # 2
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayDoubleSwitchObjects(6, Entities.Tree, True, False, Entities.Carrot, True, False)
            + getArrayObjects(1, Entities.Grass))
        # 3
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(4, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 4
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(4, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 5
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(4, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 6
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(4, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 7
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayDoubleSwitchObjects(6, Entities.Carrot, True, False, Entities.Tree, True, False)
            + getArrayObjects(1, Entities.Grass)
        )
        # 8
        array.append(
            getArrayObjects(8, Entities.Grass)
        )
        return array
    if 12 == fieldSize:
        # 1
        array.append(getArrayObjects(12, Entities.Grass))
        # 2
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(10, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 3
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(8, Entities.Tree, True, False, Entities.Grass, False, False)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 4
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 5
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 6
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 7
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 8
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 9
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 10
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(8, Entities.Grass, False, False, Entities.Tree, True, False)
            + getArrayObjects(1, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 11
        array.append(
            getArrayObjects(1, Entities.Grass)
            + getArrayObjects(10, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
        )
        # 12
        array.append(
            getArrayObjects(12, Entities.Grass)
        )
        return array
    if 16 == fieldSize:
        # 1
        array.append(
            getArrayObjects(16, Entities.Grass)
        )
        # 2
        array.append(
            getArrayObjects(16, Entities.Grass)
        )
        # 3
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(12, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 4
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(12, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 5
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(8, Entities.Tree, True, False, Entities.Grass, False, False)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 6
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 7
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 8
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 9
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 10
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 11
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(6, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 12
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(8, Entities.Grass, False, False, Entities.Tree, True, False)
            + getArrayObjects(2, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 13
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(12, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 14
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(12, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 15
        array.append(
            getArrayObjects(16, Entities.Grass)
        )
        # 16
        array.append(
            getArrayObjects(16, Entities.Grass)
        )
        return array
    if 22 == fieldSize:
        # 1
        array.append(
            getArrayObjects(22, Entities.Grass)
        )
        # 2
        array.append(
            getArrayObjects(22, Entities.Grass)
        )
        # 3
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(18, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 4
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(18, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 5
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(18, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 6
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(12, Entities.Tree, True, False, Entities.Grass, False, False)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 7
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(12, Entities.Grass, False, False, Entities.Tree, True, False)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 8
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 9
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 10
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 11
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 12
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 13
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 14
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 15
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(8, Entities.Pumpkin, True)
            + getArrayObjects(1, Entities.Grass)
            + getArrayObjects(1, Entities.Tree, True)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 16
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(12, Entities.Tree, True, False, Entities.Grass, False, False)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 17
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayDoubleSwitchObjects(12, Entities.Grass, False, False, Entities.Tree, True, False)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 18
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(18, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 19
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(18, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 20
        array.append(
            getArrayObjects(2, Entities.Grass)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(12, Entities.Cactus, True)
            + getArrayObjects(3, Entities.Carrot, True)
            + getArrayObjects(2, Entities.Grass)
        )
        # 21
        array.append(
            getArrayObjects(5, Entities.Grass)
            + getArrayObjects(12, Entities.Cactus, True)
            + getArrayObjects(5, Entities.Grass)
        )
        # 22
        array.append(
            getArrayObjects(21, Entities.Grass)
            + getArrayObjects(1, Entities.Grass, False, True)
        )
        return array

def giantOnlyField(type: Entity) -> list[list[dict[str, Entity|bool]]]:
    array = []
    for i in range(32):
        array[i] = []
        for j in range(32):
            array[i][j] = {"entity": type, "fertilize": False, "water": True}
    return array
