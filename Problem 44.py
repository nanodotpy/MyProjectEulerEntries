def pentagonal(n) :
    return n*(3*n-1)/2

pentagonals = [int(pentagonal(n)) for n in range(1,100000)]

def somme_and_diff(number) :
    
    for a in pentagonals[:pentagonals.index(number)+1] :
        if a + number in pentagonals :
            if number-a in pentagonals : 
                return number - a
        
for number in pentagonals :
    if somme_and_diff(number) != None :
        print(somme_and_diff(number))
        break
    
    
    #Not efficient at all
    