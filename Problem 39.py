def perimeter_to_length(perimeter) :
    
    p = int(perimeter)
    
    solutions = 0
    
    for a in range(1,p//2 + 1) :
        for b in range(a,p//2 + 1) :
            c = p- a - b 
            if c**2  == a ** 2 + b**2 :
                solutions += 1
    return solutions
    
final = 0

for a in range(3,1001) :
    if perimeter_to_length(a) > final :
        final = perimeter_to_length(a)
        print("highest perimeter value so far : {}".format(a))

    