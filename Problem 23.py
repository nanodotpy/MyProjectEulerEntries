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
    

abundants = []    
    
sumabundants = []

for a in range(1,30000):
    if abundant(a) :
        abundants.append(a)
        
def sum_of_abundants(number) :
    
    for i in abundants :
        if i <= number :
            pair = number - i 
            if pair in abundants :
                return True
            else : 
                return False
        
        
for number in range(1,28124) :
    if sum_of_abundants(number) :
        sumabundants.append(number)
       
print(sumabundants)        
        
result = [value for value in list(range(1,28124)) if value not in sumabundants]

print(sum(result))
        

   

                  