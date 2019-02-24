
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n*factoriel(n-1)


n = int(input("Taper l'entier "))
#P = 1
#for i in range(1,n+1):
#    P = P*i
#print("le factoriel de n",n," égale ",P)
print("le factoriel de ",n, "égale :",end="")
print(factoriel(n))