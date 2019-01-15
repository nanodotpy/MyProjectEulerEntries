from math import *


def prime(n) : 
    
    n = int(n)
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
        
    
    return False



a = int(input("Largest Prime Factor of ? "))

for i in range(3,a,2) :
    if a % i == 0 and prime(a//i):
        print(a//i)
        break
        
        
  #
            
    
            

            
            
