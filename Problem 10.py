from math import *

def prime(n) : 
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
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
        
plist(2000000)

print(sum(result))

