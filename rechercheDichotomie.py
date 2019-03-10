def func(x):
    res = x**3 + x - 11
    return res

a = 2
b = 3
ctr=0

while b-a >= 0.01:
    m = (a+b)/2
    if func(a)*func(m) <= 0:
        a = m
        ctr = ctr + 1
    else:
        b = m
        ctr = ctr + 1

print("valeur de a ", a)
print("valeur de b ", b)
print("compteur vaut = ",ctr)
