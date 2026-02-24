import entityGrid

# Checks if the entity has costs and if we have enough for it. Returns the entity which is needed, or the original entity
def needs(entity: Entity) -> Entity:
    cost = get_cost(entity)
    for item in cost:
        if num_items(item) < (cost[item] * 32 * 32 * 2):    # 32 * 32 is the field, 2 because of replanting like pumpkins
            return needs(entityGrid.getEntityToItem(item))
    return entity

def next() -> Item:
    items = {
        Items.Hay: 30000000,    # 30M
        Items.Wood: 97700000,    # 97.7M
        Items.Carrot: 16400000,    # 16.4M
        Items.Pumpkin: 25900000,    # 25.9M
        Items.Cactus: 30000000,    # 30M
        Items.Power: 30000000,    # 30M
        Items.Gold: 50000,    # 50K
#        Items.Weird_Substance: 5000,    # 5K
#        Items.Bone: 10000,      # 10K
    }
    i = 1
    while 1 == 1:
        for item in items:
            if num_items(item) < (items[item] * i):
                cost = get_cost(entityGrid.getEntityToItem(item))
                for item in cost:
                    if num_items(item) < (cost[item] * 32 * 32 * 2):    # 32 * 32 is the field, 2 because of replanting like pumpkins
                        return entityGrid.getItemToEntity(needs(entityGrid.getEntityToItem(item)))
                return item
        i = i + 1
