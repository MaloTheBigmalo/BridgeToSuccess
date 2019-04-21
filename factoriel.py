
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n*factoriel(n-1)


n = int(input("Taper l'entier "))
print("le factoriel de ",n, "égale :",end="")
print(factoriel(n))