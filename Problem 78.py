from math import ceil, sqrt, pi, e
import time
import sys

sys.setrecursionlimit(2000)

def p(n, k):
    if n < k:
        return 0
    if n == k or k == 1:
        return 1
    else:
        return p(n-1, k-1) + p(n-k, k)
    
def partitions(n):
    return sum([p(n, k) for k in range(1, n+1)])

def p_environ(n):
    return (e**(pi*sqrt(2/3*n)))/(4*n*sqrt(3))

def penta(n):
    return n*(3*n-1)//2

def penta_gen(n):
    indices = [[a, -a] for a in range(1, int(ceil((1 + sqrt(1+24*n))/6)+1))]
    indices = [a for sublist in indices for a in sublist]
    return [penta(i) for i in indices if penta(i) <= n]

parts_cache = {0: 1, 1: 1, 2: 2}

def parts(n):
    if n in parts_cache:
        return parts_cache[n]
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    parts_cache[n] = sum([parts(n-x) if a % 4 < 2 else -parts(n-x) for a, x in enumerate(penta_gen(n), 0)])
    return parts_cache[n]

def partsiter(n):
    parts_cache[n] = sum([parts_cache[n-x] if a % 4 < 2 else -parts_cache[n-x] for a, x in enumerate(penta_gen(n))])
    return parts_cache[n]


if __name__ == '__main__':
    
    for a in range(1, 81):   
        b = parts(a)
    
    time1 = time.time()
    
    print(partitions(80))
    
    time2 = time.time()
    
    print(time2 - time1)
    
    print(partsiter(80))
    
    print(time.time() - time2)

    for a in range(1, 1600):   
        b = parts(a)
        print(a, b, b%1000000)
        
    for x in range(1600, 100000):
        y = partsiter(x)
        print(x, y)
        if y % 1000000 == 0:
            break
