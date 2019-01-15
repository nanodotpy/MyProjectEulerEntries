import math

fact = str(math.factorial(100))

numlist = []

for letter in fact :
    numlist.append(int(letter)) 
    
print(sum(numlist))