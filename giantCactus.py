import field2
import handleCactus
import plantEntity

currentField = field2.giantOnlyField(Entities.Cactus, True, False)
cactusField = field2.getSpecificTypeField(Entities.Cactus, currentField)


plantEntity.plantField(cactusField)

handleCactus.handleFullCactusField(cactusField, True)
