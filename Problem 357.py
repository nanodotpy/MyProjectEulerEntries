"""
used in the divisors function
"""
from math import ceil, sqrt

FILE = open("PRIMES TO 100M.txt", "r")

PRIMES = FILE.read()
                                        # Optimized it as much as I could but takes a lot of time
PRIMES = PRIMES.split(', ')

PRIMES = [int(prime) for prime in PRIMES]

PRIMES_MINUS_1 = [prime-1 for prime in PRIMES]

def divisors(number):
    """
    returns the divisors of a positive integer
    """
    if number == 1:
        return [1, 1]
    divs = []
    for potiential_divisor in range(1, ceil(sqrt(number))+1):
        if number % potiential_divisor == 0:
            divs += [potiential_divisor, number//potiential_divisor]
    divs.sort()
    return divs

def is_prime(number):
    """
    returns if a number is prime or not
    """
    if number == 2:
        return True

    list0 = [2] + list(range(3, ceil(sqrt(number))+1, 2))
    for i in list0:
        if number % i == 0:
            break
    else:
        return True

    return False

LISTE = list(set([2] + [element -1 for element in PRIMES if element % 4 == 3]))

LISTE.sort()

RESULT = [1]

for j in LISTE:

    for d in divisors(j)[:len(divisors(j))//2 +1]:
        if not is_prime(d +j/d):
            break
    else:
        RESULT.append(j)

print(sum(RESULT))
