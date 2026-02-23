import entityGrid

# Checks if the entity has costs and if we have enough for it. Returns the entity which is needed, or the original entity
def needs(entity: Entity) -> Entity:
    cost = get_cost(entity)
    for item in cost:
        if num_items(item) < (cost[item] * 32 * 32 * 2):    # 32 * 32 is the field, 2 because of replanting like pumpkins
            return needs(entityGrid.getEntityToItem(item))
    return entity

def next() -> Entity:
    entities = {
        Entities.Grass: {
            "min": 19700000,    # 19.7M
            "item": Items.Hay,
        },
        Entities.Tree: {
            "min": 97700000,    # 97.7M
            "item": Items.Wood,
        },
        Entities.Carrot: {
            "min": 16400000,    # 16.4M
            "item": Items.Carrot,
        },
        Entities.Pumpkin: {
            "min": 25900000,    # 25.9M
            "item": Items.Pumpkin,
        },
        Entities.Cactus: {
            "min": 15600000,    # 15.6M
            "item": Items.Cactus,
        },
        Entities.Sunflower: {
            "min": 30000000,    # 30M
            "item": Items.Power,
        },
        Entities.Treasure: {
            "min": 5000,    # 5K
            "item": Items.Gold,
        },
#        Entities.Dinosaur: {
#            "min": 100000000,   # 100M
#            "item": Items.Bone,
#        },
        # Suspect ...
    }
    i = 1
    while 1 == 1:
        for entity in entities:
            if num_items(entities[entity]["item"]) < (entities[entity]["min"] * i):
                cost = get_cost(entity)
                for item in cost:
                    if num_items(item) < (cost[item] * 32 * 32 * 2):    # 32 * 32 is the field, 2 because of replanting like pumpkins
                        return needs(entityGrid.getEntityToItem(item))
                return entity
        i = i + 1
