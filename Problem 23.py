from math import ceil, sqrt

def abundant(number):
    divisors = []
    for a in range(1,ceil(sqrt(number))+1):
        if number % a == 0:
            divisors.append(a)
            divisors.append(number//a)
    
    divisors = list(set(divisors))
    
    somme = sum(divisors) 
    
    if somme > 2*number :
        return True
    else :
        return False

somme = 0

abundants = [value for value in range(1,28124) if abundant(value)]
    
abundant_set = set(abundants)        
    
for a in range(1,28124):
    for i in abundant_set:
        if i<a and a - i in abundant_set:
            break
    else :
        somme += a
            
print(somme)
        
        
            

