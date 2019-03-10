
# soit la fonction f(x) ci-dessous, et on calcule la somme des aires entre x=2 et x=0
# l'agorithme de la page illustre le principe de l'encadrement de l'intégrale d'une fonction positive
# -----------
    # intervalle est défini entre b=2 et a=0
    # n est le nombre par lequel on divisera b-a et on calcule notre h = (b - a)/n
    # h étant cette petite largeur, elle est plus petite selon que n est plus grand. Plus grand, mieux c'est.
    # S1 et S2 sont deux aires disctinctes formées par deux points adjacents x et x+h. Ainsi on a deux rectangles : un grand et un petit.

def f(x):
    result = x**2 + 2
    return result

def main():

    a = 0
    b = 2
    S1 = 0
    S2 = 0
    n = 10# 2/100 = 0.02 donc une tout petite valeur comme largeur de notre rectangle.
    x = a
    h= (b - a)/n
    for i in range(0,n-1):
        S1 = S1 + h*f(x) # ici nous faisons la somme des petits rectangles
        x = x + h
        S2 = S2 + h*f(x) # ici nous faisons la somme des grands rectangles
    print("la somme des petits rectangles est ",S1, "unités d'aire")
    print("la somme des grands restangles est ", S2,"unités d'aire")



if __name__=="__main__":
        main()

