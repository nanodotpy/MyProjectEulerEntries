import is_prime

with open("PRIMES TO 100M.txt") as f:
    primes = f.read()

primes = primes.split(", ")

primes = [int(prime) for prime in primes if int(prime)<20_000_000]

def tobase(n, base):
    number = []
    while n:
        n, digit = divmod(n, base)
        number.append(str(digit))
    return [int(a) for a in number[::-1]]

def valpadique(p, k, n):
    r  = n - k
    R  = tobase(r, p)
    K  = tobase(k, p)
    KR = tobase(k+r, p)
    return (sum(K) + sum(R) - sum(KR))//(p-1)

result = 0

for a in primes:
    result += a*valpadique(a, 15000000, 20000000)
    
print(result)
