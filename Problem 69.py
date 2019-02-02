from math import ceil, sqrt

def prime(n) : 
    if n == 1:
        return False                        #BRUTE FORCEEEEEEEE
    
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
        return [number]
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
            
    return set(factors)


def phi(n):
    factors = primefactors(n)       
    image = n
    for factor in factors:
        image *= (1-1/factor) 
    return int(image)

maximumquotient = 1

maxn = 999999

for n in range(524286,1,-2):        # 524286 was blocking my brute force problem resolving :p
    if n/phi(n) > maximumquotient:
        maximumquotient = n/phi(n)
        maxn = n
        print(maxn,n/phi(n))





    
    