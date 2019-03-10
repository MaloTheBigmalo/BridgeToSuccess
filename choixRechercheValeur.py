import sys


def choixRechercheValeur(A,monChoix):
    if monChoix==1:
        min = A[0]
        for i in range(0,len(A)):
            if A[i]<min:
                min=A[i]
        return min
    else :
        max = 0
        for i in range(0,len(A)):
            if A[i]>max:
                max=A[i]
        return max

tab=[8,3,7,1,9,4,5,2,6]
print(tab)
choix=int(sys.argv[1])
element=choixRechercheValeur(tab,choix)
print(element)

