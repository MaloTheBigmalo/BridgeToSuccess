# c'est l'algo d'une suite. On y calcule aussi la somme de la suite
u=50 # u signifie Uo
s=u  # s signifie somme a l'origine

n=int(input("Taper le nombre de mois  ")) # on demande à l'utilisateur d'entrer le nombre de mois
print("u({}) = {}".format(0,u), end=" ")
print("s({}) = {}".format(0,s))
for i in range(1,n+1):
    u=u+4
    s=s+u
    print("u({}) = {}".format(i,u), end=" ")
    print("s({}) = {}".format(i,s))




