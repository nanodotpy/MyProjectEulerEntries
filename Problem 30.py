somme = 0

for a in range(0,1000000) :
    
    u = 0
    p = 0
    o = 0
        
    if len(str(a)) == 1 and a != 1 :
        z = int(str(a)[0])
        e = 0
        r = 0
        t = 0
        y = 0
    
    if len(str(a)) == 2 :
        z = int(str(a)[0])
        e = int(str(a)[1])
        r = 0
        t = 0
        y = 0
    
    if len(str(a)) == 3 :
        z = int(str(a)[0])
        e = int(str(a)[1])
        r = int(str(a)[2])
        t = 0
        y = 0
    
    if len(str(a)) == 4 :
        z = int(str(a)[0])
        e = int(str(a)[1])
        r = int(str(a)[2])
        t = int(str(a)[3])
        y = 0
    
    
    if len(str(a)) == 5 :
        z = int(str(a)[0])
        e = int(str(a)[1])
        r = int(str(a)[2])
        t = int(str(a)[3])
        y = int(str(a)[4])
    
    if len(str(a)) == 6 :
        z = int(str(a)[0])
        e = int(str(a)[1])
        r = int(str(a)[2])
        t = int(str(a)[3])
        y = int(str(a)[4])
        u = int(str(a)[5])
        
    if z**5 + e**5+ r**5 + t**5 + y**5 + u**5 + p**5 + o**5  == a :
        print(a)
        somme += a
        
        
print(somme)
        
