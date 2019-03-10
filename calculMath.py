
def calculMath(x):
    resultat=x*2+4
    return resultat

def main():
    print("Le resultat de l'opération égale ",end="")
    solution= calculMath(6)
    print(solution)
    print("Faire à calcul math une deuxième fois égale ",end="")
    solution2=calculMath(8)
    print(solution2)

if __name__=='__main__':
   main()