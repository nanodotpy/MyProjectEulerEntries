from math import *


def ceilsq(x) :
    x = ceil(sqrt(x))
    return x

def prime(n) : 
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceilsq(n)+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
        
    
    return False


result = [2]

def plist(n): 
    for i in [2] + list(range(3,n+1,2)) :
        if prime(i) :
            result.append(i)
    return result
        
plist(1000000)

print(result[10000])


#
