import field2
import handlePumpkin

clear()

currentField = field2.giantOnlyField(Entities.Pumpkin, True, False)
pumpkinField = field2.getSpecificTypeField(Entities.Pumpkin, currentField)

handlePumpkin.handleFullPumpkinField(pumpkinField)
