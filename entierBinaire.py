# Ce programme affiche en binaire un entier quelconque

n_entier = int(input("Taper un nombre entier positif "))
c_binaire ='' # chaine de caractère representant la representation binaire du nombre entier

while n_entier > 0:
    c_binaire=str(n_entier%2) + c_binaire
    n_entier=n_entier//2
print(c_binaire)