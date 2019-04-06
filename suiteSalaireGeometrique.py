# Ce programme calcule le nombre de mois qu'un salaire ayant 1% d'augmentation mensuelle doit travailler pour doubler son salaire
# le salaire initial est fixé à 3700 euros

sal = 3700
n = 0 # nombre de mois
taux=0.01
coefficient= 1 + taux

while sal < 7400:
    print("n: ",n,"salaire: ",sal)
    sal = sal*coefficient
    n = n + 1
print(n,"mois")
