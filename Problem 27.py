from math import ceil, sqrt      #Not optimized but gets the job done

def prime(n) : 
    
    n = int(n)
    
    if n == 2 :
        return True
    
    list0 = [2] + list(range(3,ceil(sqrt(n))+1,2))
    for i in list0 :
        if n % i == 0 :
            break
    else : 
        return True
        
    
    return False

primes = [n for n in range(100000) if prime(n)]

def quadratic(x,a,b) :
    return x**2 + a*x + b

coefficients = []

for a in range(-999,1000) :
    for b in range(-1000,1001):
        if quadratic(0,a,b) >= 0 and quadratic(0,a,b) in primes :
            if quadratic(1,a,b) >= 0 and quadratic(1,a,b) in primes :
                if quadratic(2,a,b) >= 0 and quadratic(2,a,b) in primes :

                    coefficients.append((a,b))
            
            
themax = []
           
z = 0
x = 0
 
for z in range(len(coefficients)-1):
    x = 0
    while quadratic(x,coefficients[z][0],coefficients[z][1]) in primes :
        x += 1 
        
    themax.append((x,coefficients[z][0],coefficients[z][1]))


bestofmax = [x[0] for x in themax]

for a in themax :
    if a[0] == max(bestofmax):
        print(a[1]*a[2])
