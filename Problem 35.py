from math import sqrt, ceil

def prime(n) : 
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
        
    
    return False

def rotate(number): 
    
    thelist = [number]
    number = str(number)
    for d in range(1,len(number)) :
        Rfirst = number[0 : len(number)-d] 
        Rsecond = number[len(number)-d : ] 
        thelist.append(int(str(Rsecond + Rfirst)))
    return thelist

def is_circular_prime(integer) :
    if prime(integer) :
        for number in rotate(integer) :
            if not prime(number) :
                return False
        else : 
            return True
    else : 
        return False
    
num = 0 
    
for a in range(1000001) :
    if is_circular_prime(a) :
        num+= 1
        
print(num)