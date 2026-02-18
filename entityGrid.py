def items() -> dict[Item, Entity]:
    return {
        Items.Cactus: Entities.Cactus,
        Items.Wood: Entities.Bush,
        Items.Carrot: Entities.Carrot,
        Items.Hay: Entities.Grass,
        Items.Pumpkin: Entities.Pumpkin,
        Items.Power: Entities.Sunflower,
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
