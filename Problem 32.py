from math import ceil,sqrt

digits = list(range(1,10))

def divisors(number) :
    divisors = []
    for a in range(1,ceil(sqrt(number))+1) :
        if number%a == 0:
            divisors.append(a)
            divisors.append(number//a)
    return divisors
 
digits = set(range(1,10))


def pandigital_product(number) :
    itsdivisors = divisors(number)
    products = ['{}{}{}'.format(itsdivisors[e],itsdivisors[e+1],number) for e in range(0,len(itsdivisors)-1,2)]
    products = [list(product) for product in products] 
    
    for a in products :
        a = [int(e) for e in a ]
        
        if digits == set(a) :
            break

    else : 
        return False
    
    return True
    
somme = []

for a in range(0,10000) :
    if pandigital_product(a) :
        somme.append(a)
        
print(sum(set(somme)))