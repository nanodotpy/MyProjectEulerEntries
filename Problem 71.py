import fractions
import math

for d in range(999999, 0, -1):
    n = math.floor(3/7 * d)
    if math.gcd(d, n) == 1:
        print(fractions.Fraction(n,d))
        break