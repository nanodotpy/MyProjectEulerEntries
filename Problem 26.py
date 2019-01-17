"""
from decimal import *                                      # this first try doesnt fucking work


getcontext().prec = 2000


def pattern_len(integer) :
    
    decimals = Decimal(1)/Decimal(integer)
    
    decimals = (str(decimals))[2:]
    
    while decimals[0] == '0':
        decimals = decimals[1:]
        
    for i in range(1,len(decimals)-250):
        if decimals[i+20] == decimals[20] and decimals[2*i + 20] == decimals[20] :
            return int(i)
    else :
        return 0
    
    
cycleslen = []    
    
    


if __name__ == "__main__" :
    for a in range(2,1000): 
        cycleslen.append(pattern_len(a))
        
print(max(cycleslen))
"""

#Learned that the decimal cycle is the longest for 1/n when n is a 'long prime number'
# un nombre est premier long si et seulement si le premier residu des puissances de 10 modulo p egal a 1 est obtenu seulement pour 10**(p-1)

from math import ceil, sqrt
from decimal import *


getcontext().prec = 2000


def prime(n) : 
    
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
    return False

def long_prime(p) :
    
    
    if prime(p):
        if  p < 7 :
            return False
        
        t= 1
        for i in range(1,p-2):
            m = 10**i % p
            if m == 1 :
                t = 0
                i = p-1
        if t == 1 :
            return True
        else : 
            return False
    else :
        return False
        
thelongprimeslist = [] 
    
if __name__ == "__main__" :
    
    for a in range(1,1000) :
        if long_prime(a) :
            thelongprimeslist.append(a)
            
    print(max(thelongprimeslist))
    
#found the biggest long prime lower to 1000
            
    
 
      
        

        
