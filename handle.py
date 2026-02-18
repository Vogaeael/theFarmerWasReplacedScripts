import entityGrid

def water() -> None:
    if 0 == get_water():
        use_item(Items.Water)

def fertilize() -> None:
    use_item(Items.Fertilizer)

def handle(entity, farmSeparate: bool) -> None:
    if entity["water"]:
        water()

    if entity["fertilize"]:
        fertilize()

    # is skipable?
    if entity["entity"] in farmSeparate and farmSeparate[entity["entity"]]:
        # skip
        return

    # check costs
    cost = get_cost(Entities.Cactus)
    for item in cost:
        if num_items(item) < cost[item]:
            nextEntity = entityGrid.items()[item]
            handle(nextEntity)
            return

    if can_harvest() or get_entity_type() == Entities.Dead_Pumpkin:
        harvest()

        neededGroundType = entityGrid.grounds()[entity["entity"]]
        if get_ground_type() != neededGroundType:
            till()
        plant(entity["entity"])
