import field2
import handleCactus

currentField = field2.giantOnlyField(Entities.Cactus)
cactusField = field2.getSpecificTypeField(Entities.Cactus, currentField)

handleCactus.replant(cactusField)

handleCactus.handleCactusField(cactusField, True)
