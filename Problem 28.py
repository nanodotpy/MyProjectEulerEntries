def quadratic(x,a,b,c) : #Got the 4 quadratic expressions using this and doing lots of tests to find the correct a b c coefficients
    return a*x**2+b*x+c  

"""
gauche = [1,7,21,43,73,111,157,211]


for a in range(-100,100) :
    for b in range(-100,100) :
        for c in range(-100,100):
            if quadratic(0,a,b,c) == gauche[0] :
                if quadratic(1,a,b,c) == gauche[1] :
                    if quadratic(2,a,b,c) == gauche[2] :
                        print(a,b,c)
                        """

a = [a**2 for a in range(3,1002,2)]

c = [4*c**2 + 1 for c in range(1,501)]
    
e = [4*e**2 -2*e + 1 for e in range(1,501)]

y = [4*y**2 + 2*y + 1 for y in range(1,501)]

print(a[:5])
print(c[:5])
print(e[:5])
print(y[:5])

print(1+sum(a) + sum(c) + sum(e) + sum(y))