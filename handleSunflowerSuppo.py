import hat
import plantEntity

def farmRow(size: int) -> None:
    hat.randomHat()
    for _ in range(get_world_size()):
        if measure() == size:
            harvest()
        move(East)

def farm7() -> None:
    farmRow(7)

def farm8() -> None:
    farmRow(8)

def farm9() -> None:
    farmRow(9)

def farm10() -> None:
    farmRow(10)

def farm11() -> None:
    farmRow(11)

def farm12() -> None:
    farmRow(12)

def farm13() -> None:
    farmRow(13)

def farm14() -> None:
    farmRow(14)

def farm15() -> None:
    farmRow(15)

def farmIt() -> None:
    maxSunflowerSize = 15
    minSunflowerSize = 7
    farmFunctions = {
        7: farm7,
        8: farm8,
        9: farm9,
        10: farm10,
        11: farm11,
        12: farm12,
        13: farm13,
        14: farm14,
        15: farm15,
    }
    for currentSize in range(maxSunflowerSize, minSunflowerSize - 1, -1):
        for _ in range(get_world_size()):
            if num_drones() < max_drones():
                spawn_drone(farmFunctions[currentSize])
            else:
                farmRow(currentSize)
            move(North)


def handleFullSunflowerField(alreadyPlanted: bool) -> None:
    if not alreadyPlanted:
        plantEntity.plantFullField(Entities.Sunflower, True, False, True)

    farmIt()
    do_a_flip()
