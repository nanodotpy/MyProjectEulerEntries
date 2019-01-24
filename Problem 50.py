from math import ceil, sqrt

def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total

def prime(n) : 
    if n == 2:
        return True
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
        
    return False

primes = [prim for prim in range(2,30000) if prime(prim)]

def sumprimes(prim) :
    if prime(prim) :
        z = 0
        b = 0
        chi = []
        for a in primes[primes.index(prim):]:
            z += a
            if z > 1000000 :
                break
            b += 1
            if prime(z):
                chi.append((b,z))
        a = max([value[1] for value in chi])
        return max(chi)
        
final = []    

for a in primes :
    final.append(sumprimes(a))
print(max(final)[1])
