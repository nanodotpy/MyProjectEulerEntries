from math import factorial

def factorials_of_digits(number):
    result = 0
    for a in str(number):
        result += factorial(int(a))
    return result
    
big_counter = 0

for i in range(1, 1000000):
    chains = [i]
    index = 0
    while not factorials_of_digits(chains[index]) in chains:
        chains.append(factorials_of_digits(chains[index]))
        index += 1 
        if len(chains) > 60:
            break
    if len(chains) == 60:
        big_counter += 1
        
print(big_counter)