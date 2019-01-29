from math import ceil,sqrt

def prime(n) : 
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
    
    return False

def newprimecorners(c) :
    total = 0
    n = c//2
    a = 4*n**2-2*n+1
    b = 4*n**2 + 1
    d = 4*n**2 +2*n+ + 1
    if prime(a) :
        total += 1
    if prime(b) :
        total += 1
    if prime(d) : 
        total += 1
    return total


total = 13
primes = 8

for i in range(9,100000,2) :
    total += 4 
    primes += newprimecorners(i)
    if primes/total < 0.1 :
        print(i)
        break