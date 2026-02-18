import field2
import handlePumpkin

clear()

currentField = field2.giantOnlyField(Entities.Pumpkin)
pumpkinField = field2.getSpecificTypeField(Entities.Pumpkin, currentField)

handlePumpkin.handlePumpkinField(pumpkinField)
