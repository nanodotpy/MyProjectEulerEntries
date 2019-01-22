from math import factorial

def digit_factorials(natural) :
    digits = [int(digit) for digit in str(natural)]
    digits = [factorial(digit) for digit in digits ]
    return sum(digits)

somme = 0

for a in range(3,100000) :
    if digit_factorials(a) == a :
        somme += a
        
print(somme)
    