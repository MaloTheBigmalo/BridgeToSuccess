
from random import randint

num = randint(1,501)
print("Devinez un nombre entre 1 et 500")
counter=0
while True:
    trouve=int(input("Proposé le nombre deviné ? "))
    if trouve==num:
        print("C'est trouvé...Bravo")
        break
    elif trouve>num:
        print("C'est plus ")
    else :
        print("Cest moins")
    counter+=1
print("Boucle == {}".format(counter+1))

