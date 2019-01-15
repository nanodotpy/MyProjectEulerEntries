def collatz_counter(a) :
    count = 1
    while not a == 1 :
        count += 1
        if a % 2 == 0 :
            a = a/2
        else :
            a = 3*a + 1
    else : 
        return count
    
    
bestlist = [] 
    
for a in range(1,1000000) :
    bestlist.append(collatz_counter(a))
    
print(max(bestlist))

print(int(bestlist.index(max(bestlist)))+1)
    

    