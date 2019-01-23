from itertools import permutations
from math import ceil,sqrt

permus = list(permutations(range(0,10)))

primes = [2,3,5,7,11,13,17]

def property(number) :
    string = str(number)
    for a in range(1,8) :
        if not int(string[a:a+3]) % primes[a-1] == 0 :
            return False
    else :
        return True

print(property(1406357289))
somme = 0
for a in list(permutations(range(0,10))) :
    b = ""

    for n in a :
        b = int(str(b) + str(n)) 
    if property(b) :
        somme += b


print(somme)
