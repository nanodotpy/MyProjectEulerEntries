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

def number_to_set(number) :
    string = str(number)
    numberset = set(string)
    return numberset

primes = [prim for prim in range(1000,10000) if prime(prim)]

for a in primes :
    for b in range(1,10001-a) :
        A = a 
        B = a + b
        C = a + 2*b
        if C <= 10000 and prime(B) and prime(C) :
            
            setA = number_to_set(A)
            setB = number_to_set(B)
            setC = number_to_set(C)

            if setA == setB == setC :
                print(str(A)+str(B)+str(C))
        