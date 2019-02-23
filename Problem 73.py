import fractions
import math

setincroyable = set()

for d in range(1, 12001):
    for n in range(int(math.ceil(1/3*d)), int(math.floor(1/2*d)+1)):
        if math.gcd(d, n) == 1:
            setincroyable.add(fractions.Fraction(n,d))
            
setincroyable -= {fractions.Fraction(1, 2), fractions.Fraction(1, 3)}

print(len(setincroyable))

#Took 3 mins but NICE
