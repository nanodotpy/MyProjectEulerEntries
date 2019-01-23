from math import ceil, sqrt
from itertools import permutations

def prime(n) : 
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
    return False

"""
for a in (list(permutations(range(1,10))))[::-1] :
    b = ""
    for n in a :
        b = int(str(b) + str(n)) 
    if prime(b) :
        print(b)
        break
 """
    # no prime 9-pandigit 
    
for a in (list(permutations(range(1,8))))[::-1] :
    b = ""
    for n in a :
        b = int(str(b) + str(n)) 
    if prime(b) :
        print(b)
        break

