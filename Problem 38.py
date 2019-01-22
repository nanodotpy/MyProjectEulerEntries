def concatenate(number) :
    
    integer = number
    
    conca = str(integer)
    a = 2
    while len(conca) != 9 :
        conca  = conca + str(integer*a)
        
        a += 1
        
        if len(conca) > 9 :
            return False
        
    sett = set(conca) 
    sett = {int(value) for value in sett}
    if sett == set(range(1,10)) :
        return True
    else : 
        return False 
    
for a in range(10000) : 
    if concatenate(a) :
        print(a)
        print(str(a)+str(a*2))        #Just gotta take the biggest
        
    
        
