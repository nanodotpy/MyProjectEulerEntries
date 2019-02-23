from math import ceil, sqrt

def is_harshad(number):
    """
    return if a number is harshad number or not
    """
    sum_of_his_digits = sum([int(digit) for digit in str(number)])
    try:
        if number % sum_of_his_digits == 0:
            return number % sum_of_his_digits
    except ZeroDivisionError: 
        pass
    
def is_prime(number):
    """
    returns if a number is prime or not
    """
    if number == 2:
        return True

    list0 = [2] + list(range(3, ceil(sqrt(number))+1, 2))
    for i in list0:
        if number % i == 0:
            break
    else:
        return True
    
    return False

PRIMES = [x for x in range(1,10000) if is_prime(x)]

def strong_harshad(number):
    if is_prime(is_harshad(number)):
        return True
    
def right_truncatable_harshad_prime(number):
    if len(str(number)) == 1:
        return {number}
    number = int(str(number)[:-1])
    n = len(str(number))
    
    for i in range(n):
        if is_harshad(int(str(number)[-i:])) is None or strong_harshad(int(str(number)[:-1])) is None:
            break
    else:
        return set([int(str(number)[-i:]) for i in range(n)])
            
a = 0

for j in PRIMES:
    print(j)
    if right_truncatable_harshad_prime(j) is not None:
        print(j)
        a += j
        
print(a)


    
        
        
    