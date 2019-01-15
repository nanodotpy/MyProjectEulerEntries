def pytho(a,b) :
    c = 1000 -a -b
    if a**2 + b**2 == c**2 :
        return True
        
for a in range(1,1000):
    for b in range(1,1000):
        if pytho(a,b) :
            print(a*b*(1000-a-b))
    
