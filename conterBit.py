
def BitnDe(nombre): # pour un nombre donné, la fonction calcule le nombre de bit correondant
    counter = 0
    while nombre > 0:
        nombre = nombre//2
        counter = counter + 1
    return counter

nombre=BitnDe(74)
print(nombre)