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
        Items.Hay: 10 * 1000 * 1000,    # 10M
        Items.Wood: 100 * 1000 * 1000,    # 100M
        Items.Carrot: 10 * 1000 * 1000,    # 10M
        Items.Pumpkin: 25.9 * 1000 * 1000,    # 25.9M
        Items.Cactus: 10 * 1000 * 1000,    # 10M
        Items.Power: 10 * 1000 * 1000,    # 10M
        Items.Gold: 1000 * 1000,    # 1M
        Items.Weird_Substance: 1000 * 1000,    # 1M
        Items.Bone: 100 * 1000 * 1000,      # 100M
    }
    i = 1
    while 1:
        for item in items:
            if num_items(item) < (items[item] * i):
                cost = get_cost(entityGrid.getEntityToItem(item))
                for costItem in cost:
                    if num_items(costItem) < (cost[costItem] * 32 * 32 * 2):    # 32 * 32 is the field, 2 because of replanting like pumpkins
                        return entityGrid.getItemToEntity(needs(entityGrid.getEntityToItem(costItem)))
                return item
        i = i + 1
