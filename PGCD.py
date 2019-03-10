D=int(input("Taper la Dividende s'il vous plait  "))

d=int(input("Taper la diviseur s'il vous plait  "))

diff=0

while D - d > 0:
    diff = D - d
    if diff > d:
        D = diff
    else :
        D = d
        d = diff

print("Le PGCD est ", diff)