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

def composite(number) : 
     number = int(number)
     for a in range(2,ceil(sqrt(number))) :
         if number % a == 0 :
             return True
     else :
         return False
     
compodds = [number for number in range(3,100000,2) if composite(number)]

primes = [prim for prim in range(3,100000) if prime(prim)]    

squares = [2*square**2 for square in range(1,10000)]

def goldbach(number) :
    if number in compodds :
        for a in primes : 
            if a > number :
                break
            if number - a in squares :
                return True
        else :
            return False
        
for number in compodds :
    if not goldbach(number):
        print(number)            
        break