from random import randint

n = randint(0,63)
print(n)

for i in range(2,n):
    if n <= 1:
        print("False ")
    if n % i == 0:
        print("False ")
    print("True")


