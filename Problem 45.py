def triangular(n) :
    return n*(n+1)//2

def hexa(n) :
    return n*(2*n-1)

def penta(n):
    return n*(3*n-1)//2

triangles = [triangular(n) for n in range(1,150000)]
hexas = [hexa(n) for n in range(1,150000)]
pentas = [penta(n) for n in range(1,150000)]

for a in triangles :
    if a in hexas and a in pentas and a > 40755 : 
        print(a)
        break