def getUnlockedHatList() -> None:
    return [
        Hats.Brown_Hat,
        Hats.Carrot_Hat,
        Hats.Gray_Hat,
        Hats.Green_Hat,
        Hats.Pumpkin_Hat,
        Hats.Pumpkin_Hat,
        Hats.Straw_Hat,
        Hats.Traffic_Cone,
        Hats.Tree_Hat,
        Hats.Gold_Hat,
        Hats.Wizard_Hat,
        #Hats.Dinosaur_Hat,
    ]

def randomHat() -> None:
    unlockedHats = getUnlockedHatList()
    index = random() * len(unlockedHats) // 1
    change_hat(unlockedHats[index])
