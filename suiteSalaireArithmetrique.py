# Ce programme calcule le nombre de mois qu'un salaire ayant 20 euros d'augmentation mensuelle doit travailler pour doubler son salaire
# le salaire initial est fixé à 3700 euros

sal = 3700
n = 0 # nombre de mois
augsal = 20

while sal < 7400:
    sal = sal + augsal
    n = n + 1
print(n,"mois")
