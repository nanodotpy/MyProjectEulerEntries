def number_reverse(number) :
    number = str(number)
    number =number[::-1]
    number = int(number)
    return number

def palindromic(number) :
    reverse = str(number_reverse(number))
    if str(number) == reverse[::-1] and number == number_reverse(number):
        return True
    else :
        return False

def lychrel_number(number) :
    b = 0
    while b < 50 :
        b +=1
        number += number_reverse(number)
        if palindromic(number) :
            return False
    else :
        return True
    
total = 0
        
for a in range(10000):
    if lychrel_number(a) :
        total +=1
        
print(total)