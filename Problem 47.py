from math import ceil, sqrt

def prime(n) : 
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
    
    return False

def primefactors(number) :
    if prime(number) :
        return [1,number]
    factors = []
    e = 1
    while not prime(number) :
        e += 1 

        if number % e == 0:
            factors.append(e)
            number = number//e
            e = 1
        if prime(number) : 
            factors.append(number)
    for a in factors :
        if factors.count(a) > 1 :
            factors[factors.index(a)] **= factors.count(a)               
            factors = list(filter(lambda e: e != a , factors))
        
        factors = list(set(factors))
            
    return factors


compos = [number for number in range(644,1000000) if not prime(number)]
    
for a in compos :
    A = primefactors(a)
    B = primefactors(a+1)
    C = primefactors(a+2)
    D = primefactors(a+3)  
                                                 #Unpythonic way
    
    if len(A) >= 4 and len(B) >= 4 and len(C) >= 4 and len(D) >= 4 :
        print(A,B,C,D)
        print(a)
        break
    
    