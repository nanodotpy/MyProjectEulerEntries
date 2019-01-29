from fractions import Fraction 

def decimals_of_root(n) :
    
    if n == 1 :
        decimal = Fraction(1,2)
    if n == 2 :
        decimal = Fraction(1,2+Fraction(1,2))
    if n > 2 :
        decimal = Fraction(1,2+decimals_of_root(n-1))
        
    return decimal


def decimals_to_root(n) :
    return Fraction(decimals_of_root(n))+1


total = 0


for a in range(1,1001) :
    if len(str(decimals_to_root(a).numerator)) > len(str(decimals_to_root(a).denominator)) :
        total += 1
        
print(total)
