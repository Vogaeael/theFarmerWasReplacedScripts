import builtins

# The Game can't handle this type of dict, so I will only comment it and use Any as type
# FieldEntity = dict[
#     "entity": Entity,
#     "water": bool,
#     "fertilize": bool,
# ]
# FieldList = dict[
#     int,
#     dict[
#         int,
#         Any,    # FieldEntity
#     ],
# ]

def getSpecificTypeField(type: Entity, field: dict) -> Any:   # field: FieldList) -> FieldList
    typeField = {}
    for x in field:
        for y in field[x]:
            if field[x][y]["entity"] == type:
                if x not in typeField:
                    typeField[x] = {}
                typeField[x][y] = {}
                typeField[x][y]["entity"] = type
                typeField[x][y]["water"] = field[x][y]["water"]
                typeField[x][y]["fertilize"] = field[x][y]["fertilize"]
    return typeField

def getArrayObjects(
        num: int,
        entity: Entity,
        water: bool = False,
        fertilize: bool = False
        ) -> dict[Any]:     # -> list[FieldEntity]
    objects = {}
    for i in range(num):
        objects[i] = {"entity": entity, "fertilize": fertilize, "water": water}
    return objects

def getArrayDoubleSwitchObjects(
        num: int,
        entityFirst: Entity,
        waterFirst: bool,
        fertilizeFirst: bool,
        entitySecond: Entity,
        waterSecond: bool,
        fertilizeSecond: bool
        ) -> dict[Any]:     # -> list[FieldEntity]
    objects = {}
    for i in range(num):
        if i % 2:
            objects[i] = {"entity": entitySecond, "fertilize": fertilizeSecond, "water": waterSecond}
        else:
            objects[i] = {"entity": entityFirst, "fertilize": fertilizeFirst, "water": waterFirst}
    
    return objects

def mergeDictionaries(dicts: list[dict]) -> dict:
    newDict = {}
    i = 0
    for current in dicts:
        for j in current:
            newDict[i] = current[j]
            i = i + 1
    
    return newDict

# get and array of arrays
def field() -> dict[dict[Any]]:     # -> list[list[FieldEntity]]
    fieldSize = get_world_size()
    objectDict = {}
    if 8 == fieldSize:
        # 1
        objectDict[0] = getArrayObjects(8, Entities.Grass)
        # 2
        objectDict[1] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayDoubleSwitchObjects(6, Entities.Tree, True, False, Entities.Carrot, True, False),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 3
        objectDict[2] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(4, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
            ))
        )
        # 4
        objectDict[3] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(4, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
            ))
        )
        # 5
        objectDict[4] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(4, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 6
        objectDict[5] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(4, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 7
        objectDict[6] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayDoubleSwitchObjects(6, Entities.Carrot, True, False, Entities.Tree, True, False),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 8
        objectDict[7] = getArrayObjects(8, Entities.Grass)
        
        return objectDict
    if 12 == fieldSize:
        # 1
        objectDict[0] = getArrayObjects(12, Entities.Grass)
        # 2
        objectDict[1] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(10, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 3
        objectDict[2] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(8, Entities.Tree, True, False, Entities.Grass, False, False),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 4
        objectDict[3] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 5
        objectDict[4] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 6
        objectDict[5] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 7
        objectDict[6] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 8
        objectDict[7] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 9
        objectDict[8] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 10
        objectDict[9] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(8, Entities.Grass, False, False, Entities.Tree, True, False),
                getArrayObjects(1, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 11
        objectDict[10] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(10, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass)
            ))
        )
        # 12
        objectDict[11] = getArrayObjects(12, Entities.Grass)
        
        return objectDict
    if 16 == fieldSize:
        # 1
        objectDict[0] = getArrayObjects(16, Entities.Grass)
        # 2
        objectDict[1] = getArrayObjects(16, Entities.Grass)
        # 3
        objectDict[2] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(12, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 4
        objectDict[3] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(12, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 5
        objectDict[4] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(8, Entities.Tree, True, False, Entities.Grass, False, False),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 6
        objectDict[5] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 7
        objectDict[6] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 8
        objectDict[7] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 9
        objectDict[8] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 10
        objectDict[9] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 11
        objectDict[10] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(6, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 12
        objectDict[11] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(8, Entities.Grass, False, False, Entities.Tree, True, False),
                getArrayObjects(2, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 13
        objectDict[12] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(12, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 14
        objectDict[13] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(12, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 15
        objectDict[14] = getArrayObjects(16, Entities.Grass)
        # 16
        objectDict[15] = getArrayObjects(16, Entities.Grass)

        return objectDict
    if 22 == fieldSize:
        # 1
        objectDict[0] = getArrayObjects(22, Entities.Grass)
        # 2
        objectDict[1] = mergeDictionaries(
            list((
                getArrayObjects(5, Entities.Grass),
                getArrayObjects(12, Entities.Sunflower, True),
                getArrayObjects(5, Entities.Grass)
            ))
        )
        # 3
        objectDict[2] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(12, Entities.Sunflower, True),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 4
        objectDict[3] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(18, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 5
        objectDict[4] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(18, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 6
        objectDict[5] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(12, Entities.Tree, True, False, Entities.Grass, False, False),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 7
        objectDict[6] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(12, Entities.Grass, False, False, Entities.Tree, True, False),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 8
        objectDict[7] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 9
        objectDict[8] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 10
        objectDict[9] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 11
        objectDict[10] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 12
        objectDict[11] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 13
        objectDict[12] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 14
        objectDict[13] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 15
        objectDict[14] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(8, Entities.Pumpkin, True),
                getArrayObjects(1, Entities.Grass),
                getArrayObjects(1, Entities.Tree, True),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 16
        objectDict[15] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(12, Entities.Tree, True, False, Entities.Grass, False, False),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 17
        objectDict[16] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayDoubleSwitchObjects(12, Entities.Grass, False, False, Entities.Tree, True, False),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 18
        objectDict[17] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(18, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 19
        objectDict[18] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(18, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 20
        objectDict[19] = mergeDictionaries(
            list((
                getArrayObjects(2, Entities.Grass),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(12, Entities.Cactus, True),
                getArrayObjects(3, Entities.Carrot, True),
                getArrayObjects(2, Entities.Grass)
            ))
        )
        # 21
        objectDict[20] = mergeDictionaries(
            list((
                getArrayObjects(5, Entities.Grass),
                getArrayObjects(12, Entities.Cactus, True),
                getArrayObjects(5, Entities.Grass)
            ))
        )
        # 22
        objectDict[21] = mergeDictionaries(
            list((
                getArrayObjects(21, Entities.Grass),
                getArrayObjects(1, Entities.Grass, False, True)
            ))
        )

        return objectDict
    if 32 == fieldSize:
        # 1
        objectDict[0] = getArrayObjects(32, Entities.Grass)
        # 2
        objectDict[1] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass, False, True),
                getArrayObjects(30, Entities.Grass),
                getArrayObjects(1, Entities.Grass, False, True)
            ))
        )
        # 3
        objectDict[2] = getArrayObjects(32, Entities.Grass)
        # 4
        objectDict[3] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass, False, True),
                getArrayObjects(30, Entities.Grass),
                getArrayObjects(1, Entities.Grass, False, True)
            ))
        )
        # 5
        objectDict[4] = getArrayObjects(32, Entities.Grass)
        # 6
        objectDict[5] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Grass, False, True),
                getArrayObjects(30, Entities.Grass),
                getArrayObjects(1, Entities.Grass, False, True)
            ))
        )
        # 7
        objectDict[6] = getArrayObjects(32, Entities.Carrot, True)
        # 8
        objectDict[7] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Carrot, True, True),
                getArrayObjects(30, Entities.Carrot, True),
                getArrayObjects(1, Entities.Carrot, True, True)
            ))
        )
        # 9
        objectDict[8] = getArrayObjects(32, Entities.Carrot, True)
        # 10
        objectDict[9] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Carrot, True, True),
                getArrayObjects(30, Entities.Carrot, True),
                getArrayObjects(1, Entities.Carrot, True, True)
            ))
        )
        # 11
        objectDict[10] = getArrayObjects(32, Entities.Carrot, True)
        # 12
        objectDict[11] = mergeDictionaries(
            list((
                getArrayObjects(1, Entities.Carrot, True, True),
                getArrayObjects(30, Entities.Carrot, True),
                getArrayObjects(1, Entities.Carrot, True, True)
            ))
        )
        # 13
        objectDict[12] = getArrayDoubleSwitchObjects(32, Entities.Tree, True, False, Entities.Grass, False, False)
        # 14
        objectDict[13] = getArrayDoubleSwitchObjects(32, Entities.Grass, False, False, Entities.Tree, True, False)
        # 15
        objectDict[14] = getArrayDoubleSwitchObjects(32, Entities.Tree, True, False, Entities.Grass, False, False)
        # 16
        objectDict[15] = getArrayDoubleSwitchObjects(32, Entities.Grass, False, False, Entities.Tree, True, False)
        # 17
        objectDict[16] = getArrayDoubleSwitchObjects(32, Entities.Tree, True, False, Entities.Carrot, True, False)
        # 18
        objectDict[17] = getArrayDoubleSwitchObjects(32, Entities.Carrot, True, False, Entities.Tree, True, False)
        # 19
        objectDict[18] = getArrayDoubleSwitchObjects(32, Entities.Tree, True, False, Entities.Carrot, True, False)
        # 20
        objectDict[19] = getArrayDoubleSwitchObjects(32, Entities.Carrot, True, False, Entities.Tree, True, False)
        # 21
        objectDict[20] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 22
        objectDict[21] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 23
        objectDict[22] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 24
        objectDict[23] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 25
        objectDict[24] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 26
        objectDict[25] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 27
        objectDict[26] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 28
        objectDict[27] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 29
        objectDict[28] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 30
        objectDict[29] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 31
        objectDict[30] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )
        # 32
        objectDict[31] = mergeDictionaries(
            list((
                getArrayObjects(12, Entities.Pumpkin, True),
                getArrayObjects(10, Entities.Cactus, True),
                getArrayObjects(10, Entities.Sunflower, True)
            ))
        )

        return objectDict

def giantOnlyField(type: Entity, water: bool, fertilize: bool) -> dict[dict[Any]]:        # -> dict[dict[FieldEntity]]
    object = {}
    for i in range(get_world_size()):
        object[i] = getArrayObjects(get_world_size(), type, water, fertilize)

    return object

def giantDoubleSwitchField(
        mainType: Entity,
        mainWater: bool,
        mainFertilize: bool,
        secondType: Entity,
        secondWater: bool,
        secondFertilize: bool
    ) -> dict[dict[Any]]:        # -> dict[dict[FieldEntity]]
    objects = {}
    for i in range(get_world_size()):
        if i % 2:
            objects[i] = getArrayDoubleSwitchObjects(
                get_world_size(),
                mainType,
                mainWater,
                mainFertilize,
                secondType,
                secondWater,
                secondFertilize
            )
        else:
            objects[i] = getArrayDoubleSwitchObjects(
                get_world_size(),
                secondType,
                secondWater,
                secondFertilize,
                mainType,
                mainWater,
                mainFertilize
            )

    return objects
