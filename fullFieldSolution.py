import field2
import handle
import handleCactus
import handlePumpkin
import handleSunflower
import maze
import next

def runCactus(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    handleCactus.handleFullCactusField(values["field"], alreadyPlanted)

    return False

def runCarrot(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    return handle.handleCompleteField(values["field"], alreadyPlanted, valuesDict)

def runGrass(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    return handle.handleCompleteField(values["field"], alreadyPlanted, valuesDict)

def runPumpkin(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    handlePumpkin.handleFullPumpkinField(values["field"], alreadyPlanted)

    return False

def runSunflower(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    handleSunflower.handleFullSunflowerField(values["field"], alreadyPlanted)

    return False

def runMaze(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    maze.createAndSolveMaze()

    return False

def runTree(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    return handle.handleCompleteField(values["field"], alreadyPlanted, valuesDict)

def getValuesDict() -> dict:
    entityAttributes = {}

    entityAttributes[Entities.Cactus] = {}
    entityAttributes[Entities.Cactus]["field"] = field2.giantOnlyField(Entities.Cactus, True, False)
    entityAttributes[Entities.Cactus]["function"] = runCactus

    entityAttributes[Entities.Carrot] = {}
    entityAttributes[Entities.Carrot]["field"] = field2.giantOnlyField(Entities.Carrot, True, False)
    entityAttributes[Entities.Carrot]["function"] = runCarrot

    entityAttributes[Entities.Grass] = {}
    entityAttributes[Entities.Grass]["field"] = field2.giantOnlyField(Entities.Grass, False, False)
    entityAttributes[Entities.Grass]["function"] = runGrass

    entityAttributes[Entities.Pumpkin] = {}
    entityAttributes[Entities.Pumpkin]["field"] = field2.giantOnlyField(Entities.Pumpkin, True, False)
    entityAttributes[Entities.Pumpkin]["function"] = runPumpkin

    entityAttributes[Entities.Sunflower] = {}
    entityAttributes[Entities.Sunflower]["field"] = field2.giantOnlyField(Entities.Sunflower, True, False)
    entityAttributes[Entities.Sunflower]["function"] = runSunflower

    entityAttributes[Entities.Treasure] = {}
    entityAttributes[Entities.Treasure]["field"] = None
    entityAttributes[Entities.Treasure]["function"] = runMaze

    entityAttributes[Entities.Tree] = {}
    entityAttributes[Entities.Tree]["field"] = field2.giantDoubleSwitchField(Entities.Tree, True, False, Entities.Bush, True, False)
    entityAttributes[Entities.Tree]["function"] = runTree

    return entityAttributes

def getValues(values: dict, entity: Entity) -> dict:

    return values[entity]

def run() -> None:
    entityValueDict = getValuesDict()
    alreadyPlanted = False
    while 1:
        nextEntity = next.next()
        if not alreadyPlanted:
            clear()
        entityValue = getValues(entityValueDict, nextEntity)
        entityFunction = entityValue["function"]
        alreadyPlanted = entityFunction(entityValueDict, entityValue, alreadyPlanted)