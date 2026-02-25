import hat
import moveTo
import plantEntity

def replantWithSupportDrone() -> None:
    hat.randomHat()
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            moveTo.position(y, x)
            currentEntity = get_entity_type()
            if currentEntity == Entities.Dead_Pumpkin:
                plantEntity.plantEntity(Entities.Pumpkin, True, False)

def getDividedField() -> list[dict[str, int]]:
    maxPumpkinSize = 6
    rest = get_world_size()
    sideFields = []
    nextFieldSize = min(maxPumpkinSize, rest)
    sideFields.append(nextFieldSize)
    rest = rest - nextFieldSize
    while rest > maxPumpkinSize + 1:        # 1 for the separator gras line
        rest = rest - 1
        rest = rest - maxPumpkinSize
        sideFields.append(maxPumpkinSize)
    
    for i in range (rest):
        i = i % len(sideFields)
        sideFields[i] = sideFields[i] + 1
    
    dividedFields = []
    currentX = 0
    for x in sideFields:
        currentY = 0
        for y in sideFields:
            dividedFields.append({
                "startX": currentX,
                "startY": currentY,
                "length": min(x, y),
            })
            currentY = currentY + y + 1     # 1 for the separator gras line
        currentX = currentX + x + 1     # 1 for the separator gras line

    return dividedFields

def findFreeField(dividedFields: list[dict[str, int]]) -> dict[str, int] | None:
    for currentField in dividedFields:
        moveTo.position(currentField["startY"], currentField["startX"])
        if get_entity_type() == Entities.Grass or get_entity_type() == None:
            return currentField
    
    return None

def fieldIntoRestList(field: dict[str, int]) -> dict[int, list[int]]:
    startX = field["startX"]
    startY = field["startY"]
    length = field["length"]
    restField = {}
    for x in range(startX, startX + length):
        restField[x] = []
        for y in range(startY, startY + length):
            restField[x].append(y)
    
    return restField

def replantSpace(restFields: dict[int, list[int]]) -> dict[int, list[int]]:
    newRestField = {}
    for x in restFields:
        for y in restFields[x]:
            moveTo.position(y, x)
            if get_ground_type() != Grounds.Soil:
                till()
            if get_entity_type() != Entities.Pumpkin:
                harvest()
                plant(Entities.Pumpkin)
                plantEntity.water()
                if x not in newRestField:
                    newRestField[x] = []
                newRestField[x].append(y)

    return newRestField

def startWorker() -> None:
    hat.randomHat()
    dividedFields = getDividedField()

    freeField = findFreeField(dividedFields)
    
    if freeField == None:
        return      # No field is free, so nothing todo
    
    newRestField = replantSpace(fieldIntoRestList(freeField))
    while newRestField != {}:
        newRestField = replantSpace(newRestField)

    # farm it
    moveTo.position(freeField["startY"], freeField["startX"])
    harvest()

def startWorkerOrSupporter(workers: list, numMaxWorker: int) -> list:
    # return if no drones left over
    if num_drones() >= max_drones():
        return workers
    # remove finished workers
    for worker in workers:
        if has_finished(worker):
            workers.remove(worker)
    # start worker or support
    if len(workers) < numMaxWorker:
        workers.append(spawn_drone(startWorker))
    else:
        spawn_drone(replantWithSupportDrone)

    return workers

def handleFullPmpkinFieldSeparated() -> None:     # field: field2.FieldList
    clear()
    dividedFields = getDividedField()

    freeField = dividedFields.pop(0)
    numFieldWorker = len(dividedFields)

    workers = []
    
    while True:
        restFields = fieldIntoRestList(freeField)
        while restFields != {}:
            newRestFields = {}
            for x in restFields:
                for y in restFields[x]:
                    moveTo.position(y, x)
                    if get_ground_type() != Grounds.Soil:
                        till()
                    if get_entity_type() != Entities.Pumpkin:
                        harvest()
                        plant(Entities.Pumpkin)
                        plantEntity.water()
                        if x not in newRestFields:
                            newRestFields[x] = []
                        newRestFields[x].append(y)
                    workers = startWorkerOrSupporter(workers, numFieldWorker)

            restFields = newRestFields

        # farm it
        moveTo.position(freeField["startY"], freeField["startX"])
        harvest()
