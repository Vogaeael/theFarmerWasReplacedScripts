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

def getEntityToItem(item: Item) -> Entity:
    itemToEntity = items()

    return itemToEntity[item]

def getGroundToEntity(entity: Entity) -> Ground:
    entityToGround = grounds()

    return entityToGround[entity]