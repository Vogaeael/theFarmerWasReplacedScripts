def getUnlockedHatList() -> None:
    return [
        Hats.Brown_Hat,
        Hats.Cactus_Hat,
        Hats.Carrot_Hat,
        #Hats.Dinosaur_Hat,
        Hats.Gold_Hat,
        Hats.Golden_Sunflower_Hat,
        Hats.Gray_Hat,
        Hats.Green_Hat,
        Hats.Pumpkin_Hat,
        Hats.Purple_Hat,
        Hats.Straw_Hat,
        Hats.Sunflower_Hat,
        Hats.Traffic_Cone,
        Hats.Tree_Hat,
        Hats.Wizard_Hat,
    ]

def randomHat() -> None:
    unlockedHats = getUnlockedHatList()
    index = random() * len(unlockedHats) // 1
    change_hat(unlockedHats[index])
