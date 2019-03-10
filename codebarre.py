



codebarre=input("Taper les douze premiers chiffres du code barre  ")
dernierchiffre=int(input("Taper le dernier chiffre du code  "))

somme=0
counter=0
while counter < len(codebarre):
    if counter % 2 == 0 :
        somme=somme + int(codebarre[counter])*1
    else:
        somme=somme + int(codebarre[counter])*3
    counter = counter + 1

reste = somme%10
treizieme = 10 - reste
if treizieme == 10:
    treizieme=0
elif treizieme == dernierchiffre:
    print("Le code barre est valide")
else:
    print("Le code barre n n'est pas valide")

