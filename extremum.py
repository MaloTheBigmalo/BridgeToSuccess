
def f(x):
    return x**3 + 2*x**2 - x + 3

def main():

 a = -2 # intervalle inférieur
 b = 1  # intervalle supérieur
 mini = f(a)
 maxi = f(a)
 n = 30# n est le nombre de petites intervalles entre a et b : on divisera par 15 la distance entre a et b
 dx = (b - a)/n #la cadence de déplacement en partant de a vers b
 print(" dx %s "%dx)
 x = a # la première de valeur à vérifier est le debut de l'intervalle càd a

# Parcourons l'intervalle entre a et b pour chercher l'extremum minimum et maximum

 for i in range(n):
    x = x + dx
    y = f(x)
    if y > maxi:
        maxi = y
       # print("xmaxi == ",round(x,2)," fmaxi == ",round(maxi,3))
    if y < mini:
        mini = y
        #print("xmini == ",round(x,2)," fmini == ",round(mini,3))

 print("extremum minimal ", round(mini,3))
 print("extremum maximun ", round(maxi,3))

if __name__=='__main__':
    main()