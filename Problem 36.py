def is_both_bases_palindrome(number) :
    binnumber = str(bin(number))[2:]
    number = str(number)

    if number[::-1] == number and binnumber[::-1] == binnumber :
        return True
    else :
        return False
    
somme = 0
    
for a in range(1000000):
    if is_both_bases_palindrome(a):
        somme += a
        
print(somme)
    

