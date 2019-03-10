#---------------------------------fonctions utilisées dans ce programme------------

def BitnDe(nombre): # pour un nombre donné, la fonction calcule le nombre de bit correondant
    counter = 0
    while nombre > 0:
        nombre = nombre//2
        counter = counter + 1
    return counter


inputnumber=int(input("Taper un entier positif "))
bitnombre=BitnDe(inputnumber) - 1
maxnumber = 2**bitnombre
output=' '

while maxnumber >= 1:
     if inputnumber >= maxnumber:
           inputnumber=inputnumber - maxnumber
           output=output + '1'
           maxnumber=(maxnumber//2)
     else:
           output=output + '0'
           maxnumber=(maxnumber//2)

print(output)



