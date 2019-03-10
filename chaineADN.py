
#créer une chaine d'ADN qui prend en argument un nombre entier naturel n et renvoie une chaine de caractères tirés chacun au hasard
#parmi les caractères A, C, G, T
#n sera le nombre de caractère présent dans l'ADN
from random import randint
import sys

def chaineADN(n):
    choix='ACGT'
    adn=''
    for i in range(n):
        alea = randint(0,3)
        adn = adn + choix[alea]
    return adn
n=int(sys.argv[1])
adn1 = chaineADN(n)
print(adn1)




