import handle
import field2
import handlePumpkin
import handleCactus
import handleSunflower
import hat
import moveTo

currentField = field2.field()
pumpkinField = field2.getSpecificTypeField(Entities.Pumpkin, currentField)
cactusField = field2.getSpecificTypeField(Entities.Cactus, currentField)
sunflowerField = field2.getSpecificTypeField(Entities.Sunflower, currentField)

farmSeparate = {
    Entities.Pumpkin: True,
    Entities.Cactus: True,
    Entities.Bush: False,
    Entities.Tree: False,
    Entities.Carrot: False,
    Entities.Grass: False,
    Entities.Sunflower: True,
}
moveTo.position(7, 7)

while 1:
    hat.randomHat()
    
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            type = currentField[get_pos_y()][get_pos_x()]
            handle.handle(type, farmSeparate)
            move(East)
        move(North)
    
    if farmSeparate[Entities.Pumpkin]:
        handlePumpkin.handlePumpkinField(pumpkinField)

    if farmSeparate[Entities.Cactus]:
        handleCactus.handleCactusField(cactusField)

    if farmSeparate[Entities.Sunflower]:
        handleSunflower.handleSunflowerField(sunflowerField)
