def number_to_set(number) :
    number = str(number)
    set1 = set(number)
    set1 = {int(element) for element in set1}
    return set1


def permuted_multiples(number,m = 6) :
    for a in range(2,m+1):
        if not number_to_set(number*a) == number_to_set(number) :
            break
    else :
        return True
    return False

n = 1

while not permuted_multiples(n) :
    n += 1
    
print(n)


            
            
    