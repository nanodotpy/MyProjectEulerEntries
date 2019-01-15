from math import factorial

def binomial_coefficient(x,y) :
    if y > x:
        return None
    elif y == 0 :
        return 1
    elif y == x :
        return y
    elif x > y :
        return factorial(x)//(factorial(y)*factorial(x-y))
    

print(binomial_coefficient(40,20)) 

#Le nombre de possibilités de chemins dans une grille de dimensions (a*b) est égal au coefficient binomial de a parmi a + b
     