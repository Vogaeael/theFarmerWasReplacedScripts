import field2
import handle
import handleCactus
import handleDinosaur
import handlePumpkin
import handlePumpkinDivided
import handleSunflower
import handleSunflowerSuppo
import hat
import maze
import next

def runCactus(_: dict, values: dict, alreadyPlanted: bool) -> bool:
    handleCactus.handleFullCactusField(values["field"], alreadyPlanted)

    return False

def runCarrot(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    return handle.handleCompleteField(values["field"], alreadyPlanted, valuesDict)

def runGrass(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    return handle.handleCompleteField(values["field"], alreadyPlanted, valuesDict)

def runPumpkin(_: dict, __: dict, ___: bool) -> bool:
    handlePumpkinDivided.handleFullPmpkinFieldSeparated()
    #handlePumpkin.handleFullPumpkinField(values["field"], alreadyPlanted)

    return False

def runSunflower(_: dict, values: dict, alreadyPlanted: bool) -> bool:
    handleSunflowerSuppo.handleFullSunflowerField(alreadyPlanted)
    #handleSunflower.handleFullSunflowerField(values["field"], alreadyPlanted)

    return False

def runMaze(_: dict, __: dict, ___: bool) -> bool:
    maze.createAndSolveMaze()

    return False

def runTree(valuesDict: dict, values: dict, alreadyPlanted: bool) -> bool:
    return handle.handleCompleteField(values["field"], alreadyPlanted, valuesDict)

def runBone(_: dict, __: dict, ___: bool) -> bool:
    handleDinosaur.handleDinosaur()

    return False

def getValuesDict() -> dict:
    entityAttributes = {}

    entityAttributes[Items.Cactus] = {}
    entityAttributes[Items.Cactus]["field"] = field2.giantOnlyField(Entities.Cactus, True, False)
    entityAttributes[Items.Cactus]["function"] = runCactus

    entityAttributes[Items.Carrot] = {}
    entityAttributes[Items.Carrot]["field"] = field2.giantOnlyField(Entities.Carrot, True, False)
    entityAttributes[Items.Carrot]["function"] = runCarrot

    entityAttributes[Items.Hay] = {}
    entityAttributes[Items.Hay]["field"] = field2.giantOnlyField(Entities.Grass, False, False)
    entityAttributes[Items.Hay]["function"] = runGrass

    entityAttributes[Items.Pumpkin] = {}
    entityAttributes[Items.Pumpkin]["field"] = field2.giantOnlyField(Entities.Pumpkin, True, False)
    entityAttributes[Items.Pumpkin]["function"] = runPumpkin

    entityAttributes[Items.Power] = {}
    entityAttributes[Items.Power]["field"] = field2.giantOnlyField(Entities.Sunflower, True, False)
    entityAttributes[Items.Power]["function"] = runSunflower

    entityAttributes[Items.Gold] = {}
    entityAttributes[Items.Gold]["field"] = None
    entityAttributes[Items.Gold]["function"] = runMaze

    entityAttributes[Items.Wood] = {}
    entityAttributes[Items.Wood]["field"] = field2.giantDoubleSwitchField(Entities.Tree, True, False, Entities.Bush, True, False)
    entityAttributes[Items.Wood]["function"] = runTree

    entityAttributes[Items.Weird_Substance] = {}
    entityAttributes[Items.Weird_Substance]["field"] = field2.giantOnlyField(Entities.Grass, False, True)
    entityAttributes[Items.Weird_Substance]["function"] = runGrass

    entityAttributes[Items.Bone] = {}
    entityAttributes[Items.Bone]["field"] = field2.giantOnlyField(Entities.Grass, False, False)
    entityAttributes[Items.Bone]["function"] = runBone

    return entityAttributes

def getValues(values: dict, item: Item) -> dict:

    return values[item]

def run() -> None:
    hat.randomHat()
    itemValueDict = getValuesDict()
    alreadyPlanted = False
    while True:
        nextItem = next.next()
        if not alreadyPlanted:
            clear()
        itemValue = getValues(itemValueDict, nextItem)
        itemFunction = itemValue["function"]
        alreadyPlanted = itemFunction(itemValueDict, itemValue, alreadyPlanted)