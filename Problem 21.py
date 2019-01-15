from math import ceil, sqrt 

def sigma(n):
    
    divisors = []
    for a in range(1,ceil(sqrt(n))+1):
        if n % a == 0:
            divisors.append(a)
            divisors.append(n//a)
        
    return sum(divisors)

amicablelist = []

for a in range(1,10000) :
    
    sa = sigma(a)  
    b = sa - a
    if sigma(b) == sigma(a) and a!= b :
        amicablelist.append(a)
        amicablelist.append(b)


print(sum(amicablelist)//2)


