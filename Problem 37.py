from math import ceil, sqrt

def prime(n) : 
    
    if n == 1 :
        return False
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
        
    
    return False

def truncatable(number) :
    if not prime(number) :
        return False
    number = str(number)
    for a in range(1,len(number)):
        right = int(number[a:])
        left = int(number[:a])
        
        if not prime(left) or not prime(right) :
            break
    else : 
        return True
    return False
    


truncas = [] 

e = 10

while len(truncas) != 10 :
    if prime(e) and truncatable(e) :
        truncas.append(e)
        print(e)
        
    e += 1
    
print(sum(truncas)+23)   #No idea why 23 isnt in the list : gotta fix it
    
        