
import sys

premier = 0
deuxieme = 1
suivant = 0
n_terme = int(sys.argv[1]) # le nombre de termes de la suite fibonacci est donné en paramètre au moment du lancement de programme

list_fibonacci = []
# boucle for
for ctr in range(n_terme):
    if ctr < 1 :         #quant le compteur est inférieur ou égale à 1, suivant prend la valeur du comp
        suivant = premier
        list_fibonacci.append(premier)
    elif ctr == 1:
        suivant = deuxieme
        list_fibonacci.append(deuxieme)
    else :
        list_fibonacci.append(premier + deuxieme)
        suivant = premier + deuxieme
        premier = deuxieme
        deuxieme = suivant


    print(suivant,end=" ")

print("\n")

for i in list_fibonacci:
    print(i, end =" ")

print("\n")


