def items() -> dict[Item, Entity]:
    return {
        Items.Hay: Entities.Grass,
        Items.Wood: Entities.Tree,
        Items.Carrot: Entities.Carrot,
        Items.Pumpkin: Entities.Pumpkin,
        Items.Cactus: Entities.Cactus,
        Items.Power: Entities.Sunflower,
        Items.Bone: Entities.Dinosaur,
        Items.Gold: Entities.Treasure,
        Items.Weird_Substance: Entities.Grass,
    }

def entities() -> dict[Entity, Item]:
    # Since the next line doesn't work we have to add it hardcoded
    #return {v: k for k, v in items().items()}
    return {
        Entities.Grass: Items.Hay,
        Entities.Tree: Items.Wood,
        Entities.Carrot: Items.Carrot,
        Entities.Pumpkin: Items.Pumpkin,
        Entities.Cactus: Items.Cactus,
        Entities.Sunflower: Items.Power,
        Entities.Dinosaur: Items.Bone,
        Entities.Treasure: Items.Gold,
        Entities.Grass: Items.Weird_Substance,
    }

def grounds() -> dict[Entity, Ground]:
    return {
        Entities.Cactus: Grounds.Soil,
        Entities.Bush: Grounds.Grassland,
        Entities.Tree: Grounds.Grassland,
        Entities.Pumpkin: Grounds.Soil,
        Entities.Carrot: Grounds.Soil,
        Entities.Grass: Grounds.Grassland,
        Entities.Sunflower: Grounds.Soil,
    }

def defaults() -> dict[Entity, dict]:
    return {
        Entities.Cactus: {
            "water": True,
            "fertilize": False,
        },
        Entities.Bush: {
            "water": False,
            "fertilize": False,
        },
        Entities.Tree: {
            "water": True,
            "fertilize": False,
        },
        Entities.Carrot: {
            "water": True,
            "fertilize": False,
        },
        Entities.Grass: {
            "water": False,
            "fertilize": False,
        },
        Entities.Pumpkin: {
            "water": True,
            "fertilize": False,
        },
        Entities.Sunflower: {
            "water": True,
            "fertilize": False,
        },
    }

def getEntityToItem(item: Item) -> Entity:
    itemToEntity = items()

    return itemToEntity[item]

def getItemToEntity(entity: Entity) -> Item:
    entityToItem = entities()

    return entityToItem[entity]

def getGroundToEntity(entity: Entity) -> Ground:
    entityToGround = grounds()

    return entityToGround[entity]

def getDefaultToEntity(entity: Entity) -> dict:
    entityDefaults = defaults()

    return entityDefaults[entity]
