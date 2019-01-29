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
    
c = 0    
    
for a in range(101) :
    for b in range(0,a+1):
        if binomial_coefficient(a,b) > 1000000 :
            c += 1
            
print(c)