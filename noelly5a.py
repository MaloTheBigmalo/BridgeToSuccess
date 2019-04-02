import numpy as np
from random import randint

# la fonction prod(M) définie renvoie le produit des coefficients de la matrice M
# resultat = resultat*M[i] on multiplie res=1 par chaque coefficient trouver dans la matrice
#n variable qui compte le nombre d'achat de céréales effectués
# soit la matrice A avant le premier achat càd il n'y a aucune figurine présente
#variable fig détrmine la position où placer la figurine gagnée dans la matrice
# on va faire une boucle disant que le produit des coefficients renverra un nombre inférieur à 0, ce qu'on n'a pas encore toutes les 11 figures.
# Dans la boucle on incrémentera la variable n qui indiquera à la fin le nombre de boites des céréales achetées pour obtenir au total les 11 figures.
# On utilise la fonction random pour tirer de façon hasardeuse une des 11 figurines à la fois.

def prod(M):
    resultat = 1
    for i in range(np.size(M)):
        resultat = resultat*M[i]
    return resultat

def afficher(A):
    for i in range(np.size(A)):
        print("i = ",i, "valeur = ",A[i])

def zeros(a,b):
    A = np.array([0*x for x in range(a,b)])
    return A


M = zeros(1,12)
n = 0


while prod(M) < 1 :
    fig = randint(1,11) # choisit au hasard entre 1 des 11 figures
    pos = fig - 1
    if M[pos] == 0:
       M[pos] = 1
    n = n + 1
print("le nombre de boîtes nécessaires pour avoir une collection complète n = ",n)



