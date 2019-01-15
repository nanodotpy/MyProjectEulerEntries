from math import ceil, sqrt


def tri(a) :
    t = a * (a+1)//2
    return t

def nfactors(nu) :
    fac = 2
    if nu == 1 :
        return 1
    
    for i in range(2, ceil(sqrt(nu))+1) :
        if nu % i == 0 :
            fac += 2
    return fac
              
a = 1
  
while not nfactors(tri(a)) > 500 :
    a += 1


print(tri(a))
    