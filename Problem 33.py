from operator import mul
from functools import reduce

list1 = list(set(range(10,100))-set(range(10,101,10)))
list2 = []
final = []

def product(list1):
    return reduce(mul, list1)

def euclide_algorithm(a,b) :
    r = 1
    if a<b : 
        b = a
        a = b 
        
    while r != 0 :
        r = a % b
        if r == 0 :
            break
        else :
            a = b
            b = r
    return b

for a in list1 :
    for b in list1[list1.index(a)+1:] :
        A = set(str(a))
        B = set(str(b))
        if len(B.intersection(A)) == 1 :
            list2.append((a,b))
       
        
for couple in list2 :
    decimal1 = couple[0]/couple[1]
    A = set(str(couple[0]))
    B = set(str(couple[1]))
    
    if A - B.intersection(A) != set() :
        a = list(A - B.intersection(A))
        a = int(a[0])
    else :
        a = int(str(couple[0])[0])
    if B - B.intersection(A) != set() :
        b = list(B - B.intersection(A))
        b = int(b[0])
    else :
        b = int(str(couple[1])[0])
    
    if decimal1 == a/b :
        final.append(couple)     
        

numerator = product([couple[0] for couple in final])        

denominator = product([couple[1] for couple in final])

pgcd = euclide_algorithm(numerator,denominator)

print(int(denominator/pgcd))



 